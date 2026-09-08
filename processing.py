"""
Find, search, filter, update, and delete transactions.
Works on the in-memory list only — no file I/O and no printing here.

Assigned to:
"""


def generate_next_id(transactions):
    """
    Return the next unused transaction id.

    Args:
        transactions (list[dict]): list of transaction dicts (each has "id": int)

    Returns:
        int: 1 if the list is empty, otherwise highest id + 1
    """

    if len(transactions) == 0:
        return 1

    sorted_transaction = sorted(transactions, key=lambda transaction: transaction["id"])

    last_transaction = sorted_transaction[-1]
    last_transaction_id = last_transaction["id"]

    return int(last_transaction_id) + 1


def find_transaction_by_id(transactions, transaction_id):
    """
    Find one transaction by id.

    Args:
        transactions (list[dict]): list of transaction dicts
        transaction_id (int): id to look for

    Returns:
        dict | None: the matching transaction, or None if not found
    """
    
    selected_transaction = list(filter(lambda transaction: transaction["id"] == transaction_id, transactions))

    if len(selected_transaction) == 0:
        return

    return selected_transaction[0]



def update_transaction(transactions, transaction_id, updates):
    """
    Update fields on an existing transaction.

    Args:
        transactions (list[dict]): list of transaction dicts
        transaction_id (int): id to update
        updates (dict): fields to change, e.g. {"amount": 50.0, "category": "Food"}

    Returns:
        bool: True if found and updated, False if id was not found
    """

    selected_transaction = list(filter(lambda transaction: transaction["id"] == transaction_id, transactions))

    if len(selected_transaction) == 0:
        return False

    keys = list(updates.keys())

    for key in keys:
        for transaction in transactions:
            if transaction["id"] == transaction_id:
                transaction[key] = updates[key]

    return True

def delete_transaction(transactions: list[dict], transaction_id):
    """
    Remove a transaction from the list (in place).

    Args:
        transactions (list[dict]): list of transaction dicts
        transaction_id (int): id to remove

    Returns:
        bool: True if something was removed, False if id was not found
    """

    selected_transaction = list(filter(lambda transaction: transaction["id"] == transaction_id, transactions))

    if len(selected_transaction) == 0:
        return False

    transaction = selected_transaction[0]
    try:
        transactions.remove(transaction)
    except:
        return False

    return True


def search_transactions(transactions, keyword):
    """
    Search transactions by keyword in category or description.

    Args:
        transactions (list[dict]): list of transaction dicts
        keyword (str): text to search for (case-insensitive, partial match ok)

    Returns:
        list[dict]: matching transactions (empty list if none)
    """
    
    filtered_transaction = list(filter(lambda transaction: keyword.lower() in transaction["description"].lower() or keyword in transaction["category"].lower(), transactions))

    return filtered_transaction


def filter_by_category(transactions, category):
    """
    Filter transactions by category.

    Args:
        transactions (list[dict]): list of transaction dicts
        category (str): category to match (case-insensitive)

    Returns:
        list[dict]: matching transactions (empty list if none)
    """
    filtered_transaction = list(filter(lambda transaction: category.lower() == transaction["category"].lower(), transactions))

    return filtered_transaction


def _check(name, condition, detail=""):
    if condition:
        print(f"  PASS  {name}")
        return True
    extra = f" — {detail}" if detail else ""
    print(f"  FAIL  {name}{extra}")
    return False


if __name__ == "__main__":
    # Run: python3 processing.py
    print("Self-check: processing.py")
    ok = True

    sample = [
        {
            "id": 1,
            "type": "expense",
            "amount": 50.0,
            "category": "Food",
            "date": "2026-08-01",
            "description": "Lunch",
        },
        {
            "id": 3,
            "type": "expense",
            "amount": 20.0,
            "category": "Transport",
            "date": "2026-08-02",
            "description": "Bus",
        },
        {
            "id": 2,
            "type": "income",
            "amount": 100.0,
            "category": "Salary",
            "date": "2026-08-03",
            "description": "",
        },
    ]

    ok &= _check("generate_next_id empty → 1", generate_next_id([]) == 1)
    ok &= _check(
        "generate_next_id uses max id (not list length)",
        generate_next_id(sample) == 4,
        f"got {generate_next_id(sample)!r}",
    )

    found = find_transaction_by_id(sample, 2)
    ok &= _check(
        "find_transaction_by_id finds id 2",
        isinstance(found, dict) and found.get("category") == "Salary",
        f"got {found!r}",
    )
    ok &= _check(
        "find_transaction_by_id missing → None",
        find_transaction_by_id(sample, 99) is None,
    )

    txs = [dict(t) for t in sample]
    updated = update_transaction(txs, 1, {"amount": 75.0, "category": "Groceries"})
    t1 = find_transaction_by_id(txs, 1)
    ok &= _check("update_transaction returns True", updated is True)
    ok &= _check(
        "update_transaction changes fields",
        isinstance(t1, dict) and t1.get("amount") == 75.0 and t1.get("category") == "Groceries",
        f"got {t1!r}",
    )
    ok &= _check(
        "update_transaction missing id → False",
        update_transaction(txs, 99, {"amount": 1.0}) is False,
    )

    txs2 = [dict(t) for t in sample]
    deleted = delete_transaction(txs2, 3)
    ok &= _check("delete_transaction returns True", deleted is True)
    ok &= _check(
        "delete_transaction removes only that id",
        len(txs2) == 2 and find_transaction_by_id(txs2, 3) is None,
        f"remaining={[t.get('id') for t in txs2 if isinstance(t, dict)]}",
    )
    ok &= _check(
        "delete_transaction missing id → False",
        delete_transaction(txs2, 99) is False,
    )

    hits = search_transactions(sample, "lun")
    ok &= _check(
        "search_transactions partial + case-insensitive",
        isinstance(hits, list) and len(hits) == 1 and hits[0].get("id") == 1,
        f"got {hits!r}",
    )
    ok &= _check(
        "search_transactions no match → []",
        search_transactions(sample, "xyz") == [],
    )

    food = filter_by_category(sample, "food")
    ok &= _check(
        "filter_by_category case-insensitive",
        isinstance(food, list) and len(food) == 1 and food[0].get("id") == 1,
        f"got {food!r}",
    )

    print("All good." if ok else "Some checks failed — fix before opening a PR.")
