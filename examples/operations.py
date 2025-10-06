"""Example operations module demonstrating defensive programming.

This module intentionally performs input validation, uses guard clauses, and raises
custom exceptions with clear messages. It also logs at error boundaries (no secrets).
"""

from __future__ import annotations

import logging
import math
from typing import Union

Number = Union[int, float]

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
handler.setFormatter(formatter)
if not logger.hasHandlers():
    logger.addHandler(handler)
logger.setLevel(logging.WARNING)


class DefensiveError(Exception):
    """Base class for defensive programming exceptions."""


class InvalidOperandError(DefensiveError):
    """Raised when a non-numeric operand is provided."""


class DivisionByZeroError(DefensiveError):
    """Raised when an attempt is made to divide by zero."""


def _is_number(x: object) -> bool:
    """Return True if `x` is a finite numeric value acceptable as an operand.

    Explanation:
    - Purpose: centralize numeric validation so all arithmetic functions use the
      same definition of "number".
    - Accepts: ints and floats. Explicitly rejects booleans (since bool is a
      subclass of int in Python) to avoid surprising behavior.
    - Rejects: NaN and +/-infinity using `math.isfinite`.
    - Returns: True for finite int/float values, False otherwise.
    """
    try:
        # allow ints and floats, but reject booleans and other types
        if not (isinstance(x, (int, float)) and not isinstance(x, bool)):
            return False
        # reject NaN and infinities as invalid operands
        return math.isfinite(float(x))
    except Exception:
        return False


def add(a: Number, b: Number) -> float:
    """Return the sum of two numbers with defensive validation.

    Explanation:
    - Purpose: perform a simple addition while guarding against invalid inputs.
    - Inputs: `a`, `b` should be finite ints or floats (booleans rejected).
    - Error modes: raises `InvalidOperandError` when either operand is invalid.
    - Output: returns a Python float representing the sum.
    """
    if not _is_number(a):
        logger.warning("Invalid operand for add: %r", a)
        raise InvalidOperandError("Operand 'a' must be a number")
    if not _is_number(b):
        logger.warning("Invalid operand for add: %r", b)
        raise InvalidOperandError("Operand 'b' must be a number")
    return float(a) + float(b)


def subtract(a: Number, b: Number) -> float:
    """Return the difference (a - b) after validating operands."""
    if not _is_number(a):
        logger.warning("Invalid operand for subtract: %r", a)
        raise InvalidOperandError("Operand 'a' must be a number")
    if not _is_number(b):
        logger.warning("Invalid operand for subtract: %r", b)
        raise InvalidOperandError("Operand 'b' must be a number")
    return float(a) - float(b)


def multiply(a: Number, b: Number) -> float:
    """Return the product of two numbers with defensive checks."""
    if not _is_number(a):
        logger.warning("Invalid operand for multiply: %r", a)
        raise InvalidOperandError("Operand 'a' must be a number")
    if not _is_number(b):
        logger.warning("Invalid operand for multiply: %r", b)
        raise InvalidOperandError("Operand 'b' must be a number")
    return float(a) * float(b)


def divide(a: Number, b: Number) -> float:
    """Return the quotient a / b with defensive validation."""
    if not _is_number(a):
        logger.warning("Invalid operand for divide: %r", a)
        raise InvalidOperandError("Operand 'a' must be a number")
    if not _is_number(b):
        logger.warning("Invalid operand for divide: %r", b)
        raise InvalidOperandError("Operand 'b' must be a number")
    if float(b) == 0.0:
        logger.warning("Attempt to divide by zero: a=%r, b=%r", a, b)
        raise DivisionByZeroError("Cannot divide by zero")
    return float(a) / float(b)
