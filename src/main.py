#!/opt/anaconda3/bin/python
# /usr/bin/env python3
import os
import shutil
from converter import TxtConverter, MdConverter
from argparser import get_args
from markdown_link_replacer import replace_links


def process_file(file_path, lang, output_dir):
    with open(file_path, "r") as f:
        content = f.read()

    if file_path.endswith(".txt"):
        updated_content, broken_links = replace_links(
            file_path, content, is_markdown=False
        )
        TxtConverter.create_html_from_txt(file_path, updated_content, lang, output_dir)
    elif file_path.endswith(".md"):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        # Save the updated_content back to file or handle it as needed
        updated_content, broken_links = replace_links(
            file_path, content, is_markdown=True
        )
        # Handle broken_links as needed, for example, print a warning or error message
        if broken_links:
            print(f"Broken links found in {file_path}: {broken_links}")
        MdConverter.create_html_from_md(file_path, updated_content, lang, output_dir)


def main():
    args = get_args()
    # Check if the version flag is passed and print the version.
    if args.version:
        print("tml Tool Version 0.0.3")
        return

    # Check if the path is provided.
    if not args.path:
        print("Please provide a valid path using the path argument.")
        return

    # Check if the output directory is specified.
    if args.output:
        print(f"Output directory set to: {args.output}")

    # Check if the language is specified.
    if args.lang:
        print(f"Language set to: {args.lang}")

    # Handle file or directory processing
    if os.path.isfile(args.path):
        process_file(args.path, args.lang, args.output)
    elif os.path.isdir(args.path):
        if os.path.exists(args.output):
            shutil.rmtree(args.output)
        for root, dirs, files in os.walk(args.path):
            for file in files:
                process_file(os.path.join(root, file), args.lang, args.output)


if __name__ == "__main__":
    main()
