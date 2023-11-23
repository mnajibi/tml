# Import pytest
import pytest


from src.markdown_link_replacer import replace_links


# pytest function to test replace_links with good values
def test_replace_links_good():
    # setup input data and expected output
    input_data = "Test content with a [link](https://www.google.com)"
    expected_output = 'Test content with a <a href="https://www.google.com">link</a>'
    # call replace_links
    output, broken_links = replace_links("test.md", input_data, True)
    # assert to check the output against the expected result
    assert (
        output == expected_output
    ), "replace_links did not return expected HTML content"


# Test replace_links with a broken link in markdown content
def test_replace_links_broken_link_markdown():
    input_data = "Test content with a [broken link](http://example.com/broken)"
    expected_output = (
        'Test content with a <a href="#" style="color:red;">broken link</a>'
    )
    output, broken_links = replace_links("test.md", input_data, True)
    assert output == expected_output
    assert broken_links == ["http://example.com/broken"]


# Test replace_links with valid link in plain text content
def test_replace_links_valid_link_plain_text():
    input_data = "This is a valid link: http://www.valid-link.com"
    expected_output = 'This is a valid link: <a href="http://www.valid-link.com">http://www.valid-link.com</a>'
    output, broken_links = replace_links("test.txt", input_data, False)
    assert output == expected_output
    assert broken_links == []
