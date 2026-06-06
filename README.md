# paperclip-poc

A proof-of-concept repository for testing **Paperclip** and its integration with GitHub.

## Purpose

This repo exists to validate that Paperclip can interact with GitHub end-to-end, including:

- Reading repository contents (files, branches, commits)
- Creating and updating files via the GitHub API
- Working with branches and pull requests
- Managing issues and comments

## Status

🧪 **Experimental** — this is a sandbox repository. Contents may be created, modified, or deleted at any time as part of integration testing. Do not depend on anything in here.

## Structure

| Path | Description |
|---|---|
| `README.md` | This file |
| `.gitignore` | Standard ignore rules |
| `AGENTS.md` | Engineering workflow for Paperclip agents |
| `todo.py` | Simple CLI ToDo app (see Usage below) |

More files may appear as integration scenarios are exercised.

## Usage — `todo.py`

A minimal command-line ToDo app. Tasks are persisted to `todos.json` in the current working directory.

```bash
python todo.py add "write the README"
python todo.py list
python todo.py done 1
python todo.py remove 1
```

Requires Python 3.9+. No external dependencies.

## Related

- Maintained by [@RafeAtharSaksoft](https://github.com/RafeAtharSaksoft)
- Part of the Paperclip GitHub integration testing effort

## License

No license — internal testing only.
