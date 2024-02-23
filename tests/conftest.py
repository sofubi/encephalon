import pytest

MATCH = """@@note@@
$stuff
# stuff
#stuff
THIS is a note
@@end@@
"""


NO_MATCH = """@note@
$stuff
# stuff
#stuff
THIS is a note
@end@
"""


@pytest.fixture(scope="session")
def match_path(tmp_path_factory):
    file = tmp_path_factory.mktemp("notes") / "match_note.txt"
    file.write_text(MATCH, encoding="utf-8")
    return file


@pytest.fixture(scope="session")
def no_match_path(tmp_path_factory):
    file = tmp_path_factory.mktemp("notes") / "no_match.txt"
    file.write_text(NO_MATCH, encoding="utf-8")
    return file
