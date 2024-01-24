from argparse import ArgumentParser, Namespace
from pathlib import Path

from encephalon.parsing import fetch_parse


def hook():
    parser = ArgumentParser()
    parser.add_argument("path")
    args: Namespace = parser.parse_args()

    target = Path(args.path)

    if not target.exists():
        print("The target path does not exist")
        raise SystemExit(1)

    fetch_parse(target)
