#!/usr/bin/python3
""" has a markdown script """


import sys
import markdown


def markdown2html(input_file, output_file):
    """ Takes an argument 2 strings
    Second argument is the output file name """
    try:
        with open(input_file, 'r') as f:
            markdown_text = f.read()
    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    html = markdown.markdown(markdown_text)

    with open(output_file, 'w') as f:
        f.write(html)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        markdown2html(input_file, output_file)
        sys.exit(0)
