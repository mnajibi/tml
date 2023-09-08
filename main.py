#!/usr/bin/env python3

import argparse
import os
import shutil

def process_file_content(content):
    paragraphs = content.split("\n\n")
    html_paragraphs = [f"<p>{p.strip()}</p>" for p in paragraphs if p.strip()]
    return "\n".join(html_paragraphs)

def create_html_from_txt(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    body_content = process_file_content(content)

    html_content = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{os.path.basename(filepath)}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  {body_content}
</body>
</html>"""

    output_dir = './tml'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, os.path.basename(filepath).replace('.txt', '.html'))
    with open(output_file, 'w') as f:
        f.write(html_content)

def main():
    parser = argparse.ArgumentParser(description='Process .txt files to .html')
    parser.add_argument('path', nargs='?', help='path to the file or folder to be processed')
    parser.add_argument('--version', '-v', action='store_true', help='print the tool\'s name and version')

    args = parser.parse_args()

    if args.version:
        print("tml Tool Version 1.0.0")
        return

    if not args.path:
        parser.error("the following arguments are required: path")

    if not os.path.exists(args.path):
        print(f"Error: {args.path} does not exist.")
        return

    if os.path.isfile(args.path) and args.path.endswith('.txt'):
        create_html_from_txt(args.path)
    elif os.path.isdir(args.path):
        if os.path.exists('./tml'):
            shutil.rmtree('./tml')
        for root, dirs, files in os.walk(args.path):
            for file in files:
                if file.endswith('.txt'):
                    create_html_from_txt(os.path.join(root, file))

if __name__ == '__main__':
    main()



