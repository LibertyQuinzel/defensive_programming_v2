"""Skeleton for Assignment 01 - Guard Clauses.

This module provides small functions for students to practice defensive
programming and test-driven development.

Two functions are relevant to the assignment flow:

- validated_add(a, b): implemented here. Students should write tests for
    this function (tests-first exercise).
- guarded_divide(a, b): intentionally unimplemented in the skeleton. The
    instructor provides canonical Part A tests; students must implement the
    function to make those tests pass (implementation-first exercise).

The helpers and functions intentionally keep behavior small and explicit so
students can add guard clauses and observe test failures during TDD.
"""

from __future__ import annotations

import math
from typing import Union

Number = Union[int, float]


def _is_number(x: object) -> bool:
    """Return True if ``x`` is an int or float (but not bool) and finite.

    Notes:
    - ``bool`` subclasses ``int`` in Python, so we explicitly exclude it.
    - We also reject NaN and infinite values via ``math.isfinite``.
    - Any exception during coercion results in a False return value.
    """
    try:
        if not (isinstance(x, (int, float)) and not isinstance(x, bool)):
            return False
        return math.isfinite(float(x))
    except Exception:
        return False


def validated_add(a: Number, b: Number) -> float:
    """Return the sum of two numeric operands after defensive validation.

    Behavior (intended and tested by student exercises):
    - Raise TypeError for booleans or non-numeric input.
    - Raise TypeError for NaN or infinite values.
    - Otherwise return ``float(a) + float(b)``.
    """
    if not _is_number(a):
        raise TypeError("Operand 'a' must be a number")
    if not _is_number(b):
        raise TypeError("Operand 'b' must be a number")
    return float(a) + float(b)


def guarded_divide(a: Number, b: Number) -> float:
    """Guarded division with small, clear guard clauses.

    Args:
        a: The dividend (number to be divided)
        b: The divisor (number to divide by)

    Returns:
        The quotient as a float

    Raises:
        TypeError: If ``a`` or ``b`` is not a number (int/float) or is a boolean
        ValueError: If ``b`` equals zero

    Expected behavior (what instructor Part A tests assert):
    - If ``a`` or ``b`` is not a number (int/float) or is a boolean, raise
        TypeError.
    - If ``b`` equals zero, raise ValueError.
    - Otherwise return the numeric quotient ``a / b``.

    Students should implement this function to satisfy the tests in the
    instructor Part A test suite.

    Implementation hints:
    - Use the provided ``_is_number()`` helper function for validation
    - Check types first, then check for zero division
    - Remember: bool subclasses int in Python, so isinstance(True, int) is True!
    """
    # TODO: Students must implement this for Part B. For TDD flow this
    # skeleton intentionally raises until implemented.
    #
    # Suggested implementation pattern:
    # 1. Check if 'a' is a valid number using _is_number()
    # 2. Check if 'b' is a valid number using _is_number()  
    # 3. Check if 'b' equals zero
    # 4. Return the division result as float
    
    raise NotImplementedError("Implement guarded_divide(a, b) in the skeleton for Part B")
