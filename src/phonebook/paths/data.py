from typing import dataclass_transform
from phonebook.paths.base import get_home_dir
from pathlib import Path


APP_NAME: str = "phonebook"


def get_data_dir() -> Path:
    """
    Return the application's data directory:
    ~/.local/share/phonebook

    Ensures the directory exists.
    """

    data_dir: Path = get_home_dir() / ".local" / "share" / APP_NAME 

    data_dir.mkdir(parents=True, exist_ok=True)

    return data_dir 
