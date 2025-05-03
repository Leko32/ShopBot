import json
from pathlib import Path

FILE_PATH = Path("buttons_status.json")


def load_buttons_status():
    if FILE_PATH.exists():
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    return {}


def save_buttons_status(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)


def set_button_status(button_id: str, status: bool):
    data = load_buttons_status()
    data[button_id] = status
    save_buttons_status(data)


def get_button_status(button_id: str) -> bool:
    return load_buttons_status().get(button_id, True)
