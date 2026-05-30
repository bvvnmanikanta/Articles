from pathlib import Path

articles = sorted(Path("articles").glob("*.md"))

html = """
<!DOCTYPE html>
<html>
<head>
<title>Technical Articles</title>
<link rel="stylesheet" href="assets/medium.css">
</head>
<body>

<main>
<h1>Technical Articles</h1>
"""

for article in articles:

    title = article.stem.replace("-", " ").title()

    html += f"""
    <article>
      <h2>{title}</h2>

      <div class="button-container">
          <a class="btn" href="articles/{article.stem}.html">
            Read Online
          </a>
        
          <a class="btn" href="../pdfs/{article.stem}.pdf">
            Download PDF
          </a>
      </div>

      <hr>
    </article>
    """

html += """
</main>
</body>
</html>
"""

Path("docs").mkdir(exist_ok=True)

with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(html)
