# Personal Budget & Savings Goal Tracker

A command-line Python application for tracking income, expenses, and savings goals.
Users can add, update, delete, and search transactions, view spending reports, and
track progress toward savings goals — all through a simple text menu.

Formative assessment — Introduction to Programming and Databases.
We chose the **Personal Budget & Savings Goal Tracker** scenario from the brief.

For a quick overview of what the app needs (CRUD, search, reports, JSON, etc.),
see `Formative Walkthrought.txt`. The full brief is in `Formative.pdf`.

## Team

| Name                   | Role / Module(s)                        | GitHub handle       |
| ---------------------- | ---------------------------------------- | -------------------- |
| Emmanuel Adekojo        | Data Processing                          | @whiterose-arch       |
| Emmanulle Ange Bineli   | Reporting and Documentation              | @binelintsa-sketch    |
| Eric Mugisha            | Main Interface and Modules Connection    | @mugisha-eric         |

## Features

- **Add transactions** — record income or expenses with amount, category, date, and an optional description
- **View transactions** — list every recorded transaction
- **Update transactions** — edit the amount, category, or date of an existing transaction by ID
- **Delete transactions** — remove a transaction by ID (with confirmation)
- **Search / filter** — find transactions by keyword or filter by category
- **Totals** — see total income, total expenses, and current balance
- **Spending by category** — breakdown of expenses grouped by category
- **Monthly summary** — income, expenses, and net total for a given month/year
- **Savings goals** — create goals with a target amount and track progress toward them
- Data saved in `data/budget_data.json` between runs (local only; see sample file below)

## Project layout

```
budget-tracker/
├── main.py                 # menu loop
├── validation.py           # input checks
├── data_store.py           # load/save JSON
├── processing.py           # search / filter / update / delete
├── reports.py               # totals, category report, monthly summary, goals
├── data/
│   └── budget_data.sample.json   # starter data (committed)
├── AI_DISCLOSURE.md
├── Formative Walkthrought.txt
├── Formative.pdf
└── README.md
```

## Requirements

- Python 3.x
- No external dependencies — uses only the standard library (`json`, `os`)

## How to run

1. Clone the repository:
   ```bash
   git clone https://github.com/whiterose-arch/budget-tracker.git
   cd budget-tracker
   ```
2. (Optional) start with the sample data — otherwise the app starts empty:
   ```bash
   cp data/budget_data.sample.json data/budget_data.json
   ```
3. Run the application:
   ```bash
   python3 main.py
   ```

`data/budget_data.json` is what the app reads/writes while you test. If `data/budget_data.json` doesn't exist when the app starts, it will be created automatically to store your transactions and savings goals or run command: 
```bash
   cp data/budget_data.sample.json data/budget_data.json
```
to fill sample data.

## Usage
```bash
   python3 main.py
```

Running `main.py` launches an interactive menu:

```
===== BUDGET & SAVINGS TRACKER =====
1. Add transaction
2. View transactions
3. Update transaction
4. Delete transaction
5. Search / filter transactions
6. Show totals (income/expenses/balance)
7. Show spending by category
8. Manage savings goals
9. Show monthly summary
10. Exit
```

Enter the number corresponding to the action you want, then follow the prompts.
Errors in any single feature are caught so the program keeps running rather than
crashing — you'll just see a "Something went wrong" message and return to the menu.

## Data format

Transactions are stored as JSON objects with the following fields:

| Field         | Type   | Description                                  |
|---------------|--------|-----------------------------------------------|
| `id`          | int    | Unique transaction ID                         |
| `type`        | string | `"income"` or `"expense"`                     |
| `amount`      | float  | Transaction amount                            |
| `category`    | string | Category label (e.g. "Groceries", "Salary")   |
| `date`        | string | Date in `YYYY-MM-DD` format                   |
| `description` | string | Optional free-text description                |

Savings goals are stored with a name, target amount, and progress data used by
`reports.calculate_savings_progress`.


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
