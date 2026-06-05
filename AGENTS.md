# Project: paperclip-poc

We build and maintain this project. Code lives in this repo:
https://github.com/RafeAtharSaksoft/paperclip-poc
Local working directory: D:\GitRepos\paperclip-poc
Default branch: main
Work is tracked in Jira project SCRUM at https://rathar.atlassian.net

## Tools available in your runtime
- GitHub: via git, the `gh` CLI, and the GitHub MCP server (github-paperclip).
- Jira: via the Atlassian MCP server (atlassian). Our project key is SCRUM.
(Credentials/OAuth are provided by the runtime — never put tokens in code,
comments, commits, or PRs.)

## Jira workflow (exact status names)
TO DO -> IN PROGRESS -> IN REVIEW -> DONE

## Standard delivery workflow (every coding ticket)
1. Read the linked Jira issue SCRUM-xxx for full context and acceptance
   criteria.
2. Work in this repo. Create a branch off main: feat/SCRUM-xxx-<short-slug>.
3. Move the Jira issue from "TO DO" to "IN PROGRESS" when you start.
4. Implement, then run the test suite. Do not push failing code.
5. git add / commit (conventional commits, e.g. "feat: ...") / push your branch.
6. Open a PR with `gh pr create`, putting the Jira key (SCRUM-xxx) in the title
   and body.
7. Move the Jira issue to "IN REVIEW".
8. Comment on the Paperclip ticket with the PR link and a short summary.
9. After QA approves and the board signs off, the PR is merged and the Jira
   issue is moved to "DONE".

## Rules
- Never push to main directly. PRs only.
- Keep changes small and reviewable.
- If tests can't pass or scope is unclear, stop and ask — don't guess.
- QA must review before anything is marked DONE; the board approves shipping.