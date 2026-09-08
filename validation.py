"""
Helpers for reading user input safely.
Other modules should use these instead of calling input() directly
so bad input re-prompts instead of crashing.

Assigned to: Emmanuel
"""

from datetime import datetime


def get_non_empty_text(prompt):
    """
    Ask until the user enters non-empty text.

    Args:
        prompt (str): text shown to the user

    Returns:
        str: stripped non-empty string
    """
    user_value = input(prompt)

    user_value = user_value.strip()
    if not user_value:
        user_value = get_non_empty_text(prompt)

    return user_value


def get_valid_amount(prompt):
    """
    Ask until the user enters a valid amount.

    Args:
        prompt (str): text shown to the user

    Returns:
        float: must be > 0

    Notes:
        Reject non-numeric input and values <= 0; re-prompt instead of crashing.
    """
    user_amount = input(prompt)

    user_amount = user_amount.strip()

    try:
        user_amount = float(user_amount)
    except:
        user_amount = get_valid_amount(prompt)


    if user_amount <= 0:
        user_amount = get_valid_amount(prompt)

    return user_amount


def get_valid_menu_choice(prompt, valid_choices):
    """
    Ask until the user picks one of the allowed options.

    Args:
        prompt (str): text shown to the user
        valid_choices (list[str]): allowed answers, e.g. ["1", "2", "3"]

    Returns:
        str: the chosen value (one of valid_choices)
    """
    user_choice = input(prompt)

    user_choice = user_choice.strip()

    if not user_choice or user_choice not in valid_choices:
        user_choice = get_valid_menu_choice(prompt, valid_choices)

    return user_choice


def get_yes_no(prompt):
    """
    Ask until the user answers yes or no.

    Args:
        prompt (str): text shown to the user

    Returns:
        bool: True for yes (y/yes), False for no (n/no), case-insensitive
    """
    user_option = input(prompt).strip().lower()

    while not user_option or user_option not in ["y", "n", 'no', 'yes']:
        user_option = input(prompt).strip().lower()

    if user_option == "y" or user_option == "yes":
        return True
    else:
        return False


def get_valid_date(prompt):
    """
    Ask until the user enters a valid date as YYYY-MM-DD.

    Args:
        prompt (str): text shown to the user

    Returns:
        str: date string in YYYY-MM-DD form

    Notes:
        Reject empty input and values that are not a real calendar date
        in YYYY-MM-DD (e.g. "wywyew", "2026-13-40"); re-prompt instead
        of crashing.
    """
    while True:
        value = input(prompt).strip()
        if is_valid_date(value):
            return value


def is_valid_date(value):
    """
    Return True if value is a real calendar date in YYYY-MM-DD form.
    """
    try:
        datetime.strptime(value.strip(), "%Y-%m-%d")
        return True
    except (TypeError, ValueError, AttributeError):
        return False


def _check(name, condition, detail=""):
    if condition:
        print(f"  PASS  {name}")
        return True
    extra = f" — {detail}" if detail else ""
    print(f"  FAIL  {name}{extra}")
    return False


def _with_inputs(answers):
    """Feed fake keyboard answers so we can test without typing."""
    import builtins

    unused = list(answers)

    def fake_input(prompt=""):
        if not unused:
            raise AssertionError(f"Ran out of fake answers at prompt: {prompt!r}")
        value = unused.pop(0)
        print(f"{prompt}{value}")
        return value

    real_input = builtins.input
    builtins.input = fake_input
    return real_input, unused


if __name__ == "__main__":
    # Run: python3 validation.py
    import builtins

    print("Self-check: validation.py")
    print("(uses fake input — you don't need to type)")
    ok = True

    real_input, leftover = _with_inputs(["", "   ", "Groceries"])
    try:
        text = get_non_empty_text("Category: ")
        ok &= _check("get_non_empty_text skips blanks", text == "Groceries", f"got {text!r}")
        ok &= _check("get_non_empty_text used all retries", leftover == [])
    except Exception as err:
        ok &= _check("get_non_empty_text no crash", False, str(err))
    finally:
        builtins.input = real_input

    real_input, leftover = _with_inputs(["abc", "-5", "0", "12.5"])
    try:
        amount = get_valid_amount("Amount: ")
        ok &= _check("get_valid_amount accepts 12.5", amount == 12.5, f"got {amount!r}")
        ok &= _check("get_valid_amount rejected bad values first", leftover == [])
    except Exception as err:
        ok &= _check("get_valid_amount no crash", False, str(err))
    finally:
        builtins.input = real_input

    real_input, leftover = _with_inputs(["9", "2"])
    try:
        choice = get_valid_menu_choice("Choice: ", ["1", "2", "3"])
        ok &= _check("get_valid_menu_choice returns '2'", choice == "2", f"got {choice!r}")
    except Exception as err:
        ok &= _check("get_valid_menu_choice no crash", False, str(err))
    finally:
        builtins.input = real_input

    real_input, leftover = _with_inputs(["maybe", "YES"])
    try:
        yes = get_yes_no("Confirm: ")
        ok &= _check("get_yes_no YES → True", yes is True, f"got {yes!r}")
    except Exception as err:
        ok &= _check("get_yes_no no crash", False, str(err))
    finally:
        builtins.input = real_input

    real_input, leftover = _with_inputs(["n"])
    try:
        no = get_yes_no("Confirm: ")
        ok &= _check("get_yes_no n → False", no is False, f"got {no!r}")
    except Exception as err:
        ok &= _check("get_yes_no (n) no crash", False, str(err))
    finally:
        builtins.input = real_input

    real_input, leftover = _with_inputs(["wywyew", "2026-13-40", "2026-08-01"])
    try:
        date = get_valid_date("Date (YYYY-MM-DD): ")
        ok &= _check(
            "get_valid_date accepts YYYY-MM-DD",
            date == "2026-08-01",
            f"got {date!r}",
        )
        ok &= _check("get_valid_date rejected bad values first", leftover == [])
    except Exception as err:
        ok &= _check("get_valid_date no crash", False, str(err))
    finally:
        builtins.input = real_input

    print("All good." if ok else "Some checks failed — fix before opening a PR.")
