from mmap import ACCESS_READ, mmap
from os import PathLike
from pathlib import Path
from re import Pattern, compile

NOTE_START: str = "@@note@@"
NOTE_END: str = "@@end@@"

NOTE_PATTERN: Pattern[bytes] = compile(f"{NOTE_START}\n((?:.+\n)+){NOTE_END}".encode())

TESTING = b"""@@note@@
$stuff
# stuff
#stuff
THIS is a note
@@end@@
"""


def parse_notes(file: Path) -> list[str]:
    matches: list[str] = []

    with open(file, "rb") as f:
        mm = mmap(f.fileno(), 0, access=ACCESS_READ)
        matches = [n.decode("utf-8") for n in NOTE_PATTERN.findall(mm)]

    if len(matches) < 1:
        print("No matching notes found.\nNo action taken.")

    return matches


def fetch_path(file: str | PathLike) -> Path:
    if isinstance(file, Path):
        return file

    if file is not None and isinstance(file, str):
        try:
            file = Path(file).expanduser()
        except FileNotFoundError as e:
            print(f"No file found at given path: {e}")
            raise
        except Exception as e:
            print(f"Exception while finding file at given path: {e}")
            raise

        return file

    print(f"{file} is an invalid filepath.")
    raise OSError
