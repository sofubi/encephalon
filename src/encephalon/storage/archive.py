# pass list of notes
# each note goes to either new note or appends old note
# note has dirpath on top ending with file name
from pathlib import Path

from encephalon.config import Config


def archive(notes: list[list[str]], config: Config):
    top_dir: Path = Path(config.notes_location).expanduser()

    if not top_dir.exists():
        top_dir.mkdir()

    for note in notes:
        note_path: Path = top_dir / note[0]
        note_dir: Path = note_path.parent

        if not Path(note_dir).exists():
            try:
                Path(note_dir).mkdir()
            except Exception as e:
                print(f"Error creating note {note_path}: {e}")
                raise

        clean_note: str = "\n".join(note[1::])
        full_path: Path = top_dir / note_path
        with open(full_path, "a+") as f:
            f.write(clean_note)


def scrub(matches: list[str]) -> list[list[str]]:
    return [match.strip().split("\n") for match in matches]
