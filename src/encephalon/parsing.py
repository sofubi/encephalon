from os import PathLike
from pathlib import Path

NOTE_START: str = "@@note@@"
NOTE_END: str = "@@end@@"


def parse_notes(file: Path) -> list[str]:
    matches: list[str] = []

    with open(file, "r") as f:
        innote: bool = False
        match: int = 0
        for line in f:
            if innote:
                if NOTE_END in line:
                    innote = False
                    continue

                if (match - 1) < len(matches):
                    matches[match - 1] = "\n".join(
                        [matches[match - 1], line.strip("\n\r")]
                    )
                else:
                    matches.append(line.strip("\n\r"))

            if NOTE_START in line:
                innote = True
                match += 1

    if len(matches) < 1:
        print("No matching notes found.\nNo action taken.")

    return matches


def fetch_path(file: str | PathLike) -> Path:
    if isinstance(file, Path):
        return file

    if file is not None and isinstance(file, str):
        try:
            file = Path(file).expanduser()
        except Exception as e:
            print(f"Error finding file: {e}")
            raise FileNotFoundError from e

        return file

    print(f"{file} is an invalid filepath.")
    raise OSError


def fetch_parse(file: Path) -> list[str]:
    return parse_notes(fetch_path(file))
