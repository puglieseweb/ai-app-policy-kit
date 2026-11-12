#!/usr/bin/env python3
"""Build the Word, PDF and zip downloads from policies/*.md.

Needs pandoc (or `pip install pypandoc_binary`), `pip install python-docx`
and LibreOffice (`soffice`).
Usage: python3 tools/build.py [version]   ->   dist/
"""
import pathlib
import shutil
import subprocess
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
VERSION = sys.argv[1] if len(sys.argv) > 1 else "1.0"


def pandoc() -> str:
    found = shutil.which("pandoc")
    if found:
        return found
    import pypandoc  # the pip package that carries its own pandoc

    return pypandoc.get_pandoc_path()


def tidy(path: pathlib.Path) -> None:
    """Page margins, and tables a person can fill in: full width, ruled, a shaded heading row."""
    from docx import Document
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Cm, Pt

    doc = Document(str(path))
    for section in doc.sections:
        section.page_width, section.page_height = Cm(21), Cm(29.7)
        section.left_margin = section.right_margin = Cm(2)
        section.top_margin = section.bottom_margin = Cm(2)
    width = Cm(17)
    for table in doc.tables:
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = True
        props = table._tbl.tblPr
        for old in props.findall(qn("w:tblW")):
            props.remove(old)
        full = OxmlElement("w:tblW")
        full.set(qn("w:w"), "5000")
        full.set(qn("w:type"), "pct")
        props.append(full)
        borders = OxmlElement("w:tblBorders")
        for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
            line = OxmlElement(f"w:{edge}")
            line.set(qn("w:val"), "single")
            line.set(qn("w:sz"), "4")
            line.set(qn("w:color"), "B9B4C7")
            borders.append(line)
        props.append(borders)
        columns = len(table.columns)
        if not "".join(cell.text for cell in table.rows[0].cells).strip():
            table._tbl.remove(table.rows[0]._tr)  # a two-column form has no heading row
        for r, row in enumerate(table.rows):
            for cell in row.cells:
                cell.width = int(width / columns)
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        run.font.size = Pt(9)
                        if r == 0 and columns > 2:
                            run.font.bold = True
                if r == 0 and columns > 2:
                    shade = OxmlElement("w:shd")
                    shade.set(qn("w:val"), "clear")
                    shade.set(qn("w:fill"), "EEE9FA")
                    cell._tc.get_or_add_tcPr().append(shade)
    doc.save(str(path))


def main() -> None:
    shutil.rmtree(DIST, ignore_errors=True)
    word, pdf, md = DIST / "word", DIST / "pdf", DIST / "markdown"
    for folder in (word, pdf, md):
        folder.mkdir(parents=True)
    reference = ROOT / "tools" / "reference.docx"
    sources = sorted((ROOT / "policies").glob("*.md"))
    for source in sources:
        out = word / (source.stem + ".docx")
        cmd = [pandoc(), str(source), "--from", "gfm", "--to", "docx", "--output", str(out),
               "--metadata", "lang=en-GB"]
        if reference.exists():
            cmd += ["--reference-doc", str(reference)]
        subprocess.run(cmd, check=True)
        tidy(out)
        shutil.copy(source, md / source.name)
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(pdf),
                    *[str(p) for p in sorted(word.glob("*.docx"))]], check=True, stdout=subprocess.DEVNULL)
    bundle = DIST / f"ai-app-policy-kit-v{VERSION}.zip"
    with zipfile.ZipFile(bundle, "w", zipfile.ZIP_DEFLATED) as z:
        for name in ("README.md", "LICENSE"):
            z.write(ROOT / name, f"ai-app-policy-kit/{name}")
        for folder in (word, pdf, md):
            for f in sorted(folder.iterdir()):
                z.write(f, f"ai-app-policy-kit/{folder.name}/{f.name}")
    built = len(list(pdf.glob("*.pdf")))
    if built != len(sources):
        sys.exit(f"{built} PDFs for {len(sources)} documents")
    print(f"{len(sources)} documents -> {bundle.relative_to(ROOT)} ({bundle.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
