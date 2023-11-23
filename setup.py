from setuptools import setup, find_packages

setup(
    name="tml_mnajibi",
    version="0.1.0",
    author="Maryam Najibi",
    author_email="maryamnajibi55@gmail.com",  # Replace with your actual email
    description="A command-line tool to convert .txt and .md files to .html format",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mnajibi/tml",  # Replace with the URL of your project
    package_dir={"": "src"},  # New line to specify the source directory
    packages=find_packages(
        where="src"
    ),  # Modified to find packages in the 'src' directory
    install_requires=[
        "tomli",  # For TOML file parsing
        "requests",  # For validating links in markdown_link_replacer.py
    ],
    entry_points={
        "console_scripts": [
            "tml=main:main",  # Allows users to run your script using 'tml' command
        ],
    },
    classifiers=[
        # Add classifiers to help users find your project
        # Refer to https://pypi.org/classifiers/ for a full list
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify the minimum Python version required
)
