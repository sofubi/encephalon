from dataclasses import dataclass
from pathlib import Path
from tomllib import TOMLDecodeError, load
from typing import Any, TypeAlias

DEFAULT_CONFIG: str = "notes_location = '~/.encephalon'"

CONF_DIR: Path = Path("~/.config/encephalon").expanduser()
CONF_PATH: Path = CONF_DIR / "config.toml"


ConfigDict: TypeAlias = dict[str, Any]


@dataclass
class Config:
    notes_location: str

    def __init__(self) -> None:
        self.config: ConfigDict = Config.init()
        self.notes_location: str = self.config["notes_location"]

    @staticmethod
    def read() -> ConfigDict:
        try:
            with open(CONF_PATH, "rb") as f:
                return load(f)
        except TOMLDecodeError as e:
            print(f"Unable to read config file {CONF_PATH}: {e}")
            raise
        except Exception as e:
            print(f"Error while reading config file {CONF_PATH}: {e}")
            raise

    @staticmethod
    def init() -> ConfigDict:
        if not CONF_DIR.exists() or not CONF_PATH.exists():
            try:
                CONF_DIR.mkdir(exist_ok=True)
                with open(CONF_PATH, "x") as f:
                    f.write(DEFAULT_CONFIG)

            except Exception as e:
                print(f"Issue initializing config {CONF_PATH}: {e}")
                raise

        return Config.read()
