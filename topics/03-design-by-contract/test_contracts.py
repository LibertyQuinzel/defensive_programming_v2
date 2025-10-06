"""Tests for design-by-contract examples (pre/post conditions).


- Purpose: These tests codify preconditions and postconditions for a small API
  (`reciprocal`) and demonstrate how contract violations should be signalled
  using a domain-specific `ContractError`.

- Key lessons covered:
  1. Preconditions: check and reject illegal argument types or values early
      (e.g., booleans when numbers are required).
  2. Postconditions: enforce invariants after computation (e.g., the result is
      finite and meaningful), converting runtime surprises into explicit errors.
  3. Deterministic failures: contract violations should be predictable and
      testable, not dependent on platform-specific exceptions.

Students implementing contract checks should make `reciprocal` raise
`ContractError` on invalid inputs or when the computation would produce an
invalid result like infinity or NaN.
"""

import math

import pytest

from examples.contracts import reciprocal, ContractError


def test_reciprocal_happy_path():
    assert math.isclose(reciprocal(2), 0.5)


def test_reciprocal_precondition():
    with pytest.raises(ContractError):
        reciprocal(True)  # boolean is rejected


def test_reciprocal_postcondition_nan():
    with pytest.raises(ContractError):
        reciprocal(0.0)  # division by zero -> inf -> postcondition fails
