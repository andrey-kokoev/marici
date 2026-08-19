"""Extract readable text from arXiv HTML, preserving math alttext as $...$."""
import re, html, sys

src = open("2607.27315v1.html", encoding="utf-8").read()

# Replace math elements with their alttext LaTeX
def math_repl(m):
    alt = re.search(r'alttext="((?:[^"\\]|\\.)*)"', m.group(0))
    if alt:
        tex = html.unescape(alt.group(1))
        display = "display" in m.group(0)[:200]
        return "\n$$\n" + tex + "\n$$\n" if display else " $" + tex + "$ "
    return " "

src = re.sub(r"<math\b.*?</math>", math_repl, src, flags=re.S)
# Drop scripts/styles
src = re.sub(r"<(script|style)\b.*?</\1>", " ", src, flags=re.S)
# Mark headings and paragraphs
src = re.sub(r"<h([1-6])\b[^>]*>", lambda m: "\n\n" + "#" * int(m.group(1)) + " ", src)
for tag in ("p", "div", "section", "li", "tr", "table", "figure", "figcaption", "blockquote"):
    src = re.sub(r"</?%s\b[^>]*>" % tag, "\n", src)
src = re.sub(r"<br\b[^>]*>", "\n", src)
src = re.sub(r"<[^>]+>", "", src)
src = html.unescape(src)
src = re.sub(r"[ \t]+", " ", src)
src = re.sub(r"\n\s*\n\s*\n+", "\n\n", src)
open("2607.27315v1.txt", "w", encoding="utf-8").write(src)
print(len(src), "chars")
