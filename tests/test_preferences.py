from src.core.preferences import UserPreferences
from pathlib import Path
import json


def test_load_save_cycle(tmp_path: Path):
    p = tmp_path / "prefs.json"
    prefs = UserPreferences(path=p)
    prefs.update(theme="dark", font_size=14, default_drink="latte")
    prefs.save()

    # simulate new session
    loaded = UserPreferences(path=p)
    loaded.load()
    assert loaded.data["theme"] == "dark"
    assert loaded.data["font_size"] == 14
    assert loaded.data["default_drink"] == "latte"

def test_missing_file_uses_defaults(tmp_path: Path):
    p = tmp_path / "nope.json"
    prefs = UserPreferences(path=p)
    prefs.load()
    assert prefs.data["theme"] == "light"
