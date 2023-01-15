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
      # Initialize an empty list to store the lines of HTML
    html_lines = []

    # Split the markdown text into lines
    for line in markdown_text.splitlines():
        # If the line starts with '#', it's a heading
        if line.startswith('#'):
            level = line.count('#')
            text = line.lstrip('#').lstrip()
            html_lines.append(f"<h{level}>{text}</h{level}>")
        # If the line starts with '-', it's a list item
        elif line.startswith('-'):
            text = line.lstrip('-').lstrip()
            html_lines.append(f"<li>{text}</li>")
        # Otherwise, it's a paragraph
        else:
            # check if the line contains bold syntax ** or __
            line = line.replace("**", "<b>").replace("__", "<em>")
            line = line.replace("**", "</b>").replace("__", "</em>")
            html_lines.append(f"<p>{line}</p>")
    # Join the list of lines into a single string of HTML
    html_text = '\n'.join(html_lines)

    with open(output_file, "w") as f:
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
