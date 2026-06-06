#!/usr/bin/env python3
"""Simple CLI ToDo app.

Usage:
  python todo.py add <task>     Add a new task
  python todo.py list           List all tasks
  python todo.py done <id>      Mark a task as done
  python todo.py remove <id>    Remove a task
  python todo.py --help         Show this message

Tasks are persisted to todos.json in the current working directory.
"""

import json
import sys
from pathlib import Path

DATA_FILE = Path("todos.json")


def load():
    if not DATA_FILE.exists():
        return {"next_id": 1, "tasks": []}
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def save(data):
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def cmd_add(args):
    if not args:
        print("error: add requires a task description")
        return 1
    text = " ".join(args)
    data = load()
    task = {"id": data["next_id"], "text": text, "done": False}
    data["tasks"].append(task)
    data["next_id"] += 1
    save(data)
    print(f"added #{task['id']}: {text}")
    return 0


def cmd_list(_args):
    data = load()
    if not data["tasks"]:
        print("no tasks")
        return 0
    for t in data["tasks"]:
        mark = "x" if t["done"] else " "
        print(f"[{mark}] {t['id']}: {t['text']}")
    return 0


def _find(data, tid):
    for t in data["tasks"]:
        if t["id"] == tid:
            return t
    return None


def cmd_done(args):
    if not args:
        print("error: done requires an id")
        return 1
    try:
        tid = int(args[0])
    except ValueError:
        print("error: id must be an integer")
        return 1
    data = load()
    task = _find(data, tid)
    if not task:
        print(f"error: no task with id {tid}")
        return 1
    task["done"] = True
    save(data)
    print(f"marked #{tid} done")
    return 0


def cmd_remove(args):
    if not args:
        print("error: remove requires an id")
        return 1
    try:
        tid = int(args[0])
    except ValueError:
        print("error: id must be an integer")
        return 1
    data = load()
    before = len(data["tasks"])
    data["tasks"] = [t for t in data["tasks"] if t["id"] != tid]
    if len(data["tasks"]) == before:
        print(f"error: no task with id {tid}")
        return 1
    save(data)
    print(f"removed #{tid}")
    return 0


COMMANDS = {
    "add": cmd_add,
    "list": cmd_list,
    "done": cmd_done,
    "remove": cmd_remove,
}


def main(argv):
    if not argv or argv[0] in ("-h", "--help", "help"):
        print(__doc__)
        return 0
    cmd, rest = argv[0], argv[1:]
    handler = COMMANDS.get(cmd)
    if not handler:
        print(f"unknown command: {cmd}")
        print(__doc__)
        return 1
    return handler(rest)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
