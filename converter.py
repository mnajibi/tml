import os
import re

class TxtConverter:
 @staticmethod
 def process_file_content(content):
    lines = content.split("\n")
    if len(lines) > 2 and lines[1] == "" and lines[2] == "":
        title = lines[0].strip()
        body_paragraphs = re.split(r"\r?\n\r?\n", "\n".join(lines[3:]))
    else:
        title = None
        body_paragraphs = re.split(r"\r?\n\r?\n", content)

    html_paragraphs = [f"<p>{p.strip()}</p>" for p in body_paragraphs if p.strip()]
    return title, "\n".join(html_paragraphs)
 @staticmethod
 def create_html_from_txt(filepath, lang='en-CA', output_dir='./html/examples'):
        with open(filepath, 'r') as f:
            content = f.read()

        title, body_content = TxtConverter.process_file_content(content)
        title_element = title if title else os.path.basename(filepath)
        h1_element = f"<h1>{title}</h1>\n" if title else ""

        html_content = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <title>{title_element}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/water.css"/>
</head>
<body>
  {h1_element}{body_content}
</body>
</html>"""

        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, os.path.basename(filepath).replace('.txt', '.html'))
        with open(output_file, 'w') as f:
            f.write(html_content)

class MdConverter:
 @staticmethod
 def create_html_from_md(filepath, lang='en-CA' , output_dir='./html/examples'):
    os.makedirs(output_dir, exist_ok=True)

    with open(filepath, 'r', encoding='utf-8') as md_file:
        markdown_content = md_file.read()

    lines = markdown_content.split('\n')
    html_body_content = ""
    current_paragraph = []

    for line in lines:
     if line.startswith('# '):
        # Close any open paragraph
        if current_paragraph:
            html_body_content += '<p>' + ' '.join(current_paragraph) + '</p>\n'
            current_paragraph = []
        # Add the heading
        html_body_content += f'<h1>{line[2:]}</h1>\n'
     elif line.startswith('## '):
        if current_paragraph:
            html_body_content += '<p>' + ' '.join(current_paragraph) + '</p>\n'
            current_paragraph = []
        html_body_content += f'<h2>{line[3:]}</h2>\n'
     elif line.startswith('### '):
        if current_paragraph:
            html_body_content += '<p>' + ' '.join(current_paragraph) + '</p>\n'
            current_paragraph = []
        html_body_content += f'<h3>{line[4:]}</h3>\n'
     elif line.strip():
        # Append non-empty lines to the current paragraph
        current_paragraph.append(line)
     else:
        # If it's an empty line, close the current paragraph (if any)
        if current_paragraph:
            html_body_content += '<p>' + ' '.join(current_paragraph) + '</p>\n'
            current_paragraph = []

     # Close any remaining open paragraph
    if current_paragraph:
      html_body_content += '<p>' + ' '.join(current_paragraph) + '</p>\n'

    html_content = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <title>Document</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/water.css"/>
</head>
<body>
  {html_body_content}
</body>
</html>"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, os.path.basename(filepath).replace('.md', '.html'))
    with open(output_file, 'w') as f:
        f.write(html_content)
