# tml - Text to HTML Converter

## Overview

`tml` is a simple command-line tool that converts `.txt` files into `.html` format. The tool automatically wraps paragraphs from the input `.txt` file in `<p>...</p>` tags in the resulting `.html` file.

# Installation

To install `tml`, simply clone this repository to your local machine.

``
git clone <repository-url>
cd tml
``

Ensure `main.py is` executable:

``
chmod +x main.py
``
# Usage

To convert a `.txt` file to `.html`:

``
./main.py <path-to-txt-file>
``

This will produce a corresponding .html file inside the `tml` directory.

# Command Options:

* `--version` or `-v`: Display the tool's version.
* `--path`: Specify the path to a `.txt` file or a directory containing multiple .txt files. If a directory is provided, `tml` will recursively process all `.txt` files within.

# Features

* 📄 Converts single or multiple `.txt` files to `.html`.
* 🖋 Automatic paragraph wrapping in `<p>...</p>` tags.
* 📁 Outputs to a `tml` directory.
* 🔄 Overwrites existing `tml` directory to ensure it only contains the most recent outputs.


# Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

# License

[GNU](https://github.com/mnajibi/tml/blob/main/LICENSE)
