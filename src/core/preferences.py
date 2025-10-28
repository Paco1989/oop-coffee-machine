# preferences.py
from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict

class UserPreferences:
    def __init__(self, path: Path | None = None) -> None:
        self.path = path or Path.home() / ".coffee_prefs.json"
        self.data: Dict[str, Any] = {
            "theme": "light",
            "font_size": 12,
            "default_drink": "espresso"
        }

    def load(self) -> None:
        try:
            if self.path.exists():
                self.data.update(json.loads(self.path.read_text(encoding="utf-8")))
        except Exception:
            # fail safe: keep defaults
            pass

    def save(self) -> None:
        try:
            self.path.write_text(json.dumps(self.data, indent=2), encoding="utf-8")
        except Exception:
            # non-fatal for UI; optionally log
            pass

    def update(self, **kwargs: Any) -> None:
        self.data.update({k: v for k, v in kwargs.items() if k in self.data})
