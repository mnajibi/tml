# tml - Text to HTML Converter

## Overview

`tml` is a simple command-line tool that converts `.txt` files into `.html` format. The tool automatically wraps paragraphs from the input `.txt` file in `<p>...</p>` tags in the resulting `.html` file.

## Installation

To install `tml`, simply clone this repository to your local machine.

`
git clone https://github.com/mnajibi/tml.git
cd tml
`

Ensure `main.py is` executable:

`
chmod +x main.py
`
## Usage

To convert a `.txt` file to `.html`:

`
./main.py <path-to-txt-file>
`

To specify a different output directory:

`
./main.py <path-to-txt-file> --output <path-to-output-directory>
`

By default, if no output directory is specified, the `.html` files will be saved inside the `tml/examples` directory.

## Command Options:

* `--version` or `-v`: Display the tool's version.
* `path`: Specify the path to a `.txt` file or a directory containing multiple .txt files. If a directory is provided, `tml` will recursively process all `.txt` files within.
* `--output` or `-o`: Specify a custom output directory. The tool will create the directory if it does not exist.

## Features

* 📄 Converts single or multiple `.txt` files to `.html`.
* 🖋 Automatic paragraph wrapping in `<p>...</p>` tags.
* 📁 Can output to a custom directory or default to `tml/examples`.
* 🔄 Overwrites existing output directory content to ensure it contains only the most recent outputs.
* 🎉 Extracts title from the text file if present. The title is identified as the first line followed by two blank lines.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## License

[MIT](https://github.com/mnajibi/tml/blob/main/LICENSE)

