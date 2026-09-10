# Project: Personal Budget & Savings Goal Tracker

___

## 1. Problem Statement 
___
Just Imagine a student receiving his monthly stipend and wants to track fixed costs like rent, but lose track of frequent daily expenses leading to unexpected shortfalls at the end of the month. Managing personal finances effectively is a significant challenge for many individuals and students. Without clear visibility into income, recurring expenses, and spending habits, individuals often struggle to stick to a budget or save for future financial goals. The proposed solutions can be complex for some people, require continuous internet connectivity, or even charge subscription fees.
The Personal Budget & Savings Tracker is here to solve this problem by:
* Providing a simple command-line tool that allows users to record transactions offline.
* Analyzing spending patterns 
* Tracking  long-term savings goals locally.

___

## 2. GCGO & Mission Alignment
___
Our main challenge was to  design a robust input validation function using `try/except` blocks to handle unexpected user entries (like text input when a number is expected from the user) without crashing the program. We used backend systems foundations like; data abstraction, error handling, input validation, and unit testing to build the software.  Building this application provides practical experience in structuring modular Python code, managing state across functions, and implementing JSON file operations.
___
This project would assist users with their economic growth challenges by promoting personal financial literacy, budgeting discipline, and structured savings planning.

___

## 3. Functional Requirements
___
* **Add Record**: The system shall allow users to add new financial records (income or expense) with an auto-incremented ID, amount, category, date, and description.
* **View Records**: The system shall display all recorded transactions in a formatted list view.
* **Update Record**: The system shall allow users to update existing transaction details by providing a specific transaction ID.
* **Delete Record**: The system shall allow users to permanently delete a transaction record by specifying its transaction ID.
* **Search / Filter**: The system shall allow users to search transactions by keyword, date, or category.
* **Total Calculations**: The system shall calculate total income, total expenses, and remaining net balance across all recorded data.
* **Category Breakdown**: The system shall aggregate and report total expenses broken down by individual categories (e.g., Food, Transport, Rent).
* **Monthly Summary**: The system shall generate a summary for a specific year and month (`YYYY-MM`) showing total income, total expenses, and net savings.
* **Savings Goals Tracker**: The system shall allow users to define target savings goals, update an existing goal (name, target amount, and current amount), and compute their progress towards these targets as a percentage.
* **Data Persistence**: The system shall load data from a `data.json` file on startup and save changes automatically when records are modified.
* **Input Validation**: The system shall use `try/except` blocks to catch invalid inputs and missing/corrupted data files without crashing.

___

## 4. Data Storage Structure (`data.json`)
___
{
  "transactions": [
    {
      "id": 1,
      "type": "income",
      "amount": 1000.0,
      "category": "Salary",
      "date": "2026-08-01",
      "description": "Monthly stipend"
    },
    {
      "id": 2,
      "type": "expense",
      "amount": 200.0,
      "category": "Food",
      "date": "2026-08-05",
      "description": "Groceries"
    }
  ],
  "savings_goals": [
    {
      "name": "Emergency Fund",
      "target_amount": 2000.0,
      "current_amount": 500.0
    }
  ]
}
