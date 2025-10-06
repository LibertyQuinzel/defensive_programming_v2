"""Starter for Assignment 03: Design by Contract

This starter shows a precondition and postcondition example.
Edit the function to make tests pass and obey the contract.
"""

"""
Explanation (short):

- Goal: introduce design-by-contract concepts — preconditions and
  postconditions — and show how they make function behavior explicit.

- The `reciprocal` function demonstrates:
  - Precondition checks: validate inputs before computing.
  - Postcondition checks: assert properties about the result after computation.

Student steps:
1. Run this file to see the happy path:
   `python topics/03-design-by-contract/starter.py`
2. Experiment by calling `reciprocal` with edge inputs (e.g., `True`, `0`,
   very small numbers) to see pre/post failures.
3. Refactor the inline checks into reusable `@pre` and `@post` decorators
   (see the example_contracts module for reference) and re-run the tests.
4. Optionally add a dev-mode toggle to disable postconditions in production
   and discuss the trade-offs.

This starter includes a working example and a commented failing example that
you can uncomment to trigger a failure.
"""


def reciprocal(x):
    """Return reciprocal with explicit pre/post checks.

    Preconditions:
    - x must be a number (int or float, booleans are rejected).
    - x must not be zero.

    Postconditions:
    - result * x is approximately 1 (within floating-point tolerance).
    """
    # Precondition: x must be numeric and not a boolean
    if not isinstance(x, (int, float)):
        raise TypeError("x must be a number")
    if x == 0:
        raise ValueError("x must not be zero")

    result = 1 / x

    # Postcondition: result times x should be approximately 1
    if not abs(result * x - 1) < 1e-9:
        raise AssertionError("postcondition failed")
    return result


if __name__ == "__main__":
    # Working example
    print(reciprocal(2))

    # Failing examples (uncomment one at a time to observe pre/post failures):
    # reciprocal(True)   # <- precondition: boolean is rejected
    # reciprocal(0)      # <- precondition: division by zero
