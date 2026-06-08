#!/usr/bin/env python3
"""Shared JSON persistence for the todo app.

Both the CLI (todo.py) and the web UI (webapp.py) import load/save from here
so that todos.json is always the single source of truth.
"""
from __future__ import annotations

import json
from pathlib import Path

DATA_FILE = Path("todos.json")


def load() -> dict:
    if not DATA_FILE.exists():
        return {"next_id": 1, "tasks": []}
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def save(data: dict) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
