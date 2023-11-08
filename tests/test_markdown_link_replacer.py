# Import pytest
import pytest


from ..markdown_link_replacer import replace_links


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
