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
    html_lines = []
    in_list = False
    in_para = False
    for line in lines:
        if line.startswith("# "):
            if in_para:
                html_lines.append("</p>")
                in_para = False
            if in_list:
                html_lines.append("</ol>")
                in_list = False
            html_lines.append("<h1>" + line[2:] + "</h1>")
        elif line.startswith("## "):
            if in_para:
                html_lines.append("</p>")
                in_para = False
            if in_list:
                html_lines.append("</ol>")
                in_list = False
            html_lines.append("<h2>" + line[3:] + "</h2>")
        elif line.startswith("### "):
            if in_para:
                html_lines.append("</p>")
                in_para = False
            if in_list:
                html_lines.append("</ol>")
                in_list = False
            html_lines.append("<h3>" + line[4:] + "</h3>")
        elif line.startswith("#### "):
            if in_para:
                html_lines.append("</p>")
                in_para = False
            if in_list:
                html_lines.append("</ol>")
                in_list = False
            html_lines.append("<h4>" + line[5:] + "</h4>")
        elif line.startswith("##### "):
            if in_para:
                html_lines.append("</p>")
                in_para = False
            if in_list:
                html_lines.append("</ol>")
                in_list = False
            html_lines.append("<h5>" + line[6:] + "</h5>")
        elif line.startswith("1. ") or (in_list and line.startswith("  1. ")):
            if not in_list:
                html_lines.append("<ol>")
                in_list = True
            if line.startswith("  1. "):
                line = line[4:]


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
