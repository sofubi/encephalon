from pathlib import Path
from re import compile, Pattern
from sys import argv

prog: Pattern[str] = compile(r"@note@([\s\S]*?)@end@")


# TODO: Flesh out
# [ ] Error handling
# [ ] Flexibility for long lists
def read(file: str) -> list[str]:
    file = Path(file).expanduser()
    with open(file, "r") as f:
        return prog.findall(f.read())


def run() -> None:
    result: list[str] = read(argv[1])
    print(len(result))
    print(result)


# TODO: Reasonable CLI interface
# [ ] Create basics with argparse
# [ ] Consider potential needs
if __name__ == "__main__":
    read(argv[1])
