# paperclip-poc

A proof-of-concept repository for testing **Paperclip** and its integration with GitHub. Includes a simple Python CLI ToDo app as the primary deliverable.

## Todo CLI

A tiny stdlib-only CLI to manage a personal task list. Tasks are persisted to `todos.json` in the current working directory.

### Requirements

- Python 3.8+

No third-party dependencies.

### Usage

```
python todo.py add <task>     # add a new task
python todo.py list           # list all tasks
python todo.py done <id>      # mark a task as done
python todo.py remove <id>    # remove a task
python todo.py --help         # show help
```

### Examples

```
$ python todo.py add "Write docs"
added #1: Write docs

$ python todo.py add "Ship release"
added #2: Ship release

$ python todo.py list
[ ] 1: Write docs
[ ] 2: Ship release

$ python todo.py done 1
marked #1 done

$ python todo.py list
[x] 1: Write docs
[ ] 2: Ship release

$ python todo.py remove 2
removed #2
```

### Storage

Tasks live in `todos.json` next to wherever you run the command. Move or delete the file to start fresh.

## Structure

| Path | Description |
|---|---|
| `README.md` | This file |
| `todo.py` | Python CLI ToDo app |
| `AGENTS.md` | Agent workflow rules |
| `.gitignore` | Standard ignore rules |

## Related

- Maintained by [@RafeAtharSaksoft](https://github.com/RafeAtharSaksoft)
- Part of the Paperclip GitHub integration testing effort

## License

No license — internal testing only.
