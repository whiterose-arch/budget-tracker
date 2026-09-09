# Budget & Savings Tracker

A command-line Python application for tracking income, expenses, and savings goals.
Users can add, update, delete, and search transactions, view spending reports, and
track progress toward savings goals — all through a simple text menu.

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

## Project structure

```
.
├── main.py            # Menu and user flows (entry point)
├── data_store.py       # Load/save data as JSON
├── validation.py        # Safe input helpers (amounts, dates, menu choices, etc.)
├── processing.py        # Core transaction logic (find/update/delete/search)
├── reports.py            # Totals, category report, monthly summary, savings goals
└── data/
    └── budget_data.json  # Persisted transaction and savings goal data
```

## Requirements

- Python 3.x
- No external dependencies — uses only the Python standard library

## Getting started

1. Clone the repository:
   ```
   git clone https://github.com/whiterose-arch/budget-tracker.git
   cd budget-tracker
   ```
2. Run the application:
   ```
   python main.py
   ```
3. On first run, if `data/budget_data.json` doesn't exist yet, it will be created
   automatically to store your transactions and savings goals.

## Usage

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

## Team

| Name | Role / Module(s) | Github Handler |
|------|------------------|----------=-----|
| Emmanuel Adekojo | Data Processing |
| Emmanulle Ange Bineli | Reporting and Documentation |
| Eric Mugisha | Main Interface and Modules Connection |

