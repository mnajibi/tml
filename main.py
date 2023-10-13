#!/opt/anaconda3/bin/python
#/usr/bin/env python3
import argparse
import os
import shutil
import re
import tomli

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

def create_html_from_md(filepath, lang='en-CA' , output_dir='./html/examples'):
    os.makedirs(output_dir, exist_ok=True)

    # Read the Markdown content from the input file
    with open(filepath, 'r', encoding='utf-8') as md_file:
        markdown_content = md_file.read()

    # Split the Markdown content into lines
    lines = markdown_content.split('\n')

    # Initialize an empty HTML content string
    html_body_content = ""
    current_paragraph=[]

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

   
def create_html_from_txt(filepath, lang='en-CA' ,output_dir='./tml/examples'):
    with open(filepath, 'r') as f:
        content = f.read()

    title, body_content = process_file_content(content)

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

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, os.path.basename(filepath).replace('.txt', '.html'))
    with open(output_file, 'w') as f:
        f.write(html_content)


def main():
 try: 
    parser = argparse.ArgumentParser(description='Process .txt files to .html')
    parser.add_argument('path', nargs='?', help='path to the file or folder to be processed')
    parser.add_argument('--version', '-v', action='store_true', help='print the tool\'s name and version')
    parser.add_argument('--output', '-o', default='./tml/examples', help='Specify a different output directory')
    parser.add_argument('--lang', '-l', default='en-CA', help='Specify the language for the lang attribute in the HTML document')
    parser.add_argument('--config', '-c', help='Specify a different config file')

 

    args = parser.parse_args()


    if args.config:
        try:
            with open(args.config, "rb") as f:
                default_values = {
                    'path': None,
                    'output': './tml/examples',
                    'lang': 'en-CA',
                    'version': False
                }
                
                toml_dict = tomli.load(f)
                
                # Convert the dict to a Namespace object 
                args = argparse.Namespace(**toml_dict)

                # Set any missing args to their default values
                for key, value in default_values.items():
                    setattr(args, key, getattr(args, key, value))
        except tomli.TOMLDecodeError:
            print(f"Error: {args.config} is not a valid config TOML file.")
            return(-1)
        except FileNotFoundError:
            print(f"Error: {args.config} does not exist.")
            return(-1)
        except IsADirectoryError:
            print(f"Error: {args.config} is a directory. Must provide path to config file.")
            return(-1)


    if args.version:
        print("tml Tool Version 0.0.3")
        return(0)

    if not args.path:
        parser.error("the following arguments are required: path")
        return(-1)

    if not os.path.exists(args.path):
        print(f"Error: {args.path} does not exist.")
        return(-1)

    if os.path.isfile(args.path) and args.path.endswith('.txt'):
        create_html_from_txt(args.path, args.lang, args.output)
    elif os.path.isfile(args.path) and args.path.endswith('.md'):
        create_html_from_md(args.path, args.lang, args.output)
    elif os.path.isdir(args.path):
        if os.path.exists(args.output):
            shutil.rmtree(args.output)
        for root, dirs, files in os.walk(args.path):
            for file in files:
                if file.endswith('.txt'):
                     create_html_from_txt(os.path.join(root, file), args.lang, args.output)  # pass output directory here
                elif file.endswith('.md'):
                     create_html_from_md(os.path.join(root, file), args.lang, args.output)

 except Exception as e:
    print(f"An unexpected error occurred: {e}")
    return(-1)  # Here sys is already defined by the import statement at the top

 return(0)  # If no error occurs, exit with code 0              



                     


if __name__ == '__main__':
    main()