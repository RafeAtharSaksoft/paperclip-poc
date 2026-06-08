#!/usr/bin/env python3
"""Flask web UI for the todo app.

Shares todos.json with the existing CLI (todo.py) via todo_store.py.

Usage:
    python webapp.py          (runs on http://localhost:5000)
    flask --app webapp run    (alternative)
"""
from __future__ import annotations

from flask import Flask, redirect, render_template, request, url_for

from todo_store import load, save

app = Flask(__name__)


@app.route("/")
def index():
    data = load()
    return render_template("index.html", tasks=data["tasks"])


@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("text", "").strip()
    if text:
        data = load()
        task_id = data["next_id"]
        data["tasks"].append({"id": task_id, "text": text, "done": False})
        data["next_id"] = task_id + 1
        save(data)
    return redirect(url_for("index"))


@app.route("/done/<int:task_id>", methods=["POST"])
def done(task_id: int):
    data = load()
    for t in data["tasks"]:
        if t["id"] == task_id:
            t["done"] = True
            break
    save(data)
    return redirect(url_for("index"))


@app.route("/remove/<int:task_id>", methods=["POST"])
def remove(task_id: int):
    data = load()
    data["tasks"] = [t for t in data["tasks"] if t["id"] != task_id]
    save(data)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
