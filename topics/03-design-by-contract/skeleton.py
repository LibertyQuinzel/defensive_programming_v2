"""Skeleton for Assignment 03 - Design by Contract.

This module contains a small function ``reciprocal(x)`` intended to show
preconditions and postconditions (design-by-contract). Students should add
clear precondition checks (type and non-zero) and ensure the postcondition
``reciprocal(x) * x == 1`` holds for valid inputs.
"""


def validated_reciprocal(x):
    """Student-facing helper: implemented reciprocal for tests-first.

    Performs the needed pre- and post-condition checks and returns 1/x.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be a number")
    if x == 0:
        raise ValueError("x must not be zero")
    result = 1 / x
    if not abs(result * x - 1) < 1e-9:
        raise AssertionError("postcondition failed")
    return result


def reciprocal(x):
    """Instructor-target function for Part A (unimplemented in skeleton).

    Students implement this for Part B to satisfy instructor tests.
    """
    # Instructor-target function for Part A (unimplemented in skeleton).
    # Students implement this for Part B to satisfy instructor tests.
    raise NotImplementedError("Implement reciprocal(x) in the skeleton for Part B")
    
