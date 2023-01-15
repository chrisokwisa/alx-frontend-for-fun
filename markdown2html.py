#!/usr/bin/python3
""" Has a script markdown2html """


#!/usr/bin/python3
import sys

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

markdown_file = sys.argv[1]
html_file = sys.argv[2]

try:
    with open(markdown_file, 'r') as f:
        markdown_text = f.read()
except FileNotFoundError:
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)

# Add ordered list extension to Markdown
md = markdown.Markdown(extensions=['markdown.extensions.olist'])
html = md.convert(markdown_text)

with open(html_file, 'w') as f:
    f.write(html)

sys.exit(0)
