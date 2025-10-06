"""Tests for defensive hardening of arithmetic operations.


- Purpose: these tests demonstrate how small numeric APIs should be hardened against
  incorrect inputs and undefined behavior. They encode the contract for `add`,
  `multiply`, and `divide` using domain-specific exceptions instead of allowing
  Python's built-in errors or silent failures.

- Key lessons covered:
  1. Input validation: reject values that are not of the expected type (e.g.,
      strings or booleans) with clear, descriptive exceptions (InvalidOperandError).
  2. Domain-specific errors: signal domain problems explicitly (DivisionByZeroError)
      rather than returning sentinel values or letting a generic ZeroDivisionError
      bubble up unpredictably.
  3. Happy path tests: verify correct numerical results to ensure normal behavior
      is preserved while adding defensive checks.

These tests are intentionally concise: each focuses on one failure mode or the
happy path. Students should use them as a specification when implementing guard
clauses in `skeleton.py`.
"""

import pytest

from examples.operations import (
     add,
     divide,
     multiply,
     InvalidOperandError,
     DivisionByZeroError,
)


def test_add_invalid_operand():
    with pytest.raises(InvalidOperandError):
        add(None, 1)
    with pytest.raises(InvalidOperandError):
        add(1, "two")


def test_multiply_invalid_operand():
    with pytest.raises(InvalidOperandError):
        multiply(True, 2)  # booleans are rejected here


def test_divide_by_zero():
    with pytest.raises(DivisionByZeroError):
        divide(5, 0)


def test_divide_and_add_happy_path():
    assert add(2, 3) == 5.0
    assert divide(6, 3) == 2.0
