"""
Load and save app data as JSON so it survives between runs.

Data shape:
{
    "transactions": [ {id, type, amount, category, date, description}, ... ],
    "savings_goals": [ {name, target_amount, current_amount}, ... ]
}

Assigned to: Emmanuel
"""

import json
import os

DEFAULT_DATA = {
    "transactions": [],
    "savings_goals": [],
}


def load_data(filepath):
    """
    Load the data dict from filepath.

    Args:
        filepath (str): path to the JSON file (e.g. "data/budget_data.json")

    Returns:
        dict: always has "transactions" (list) and "savings_goals" (list).
              If the file is missing or unreadable, return DEFAULT_DATA
              (don't crash).
    """
    filepath = filepath.strip()

    if not filepath:
        return DEFAULT_DATA.copy()

    is_file_exist = os.path.exists(filepath)

    if not is_file_exist:
        return DEFAULT_DATA.copy()
    
    with open(filepath, "rb") as file:
        file_obj = file.read()

        if not file_obj:
            return DEFAULT_DATA.copy()

        try:
            obj = json.loads(file_obj)
        except:
            return DEFAULT_DATA.copy()

        keys = obj.keys()

        if "transactions" not in keys or "savings_goals" not in keys:
            return DEFAULT_DATA.copy()

        transactions = obj["transactions"]
        savings_goals = obj["savings_goals"]

        if not isinstance(transactions, list) or not isinstance(savings_goals, list):
            return DEFAULT_DATA.copy()

        
        return obj


def save_data(filepath, data):
    """
    Save the data dict to filepath as JSON.

    Args:
        filepath (str): path to write to
        data (dict): same shape as DEFAULT_DATA

    Returns:
        bool: True if the write worked, False if it failed
    """
    try:
        with open(filepath, "wb") as file:
            obj = json.dumps(data).encode("utf-8")
            file.write(obj)

        return True
    except:
        return False


def _check(name, condition, detail=""):
    if condition:
        print(f"  PASS  {name}")
        return True
    extra = f" — {detail}" if detail else ""
    print(f"  FAIL  {name}{extra}")
    return False


if __name__ == "__main__":
    # Run: python3 data_store.py
    import tempfile

    print("Self-check: data_store.py")
    ok = True
    test_dir = tempfile.mkdtemp()
    path = os.path.join(test_dir, "budget_data.json")

    missing = load_data(path)
    ok &= _check(
        "load_data missing file → default shape",
        isinstance(missing, dict)
        and "transactions" in missing
        and "savings_goals" in missing
        and missing["transactions"] == []
        and missing["savings_goals"] == [],
        f"got {missing!r}",
    )
    ok &= _check(
        "load_data missing file → not same object as DEFAULT_DATA",
        isinstance(missing, dict) and missing is not DEFAULT_DATA,
        "return a copy so later edits don't mutate DEFAULT_DATA",
    )

    sample = {
        "transactions": [
            {
                "id": 1,
                "type": "expense",
                "amount": 10.0,
                "category": "Food",
                "date": "2026-08-01",
                "description": "test",
            }
        ],
        "savings_goals": [],
    }
    saved = save_data(path, sample)
    ok &= _check("save_data returns True", saved is True, f"got {saved!r}")
    ok &= _check("save_data created file", os.path.isfile(path))

    loaded = load_data(path)
    ok &= _check(
        "load_data round-trip",
        loaded == sample,
        f"got {loaded!r}",
    )

    bad_path = os.path.join(test_dir, "broken.json")
    with open(bad_path, "w", encoding="utf-8") as f:
        f.write("{not valid json")
    broken = load_data(bad_path)
    ok &= _check(
        "load_data bad JSON → default shape (no crash)",
        isinstance(broken, dict)
        and "transactions" in broken
        and "savings_goals" in broken,
        f"got {broken!r}",
    )

    print("All good." if ok else "Some checks failed — fix before opening a PR.")
