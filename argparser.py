import argparse
import tomli


def get_args():
    parser = argparse.ArgumentParser(description="Process .txt and .md files to .html")
    parser.add_argument(
        "path", nargs="?", help="path to the file or folder to be processed"
    )
    parser.add_argument(
        "--version", "-v", action="store_true", help="print the tool's name and version"
    )
    parser.add_argument(
        "--output",
        "-o",
        default="./html/examples",
        help="Specify a different output directory",
    )
    parser.add_argument(
        "--lang",
        "-l",
        default="en-CA",
        help="Specify the language for the lang attribute in the HTML document",
    )
    parser.add_argument("--config", "-c", help="Specify a different config file")

    args = parser.parse_args()

    # Handle TOML config logic
    if args.config:
        try:
            with open(args.config, "rb") as f:
                default_values = {
                    "path": None,
                    "output": "./html/examples",
                    "lang": "en-CA",
                    "version": False,
                }

                toml_dict = tomli.load(f)

                # Convert the dict to a Namespace object
                args = argparse.Namespace(**toml_dict)

                # Set any missing args to their default values
                for key, value in default_values.items():
                    setattr(args, key, getattr(args, key, value))
        except tomli.TOMLDecodeError:
            print(f"Error: {args.config} is not a valid config TOML file.")
            return None
        except FileNotFoundError:
            print(f"Error: {args.config} does not exist.")
            return None
        except IsADirectoryError:
            print(
                f"Error: {args.config} is a directory. Must provide path to config file."
            )
            return None

    return args
