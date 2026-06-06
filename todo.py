#!/usr/bin/env python3
"""Simple CLI ToDo app.

Usage:
    python todo.py add <task description>
    python todo.py list
    python todo.py done <id>
    python todo.py remove <id>

Tasks are persisted to todos.json in the current working directory.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

DATA_FILE = Path("todos.json")


def load() -> dict:
    if not DATA_FILE.exists():
        return {"next_id": 1, "tasks": []}
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return {"next_id": 1, "tasks": []}
    data.setdefault("next_id", 1)
    data.setdefault("tasks", [])
    return data


def save(data: dict) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def cmd_add(args: argparse.Namespace) -> int:
    text = " ".join(args.task).strip()
    if not text:
        print("error: task description is required", file=sys.stderr)
        return 2
    data = load()
    task_id = data["next_id"]
    data["tasks"].append({"id": task_id, "text": text, "done": False})
    data["next_id"] = task_id + 1
    save(data)
    print(f"added #{task_id}: {text}")
    return 0


def cmd_list(_: argparse.Namespace) -> int:
    data = load()
    if not data["tasks"]:
        print("(no tasks)")
        return 0
    for t in data["tasks"]:
        mark = "x" if t["done"] else " "
        print(f"[{mark}] {t['id']:>3}  {t['text']}")
    return 0


def _find(tasks: list[dict], task_id: int) -> dict | None:
    for t in tasks:
        if t["id"] == task_id:
            return t
    return None


def cmd_done(args: argparse.Namespace) -> int:
    data = load()
    t = _find(data["tasks"], args.id)
    if t is None:
        print(f"error: no task with id {args.id}", file=sys.stderr)
        return 1
    if t["done"]:
        print(f"#{args.id} already done")
        return 0
    t["done"] = True
    save(data)
    print(f"done #{args.id}: {t['text']}")
    return 0


def cmd_remove(args: argparse.Namespace) -> int:
    data = load()
    t = _find(data["tasks"], args.id)
    if t is None:
        print(f"error: no task with id {args.id}", file=sys.stderr)
        return 1
    data["tasks"] = [x for x in data["tasks"] if x["id"] != args.id]
    save(data)
    print(f"removed #{args.id}: {t['text']}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="todo",
        description="Simple CLI ToDo app. Tasks persist to todos.json in the current directory.",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    p_add = sub.add_parser("add", help="add a new task")
    p_add.add_argument("task", nargs="+", help="task description")
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list", help="list all tasks")
    p_list.set_defaults(func=cmd_list)

    p_done = sub.add_parser("done", help="mark a task as done")
    p_done.add_argument("id", type=int, help="task id")
    p_done.set_defaults(func=cmd_done)

    p_rm = sub.add_parser("remove", help="remove a task")
    p_rm.add_argument("id", type=int, help="task id")
    p_rm.set_defaults(func=cmd_remove)

    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
