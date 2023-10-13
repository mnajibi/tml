#!/opt/anaconda3/bin/python
#/usr/bin/env python3
import os
import shutil
from converter import TxtConverter, MdConverter
from argparser import get_args

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
    if os.path.isfile(args.path) and args.path.endswith('.txt'):
        TxtConverter.create_html_from_txt(args.path, args.lang, args.output)
    elif os.path.isfile(args.path) and args.path.endswith('.md'):
        MdConverter.create_html_from_md(args.path, args.lang, args.output)
    elif os.path.isdir(args.path):
        if os.path.exists(args.output):
            shutil.rmtree(args.output)
        for root, dirs, files in os.walk(args.path):
            for file in files:
                if file.endswith('.txt'):
                    TxtConverter.create_html_from_txt(os.path.join(root, file), args.lang, args.output)
                elif file.endswith('.md'):
                    MdConverter.create_html_from_md(os.path.join(root, file), args.lang, args.output)

if __name__ == '__main__':
    main()
