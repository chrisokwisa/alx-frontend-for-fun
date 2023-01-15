#!/usr/bin/python3
""" Has a script markdown2html """


import sys


def markdown2html(input_file, output_file):
    """ Takes an argument 2 strings """
    try:
        with open(input_file, 'r') as f:
            markdown_text = f.read()
    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)
    lines = markdown_text.split("\n")
    html_lines = []

    for line in lines:
        if line.startswith("- "):
            html_lines.append("<li>" + line[2:] + "</li>")
        else:
            if html_lines[-1] != "<ul>":
                html_lines.append("</ul>")
            html_lines.append(line)
    if html_lines[-1] != "<ul>":
        html_lines.append("</ul>")
    html_text = "\n".join(html_lines)
    with open(output_file, 'w') as f:
        f.write(html_text)


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
