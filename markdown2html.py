#!/usr/bin/python3
""" Has a script that runs the markdown html """


import sys


def markdown2html(input_file, output_file):
    """ Takes an argument 2 strings """
    try:
        with open(input_file, 'r') as f:
            markdown_text = f.read()
    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Add ordered list extension to Markdown
    md = markdown.Markdown(extensions=['markdown.extensions.olist'])
    html = md.convert(markdown_text)

    with open(output_file, 'w') as f:
        f.write(html)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        markdown2html(input_file, output_file)
        sys.exit(0)
