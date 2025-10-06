"""Skeleton for Assignment 04 - Decorators.

This module exposes a small decorator ``announce`` that demonstrates how
wrapping a function can add cross-cutting behavior (printing) while
preserving the wrapped function's return value and metadata.
"""

import functools
import os


def announce(fn):
    """Decorator that prints a message when the wrapped function is called.

    Contract:
    - The decorator must return a callable that returns the original function's
      return value.
    - If environment variable ``QUIET`` is set (non-empty), printing is
      suppressed.

    Students should implement the decorator for Part B so the instructor
    Part A tests can exercise its behavior.
    """

    # Instructor target: announce remains intentionally unimplemented here.
    raise NotImplementedError("Implement announce(fn) decorator in the skeleton for Part B")


def basic_add(a, b):
    """Student-facing implemented helper: simple addition for tests-first.

    Students can write tests for this small working function before tackling
    the decorator implementation in Part B.
    """
    return a + b

