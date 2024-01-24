from pathlib import Path

import pytest

from encephalon.parsing import parse_notes


def test_successful_parse_notes(match_path):
    pytest.assume(isinstance(match_path, Path))
    pytest.assume(isinstance(parse_notes(match_path), list))
    pytest.assume(len(parse_notes(match_path)) == 1)


def test_unsuccessful_parse_notes(no_match_path):
    pytest.assume(isinstance(no_match_path, Path))
    pytest.assume(isinstance(parse_notes(no_match_path), list))
    pytest.assume(len(parse_notes(no_match_path)) == 0)
