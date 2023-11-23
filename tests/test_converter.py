import os
import pytest
from src.converter import TxtConverter, MdConverter


@pytest.fixture
def setup_files(tmp_path):
    # Create the directory 'test_html_output' inside the temporary path
    test_dir = tmp_path / "test_html_output"
    os.makedirs(test_dir, exist_ok=True)  # Ensure the directory is created

    # Define file paths
    test_txt_file = test_dir / "test.txt"
    test_md_file = test_dir / "test.md"
    expected_html_output_for_txt = test_dir / "test.html"

    # Create sample files for conversion
    test_txt_file.write_text("Title\n\n\nThis is a test.")
    test_md_file.write_text("# Markdown Title\n\nThis is a test using markdown.")

    # Return the paths in a dictionary so they can be used in tests
    yield {
        "test_dir": test_dir,
        "test_txt_file": test_txt_file,
        "test_md_file": test_md_file,
        "expected_html_output_for_txt": expected_html_output_for_txt,
    }

    # No explicit teardown needed; tmp_path is a fixture that cleans up after itself


def test_txt_to_html_conversion(setup_files):
    # Run the conversion
    TxtConverter.create_html_from_txt(
        str(setup_files["test_txt_file"]), output_dir=str(setup_files["test_dir"])
    )
    # Define the expected output file path for text conversion
    expected_html_output_for_txt = setup_files["test_txt_file"].with_suffix(".html")
    # Check if the HTML file is created
    assert (
        expected_html_output_for_txt.exists()
    ), "The HTML file expected from txt conversion does not exist."


def test_md_to_html_conversion(setup_files):
    # Run the conversion
    MdConverter.create_html_from_md(
        str(setup_files["test_md_file"]), output_dir=str(setup_files["test_dir"])
    )
    # Define the expected output file path for Markdown conversion
    expected_html_output_for_md = setup_files["test_md_file"].with_suffix(".html")
    # Check if the HTML file is created
    assert expected_html_output_for_md.exists()
