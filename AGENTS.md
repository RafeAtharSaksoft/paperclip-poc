# Project: paperclip-poc

We build and maintain this project. Code lives in this repo:
https://github.com/RafeAtharSaksoft/paperclip-poc
Local working directory: D:\GitRepos\paperclip-poc
Work is tracked in Jira project SCRUM at https://rathar.atlassian.net

## Tools available in your runtime
- GitHub: via git, the `gh` CLI, and the GitHub MCP server (github-paperclip).
- Jira: via the Atlassian MCP server. Our project key is SCRUM.
(Credentials/OAuth are provided by the runtime — never put tokens in code,
comments, commits, or PRs.)

## Standard delivery workflow (every coding ticket)
1. Read the linked Jira issue SCRUM-xxx for full context and acceptance criteria.
2. Work in this repo. Branch: feat/SCRUM-xxx-<short-slug> off <main|master>.
3. Implement, then run the test suite. Do not push failing code.
4. git add / commit (conventional commits) / push your branch.
5. Open a PR with `gh pr create`, putting the Jira key (SCRUM-xxx) in the title and body.
6. Move the Jira issue from "TO DO" -> "IN PROGRESS" when you start, and to
   "<IN REVIEW or DONE>" when the PR is open.
7. Comment on the Paperclip ticket with the PR link and a summary.

## Rules
- Never push to main directly. PRs only.
- Keep changes small and reviewable.
- If tests can't pass or scope is unclear, stop and ask — don't guess.
- QA must review before anything is marked done; the board approves shipping.