
# Contributing to tml - Text to HTML Converter

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Getting Started

## Installation for Development

```bash
git clone https://github.com/mnajibi/tml.git
cd tml
chmod +x main.py
```


## Development and Testing

Before sending a pull request, please make sure the following is done:

- Fork the repo and create your branch from main.
- If you've added code, add tests.
- Ensure your code works with the existing tests.
- Update the documentation if necessary.

When you're ready to create a pull request, be sure to:

+ Write a clear log message for your commits. One-line messages are fine for small changes, but bigger changes should look like this:
```bash
$ git commit -m "A brief summary of the commit
>
> A paragraph describing what changed and its impact."
```

## Code Style and Formatting

This project enforces a consistent code style provided by Black, the uncompromising Python code formatter. Make sure you run Black before committing your code. You can install it and format code as follows:

### Installing Black

```bash
pip install black
```

### Formatting Code with Black

Run Black to format your code:

```bash
black .
```
Commit your changes after formatting:
```bash
git add .
git commit -m "Formatted with Black"
```

Check if your code conforms to Black's style:
```bash
black --check .
```

### Using the Linter (Flake8)

This project also enforces good code practices and adheres to PEP 8 style guidelines using Flake8. To ensure your code is clean and follows the project's coding standards, you should run Flake8 before committing your changes.

#### Installing Flake8

```bash
pip install flake8
```

## Running Flake8
To check your code for errors and style issues:

```bash
flake8 path/to/your/code/
```
If Flake8 points out any issues, try to resolve them to maintain the code quality. Some issues can be ignored if they are not critical or if they have been agreed upon by the maintainers (see .flake8 configuration file).

### Flake8 Configuration
The project has a `.flake8` configuration file which you can find at the root of the repository. If there are rules that we have agreed to ignore as a project, they will be listed there.

### Submitting changes

Please send a GitHub Pull Request to tml with a clear list of what you've done (read more about pull requests). When you send a pull request, we will love you forever if you include tests. We can always use more test coverage. Please make sure all of your commits are atomic (one feature per commit).

Always write a clear log message for your commits. One-line messages are fine for small changes, but larger changes should have a paragraph describing what changed and why.

### Reporting Bugs

We use GitHub issues to track public bugs. Report a bug by opening a new issue; it's that easy!

Thank you for contributing to `tml`!