"""
Totals, category breakdown, monthly summary, and savings goals.
Calculation only — no file I/O and no printing here.

Assigned to: Ange Emmanuelle Ntsa Bineli
"""


def calculate_totals(transactions):
    """
    Sum income, expenses, and balance.

    Args:
        transactions (list[dict]): each has "type" ("income"|"expense") and "amount" (float)

    Returns:
        dict: {"income": float, "expenses": float, "balance": float}
              where balance = income - expenses
    """
    income = sum(t["amount"] for t in transactions if t.get("type") == "income")
    expenses = sum(t["amount"] for t in transactions if t.get("type") == "expense")
    return {
        "income": float(income),
        "expenses": float(expenses),
        "balance": float(income - expenses),
    }



def calculate_by_category(transactions):
    """
    Total spending per category (expenses only).

    Args:
        transactions (list[dict]): each has "type", "category" (str), "amount" (float)

    Returns:
        dict[str, float]: {category: total_expense_amount}
    """
    
    categories = {}
    for t in transactions:
        if t.get("type") == "expense":
            cat = t.get("category")
            categories[cat] = categories.get(cat, 0.0) + t.get("amount", 0.0)
    return categories


def generate_monthly_summary(transactions, year, month):
    """
    Income / expenses / net for one month.

    Args:
        transactions (list[dict]): each has "date" as "YYYY-MM-DD", plus type/amount
        year (str|int): e.g. "2026" or 2026
        month (str|int): e.g. "09" or 9 — decide how you handle both forms

    Returns:
        dict: {"income": float, "expenses": float, "net": float}
              where net = income - expenses
    """
    
    target_prefix = f"{int(year):04d}-{int(month):02d}"

    income = 0.0
    expenses = 0.0

    for t in transactions:
        if t.get("date", "").startswith(target_prefix):
            if t.get("type") == "income":
                income += t.get("amount", 0.0)
            elif t.get("type") == "expense":
                expenses += t.get("amount", 0.0)

    return {
        "income": income,
       "expenses": expenses,
        "net": income - expenses,
    }       



def add_savings_goal(savings_goals, name, target_amount):
    """
    Append a new savings goal.

    Args:
        savings_goals (list[dict]): list to append to
        name (str): goal name
        target_amount (float): must be > 0

    Returns:
        dict: the new goal
              {"name": str, "target_amount": float, "current_amount": 0}
    """
    
    goal = {
        "name": name,
         "target_amount": float(target_amount),
        "current_amount": 0,
    }
    savings_goals.append(goal)
    return goal



def calculate_savings_progress(goal):
    """
    Progress toward a savings goal as a percentage.

    Args:
        goal (dict): has "current_amount" (float) and "target_amount" (float)

    Returns:
        float: percentage (0–100). If target_amount is 0, return 0 (no divide-by-zero).
    """

    target = goal.get("target_amount", 0.0)
    current = goal.get("current_amount", 0.0)

    if target <= 0:
        return 0.0

    return (current / target) * 100.0



def _check(name, condition, detail=""):
    if condition:
        print(f"  PASS  {name}")
        return True
    extra = f" — {detail}" if detail else ""
    print(f"  FAIL  {name}{extra}")
    return False


if __name__ == "__main__":
    # Run: python3 reports.py
    print("Self-check: reports.py")
    ok = True

    sample = [
        {
            "id": 1,
            "type": "income",
            "amount": 1000.0,
            "category": "Salary",
            "date": "2026-08-01",
            "description": "",
        },
        {
            "id": 2,
            "type": "expense",
            "amount": 200.0,
            "category": "Food",
            "date": "2026-08-05",
            "description": "",
        },
        {
            "id": 3,
            "type": "expense",
            "amount": 50.0,
            "category": "Food",
            "date": "2026-08-10",
            "description": "",
        },
        {
            "id": 4,
            "type": "expense",
            "amount": 80.0,
            "category": "Transport",
            "date": "2026-09-02",
            "description": "",
        },
        {
            "id": 5,
            "type": "income",
            "amount": 100.0,
            "category": "Gift",
            "date": "2026-09-15",
            "description": "",
        },
    ]

    totals = calculate_totals(sample)
    ok &= _check(
        "calculate_totals",
        isinstance(totals, dict)
        and totals.get("income") == 1100.0
        and totals.get("expenses") == 330.0
        and totals.get("balance") == 770.0,
        f"got {totals!r}",
    )
    empty_totals = calculate_totals([])
    ok &= _check(
        "calculate_totals empty",
        isinstance(empty_totals, dict)
        and float(empty_totals.get("income", -1)) == 0.0
        and float(empty_totals.get("expenses", -1)) == 0.0
        and float(empty_totals.get("balance", -1)) == 0.0,
        f"got {empty_totals!r}",
    )

    by_cat = calculate_by_category(sample)
    ok &= _check(
        "calculate_by_category expenses only + sums",
        isinstance(by_cat, dict)
        and by_cat.get("Food") == 250.0
        and by_cat.get("Transport") == 80.0
        and "Salary" not in by_cat,
        f"got {by_cat!r}",
    )

    august = generate_monthly_summary(sample, "2026", "08")
    ok &= _check(
        "generate_monthly_summary August",
        isinstance(august, dict)
        and august.get("income") == 1000.0
        and august.get("expenses") == 250.0
        and august.get("net") == 750.0,
        f"got {august!r}",
    )
    sept = generate_monthly_summary(sample, 2026, 9)
    ok &= _check(
        "generate_monthly_summary September (month as int 9)",
        isinstance(sept, dict)
        and sept.get("income") == 100.0
        and sept.get("expenses") == 80.0
        and sept.get("net") == 20.0,
        f"got {sept!r}",
    )

    goals = []
    goal = add_savings_goal(goals, "Emergency", 2000.0)
    ok &= _check(
        "add_savings_goal shape + append",
        isinstance(goal, dict)
        and goal.get("name") == "Emergency"
        and goal.get("target_amount") == 2000.0
        and goal.get("current_amount") == 0
        and goals == [goal],
        f"got goal={goal!r} goals={goals!r}",
    )

    progress = calculate_savings_progress(
        {"name": "Emergency", "target_amount": 2000.0, "current_amount": 500.0}
    )
    ok &= _check(
        "calculate_savings_progress 500/2000 → 25%",
        progress == 25 or progress == 25.0,
        f"got {progress!r}",
    )
    zero_target = calculate_savings_progress(
        {"name": "x", "target_amount": 0, "current_amount": 10}
    )
    ok &= _check(
        "calculate_savings_progress target 0 → 0",
        zero_target == 0 or zero_target == 0.0,
        f"got {zero_target!r}",
    )

    print("All good." if ok else "Some checks failed — fix before opening a PR.")
