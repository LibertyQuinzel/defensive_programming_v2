"""Starter for Assignment 00: Hello and basic guard clauses.

This file is deliberately tiny. Run it with:

    python starter.py

Then edit the value of `x` and re-run.
"""

"""
Explanation (short):

- Goal: show a tiny guard clause that validates input early and provides a clear
  error or fallback. Guard clauses improve readability by handling invalid or
  edge inputs immediately instead of nesting logic.

- What's in this starter:
  1) a minimal function `greet` that validates its input
  2) one working example (happy path) printed when run
  3) one commented failing example that you can uncomment to observe a
     TypeError being raised (this simulates a failing test or runtime error).

Step-by-step (what the student should do):
1. Read the code and the short explanation above.
2. Run this file: `python topics/00-intro/starter.py` to see the happy path.
3. Inspect `greet` and reason about what inputs are allowed.
4. Uncomment the failing example below and re-run to see the error.
5. Modify `greet` to handle or document the behavior for the failing input.

The function below is intentionally strict: it insists on a `str` name and
returns a friendly default for empty strings.
"""

def greet(name):
    """Return a friendly greeting for a valid name.

    Preconditions:
    - `name` must be a str. If not, we raise a TypeError to fail fast.

    Postconditions:
    - returns a str that greets the provided name.
    - if the name is an empty string, a friendly default "Hello, stranger" is
      returned to avoid surprising empty responses.
    """
    # Defensive check: prefer a clear error early
    if not isinstance(name, str):
        raise TypeError("name must be a string")

    # Friendly default for empty names (business rule)
    if name == "":
        return "Hello, stranger"

    return f"Hello, {name}"


if __name__ == "__main__":
    # Working example (happy path)
    print(greet("Student"))

    # Failing example (uncomment to observe a TypeError; useful to demo a test
    # failure or to practice handling invalid inputs):
    # print(greet(123))  # <- uncomment to trigger a TypeError
