"""
Budget & Savings Tracker — menu and user flows.

Calls the other modules for the actual work:
  data_store.py  — load/save JSON
  validation.py  — safe input helpers
  processing.py  — find / update / delete / search
  reports.py     — totals, category report, monthly summary, goals

Try not to change this file while issues #1–#4 are in progress.
If something here needs a fix so your function works, note it in the PR.

Assigned to: whole team (integration = whoever takes issue #5)
"""

import data_store
import validation
import processing
import reports

DATA_FILE = "data/budget_data.json"


def add_transaction_flow(data):
    print("\n-- Add transaction --")
    t_type = validation.get_valid_menu_choice(
        "Type (1=Income, 2=Expense): ", ["1", "2"]
    )
    t_type = "income" if t_type == "1" else "expense"
    amount = validation.get_valid_amount("Amount: ")
    category = validation.get_non_empty_text("Category: ")
    date = validation.get_valid_date("Date (YYYY-MM-DD): ")
    description = input("Description (optional): ").strip()

    new_id = processing.generate_next_id(data["transactions"])
    transaction = {
        "id": new_id,
        "type": t_type,
        "amount": amount,
        "category": category,
        "date": date,
        "description": description,
    }
    data["transactions"].append(transaction)
    data_store.save_data(DATA_FILE, data)
    print(f"Added transaction #{new_id}.")


def view_transactions_flow(data):
    print("\n-- All transactions --")
    if not data["transactions"]:
        print("No transactions yet.")
        return
    for t in data["transactions"]:
        print(
            f"#{t['id']} | {t['type']:7} | {t['amount']:>10.2f} | "
            f"{t['category']:12} | {t['date']} | {t.get('description', '')}"
        )


def update_transaction_flow(data):
    print("\n-- Update transaction --")
    t_id = validation.get_valid_amount("Transaction ID to update: ")
    transaction = processing.find_transaction_by_id(data["transactions"], int(t_id))
    if transaction is None:
        print("No transaction with that ID.")
        return

    print("Leave a field blank to keep its current value.")
    new_amount = input(f"Amount [{transaction['amount']}]: ").strip()
    new_category = input(f"Category [{transaction['category']}]: ").strip()
    new_date = input(f"Date [{transaction['date']}]: ").strip()

    updates = {}
    if new_amount:
        updates["amount"] = float(new_amount)
    if new_category:
        updates["category"] = new_category
    if new_date:
        while new_date and not validation.is_valid_date(new_date):
            new_date = input(
                f"Date [{transaction['date']}] (YYYY-MM-DD, blank to keep): "
            ).strip()
        if new_date:
            updates["date"] = new_date

    success = processing.update_transaction(data["transactions"], int(t_id), updates)
    if success:
        data_store.save_data(DATA_FILE, data)
        print("Transaction updated.")
    else:
        print("Update failed.")


def delete_transaction_flow(data):
    print("\n-- Delete transaction --")
    t_id = validation.get_valid_amount("Transaction ID to delete: ")
    confirm = validation.get_yes_no(f"Delete transaction #{int(t_id)}? (y/n): ")
    if not confirm:
        print("Cancelled.")
        return
    success = processing.delete_transaction(data["transactions"], int(t_id))
    if success:
        data_store.save_data(DATA_FILE, data)
        print("Transaction deleted.")
    else:
        print("No transaction with that ID.")


def search_transactions_flow(data):
    print("\n-- Search / filter --")
    mode = validation.get_valid_menu_choice(
        "1=Search by keyword, 2=Filter by category: ", ["1", "2"]
    )
    if mode == "1":
        keyword = validation.get_non_empty_text("Keyword: ")
        results = processing.search_transactions(data["transactions"], keyword)
    else:
        category = validation.get_non_empty_text("Category: ")
        results = processing.filter_by_category(data["transactions"], category)

    if not results:
        print("No matching transactions.")
        return
    for t in results:
        print(f"#{t['id']} | {t['type']:7} | {t['amount']:>10.2f} | {t['category']:12} | {t['date']}")


def show_totals_flow(data):
    print("\n-- Totals --")
    totals = reports.calculate_totals(data["transactions"])
    print(f"Total income:   {totals['income']:.2f}")
    print(f"Total expenses: {totals['expenses']:.2f}")
    print(f"Balance:        {totals['balance']:.2f}")


def show_category_report_flow(data):
    print("\n-- Spending by category --")
    breakdown = reports.calculate_by_category(data["transactions"])
    if not breakdown:
        print("No expense data yet.")
        return
    for category, total in breakdown.items():
        print(f"{category:15}: {total:.2f}")


def show_monthly_summary_flow(data):
    print("\n-- Monthly summary --")
    year = validation.get_non_empty_text("Year (e.g. 2026): ")
    month = validation.get_non_empty_text("Month (e.g. 09): ")
    summary = reports.generate_monthly_summary(data["transactions"], year, month)
    print(f"Income:   {summary['income']:.2f}")
    print(f"Expenses: {summary['expenses']:.2f}")
    print(f"Net:      {summary['net']:.2f}")


def manage_savings_goals_flow(data):
    print("\n-- Savings goals --")
    print("1. Add a goal")
    print("2. View goal progress")
    choice = validation.get_valid_menu_choice("Choice: ", ["1", "2"])
    if choice == "1":
        name = validation.get_non_empty_text("Goal name: ")
        target = validation.get_valid_amount("Target amount: ")
        reports.add_savings_goal(data["savings_goals"], name, target)
        data_store.save_data(DATA_FILE, data)
        print("Goal added.")
    else:
        if not data["savings_goals"]:
            print("No savings goals yet.")
            return
        for goal in data["savings_goals"]:
            progress = reports.calculate_savings_progress(goal)
            print(f"{goal['name']}: {progress:.1f}% of {goal['target_amount']:.2f}")


def print_menu():
    print("\n===== BUDGET & SAVINGS TRACKER =====")
    print("1. Add transaction")
    print("2. View transactions")
    print("3. Update transaction")
    print("4. Delete transaction")
    print("5. Search / filter transactions")
    print("6. Show totals (income/expenses/balance)")
    print("7. Show spending by category")
    print("8. Manage savings goals")
    print("9. Show monthly summary")
    print("10. Exit")


def main():
    data = data_store.load_data(DATA_FILE)

    actions = {
        "1": add_transaction_flow,
        "2": view_transactions_flow,
        "3": update_transaction_flow,
        "4": delete_transaction_flow,
        "5": search_transactions_flow,
        "6": show_totals_flow,
        "7": show_category_report_flow,
        "8": manage_savings_goals_flow,
        "9": show_monthly_summary_flow,
    }

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "10":
            print("Goodbye!")
            break
        elif choice in actions:
            try:
                actions[choice](data)
            except Exception as error:
                # Keep the menu running if one feature breaks
                print(f"Something went wrong: {error}")
        else:
            print("That's not a valid option, try again.")


if __name__ == "__main__":
    main()
