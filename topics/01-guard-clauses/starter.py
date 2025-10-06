"""Starter for Assignment 01: Guard Clauses

Complete the TODO comments. Keep functions small and add simple checks.
"""

"""
Explanation (short):

- Goal: demonstrate a simple function that should be hardened with guard
  clauses. Students will add input validation (types and value checks) to avoid
  runtime errors and to provide clear, actionable exceptions.

What this starter shows:
1) A minimal `divide` implementation (intentionally without checks).
2) A working example (divide 10 by 2) printed on run.
3) A commented failing example that triggers a runtime error (or would
   trigger a failing test) if you uncomment it.

Student steps:
1. Run: `python topics/01-guard-clauses/starter.py` and observe the happy path.
2. Read the `divide` docstring and decide which preconditions to enforce.
3. Implement checks for:
   - types (allow int/float, reject bool and other types)
   - divide-by-zero
   - NaN/Inf using `math.isfinite` (optional)
4. Re-run and uncomment the failing example to confirm the check catches it.

After you implement the checks, run the topic tests (if available) to verify
the behavior.
"""

def divide(a, b):
    """Divide two numbers with minimal checks (student should harden this).

    Currently this function trusts that the caller supplies valid numeric
    operands. Your task is to add explicit guard clauses to validate inputs
    and raise clear exceptions when inputs are invalid.
    """
    # Intentionally minimal: student should add checks here
    return a / b


if __name__ == "__main__":
    # Working example (happy path)
    print(divide(10, 2))

    # Failing example: uncomment to observe a runtime error or to practice
    # writing a guard clause that prevents it.
    # print(divide(10, 0))  # <- uncomment to trigger ZeroDivisionError if no guard
