# test_argparser.py
import pytest
from ..argparser import get_args


# This is necessary to replace argv for the tests
@pytest.fixture
def mock_argv(monkeypatch):
    def _mock_argv(args):
        monkeypatch.setattr("sys.argv", args)

    return _mock_argv


def test_get_args_no_arguments(mock_argv):
    mock_argv(["main.py"])
    args = get_args()
    assert args.path is None
    assert not args.version
    assert args.output == "./html/examples"
    assert args.lang == "en-CA"
    assert args.config is None


def test_get_args_with_path(mock_argv):
    test_path = "/path/to/file.txt"
    mock_argv(["main.py", test_path])
    args = get_args()
    assert args.path == test_path


def test_get_args_with_version(mock_argv):
    mock_argv(["main.py", "--version"])
    args = get_args()
    assert args.version is True


def test_get_args_with_output(mock_argv):
    test_output = "/custom/output"
    mock_argv(["main.py", "--output", test_output])
    args = get_args()
    assert args.output == test_output


def test_get_args_with_lang(mock_argv):
    test_lang = "fr-CA"
    mock_argv(["main.py", "--lang", test_lang])
    args = get_args()
    assert args.lang == test_lang
