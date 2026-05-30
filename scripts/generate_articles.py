from pathlib import Path
import subprocess

ARTICLES_DIR = Path("articles")
PDF_DIR = Path("pdfs")
HTML_DIR = Path("docs/articles")

PDF_DIR.mkdir(exist_ok=True)
HTML_DIR.mkdir(parents=True, exist_ok=True)

for md_file in ARTICLES_DIR.glob("*.md"):

    name = md_file.stem

    html_file = HTML_DIR / f"{name}.html"
    pdf_file = PDF_DIR / f"{name}.pdf"

    if not html_file.exists():
        subprocess.run([
            "pandoc",
            str(md_file),
            "--standalone",
            "--toc",
            "--template=templates/medium.html",
            "-o",
            str(html_file)
        ], check=True)

    if not pdf_file.exists():
        subprocess.run([
            "pandoc",
            str(md_file),
            "--pdf-engine=xelatex",
            "-V", "geometry:margin=1in",
            "-V", "fontsize=12pt",
            "-o",
            str(pdf_file)
        ], check=True)

print("Generation complete.")
