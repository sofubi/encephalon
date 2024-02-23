import sys
from argparse import ArgumentParser, Namespace
from pathlib import Path

from encephalon.config import Config
from encephalon.parsing import fetch_path, parse_notes
from encephalon.storage.archive import archive, scrub


def hook():
    parser = ArgumentParser()
    parser.add_argument("path")
    args: Namespace = parser.parse_args()

    target = Path(args.path)

    if not target.exists():
        print("The target path does not exist")
        raise sys.exit(1)

    config: Config = Config()

    # FIXME: Should be handled outside of hook
    real_path: Path = fetch_path(target)
    notes = parse_notes(real_path)
    clean_notes = scrub(notes)
    archive(clean_notes, config)
