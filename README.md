# Personal Budget & Savings Goal Tracker

Menu-driven Python CLI for tracking income, expenses, and savings goals.

Formative assessment — Introduction to Programming and Databases.
We chose the **Personal Budget & Savings Goal Tracker** scenario from the brief.

For a quick overview of what the app needs (CRUD, search, reports, JSON, etc.),
see `Formative Walkthrought.txt`. The full brief is in `Formative.pdf`.

## Team

| Name       | GitHub handle |
| ---------- | ------------- |
| Member 1   | @your-handle  |
| Member 2   | @your-handle  |
| Member 3   | @your-handle  |

## Project layout

```
budget-tracker/
├── main.py                 # menu loop
├── validation.py           # input checks
├── data_store.py           # load/save JSON
├── processing.py           # search / filter / update / delete
├── reports.py              # totals, category report, monthly summary, goals
├── data/
│   └── budget_data.sample.json   # starter data (committed)
├── AI_DISCLOSURE.md
├── Formative Walkthrought.txt
├── Formative.pdf
└── README.md
```

Each of `validation.py`, `data_store.py`, `processing.py`, and `reports.py`
has empty functions (`# TODO`) for someone to fill in. `main.py` already
calls them, so once a file is done that part of the menu should work.

Before opening a PR, run your file on its own — each one has a small
self-check at the bottom (`if __name__ == "__main__"`):

```bash
python3 data_store.py
python3 validation.py
python3 processing.py
python3 reports.py
```

You want `PASS` lines and `All good.` at the end. No extra libraries needed.

## How to run

```bash
# optional: start with the sample data (otherwise the app starts empty)
cp data/budget_data.sample.json data/budget_data.json

python3 main.py
```

Needs Python 3 only (standard library: `json`, `os`). No extra packages.

`data/budget_data.json` is what the app reads/writes while you test. It’s in
`.gitignore` so random test data doesn’t show up in PRs. Edit/share starter
data via `data/budget_data.sample.json` instead.

## Features (what we're building)

- Add / view / update / delete transactions
- Search or filter transactions
- Totals (income, expenses, balance)
- Spending by category
- Monthly summary
- Savings goals and progress %
- Data saved in `data/budget_data.json` between runs (local only; see sample file above)

## Team workflow

We split work by file so we don't step on each other. One GitHub issue per
file (see the Issues tab once the repo is on GitHub).

1. Pick an open issue and assign yourself.
2. Branch off `main`: `<your-github-handle>/issue-<number>-<short-name>`
   e.g. `alex/issue-2-validation`
3. Only change the file(s) listed on that issue.
4. Open a PR. First line of the description: `Closes #<issue-number>`
5. Someone else reviews before merge — don't merge your own PR.
6. Don't push straight to `main`.

### Commit messages (required)

Use this format so history stays readable:

```
type: short summary of what changed
```

Allowed `type` values:

| type | when to use |
| ---- | ----------- |
| `feat` | new behaviour / implementing a function |
| `fix` | bug fix |
| `docs` | README, issues, disclosure, requirements note |
| `chore` | .gitignore, sample data, small cleanup |
| `test` | self-check / testing tweaks |

Examples:

```
feat: implement load_data and save_data
fix: reject zero amounts in get_valid_amount
docs: fill in team names in README
chore: expand sample budget data
```

Optional: mention the issue — `feat: implement validation helpers (#2)`.

Keep the summary short (about one line). Don’t paste huge explanations into the commit title.

`data_store`, `validation`, `processing`, and `reports` can be done at the
same time. After those are in, we do a full run-through and fix anything
that breaks when the pieces meet.

## Sources & AI disclosure

We used ChatGPT to help with project setup and wording:

- Structure and wording of this `README.md` (layout, how to run, team workflow)
- Drafting other markdown helpers (`AI_DISCLOSURE.md` and related notes)
- Small **self-check blocks** at the bottom of `data_store.py`,
  `validation.py`, `processing.py`, and `reports.py`
  (`if __name__ == "__main__"`) so each person can run their file and see
  PASS/FAIL before opening a PR

Those self-checks are not part of the app menu.

The actual function bodies (the `# TODO` logic for load/save, validation,
processing, and reports) are written by the team member who owns that file.

**Reference (APA 7th):** OpenAI. (2026). *ChatGPT* [Large language model].
https://chatgpt.com

Same note is also in [`AI_DISCLOSURE.md`](AI_DISCLOSURE.md).

## Other deliverables

Still to write as a team:

- Short requirements note (problem, GCGO link, features, data fields)
- Demo walkthrough video

These are listed in `Formative.pdf` under Required Deliverables.
