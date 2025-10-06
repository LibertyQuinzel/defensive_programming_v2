"""Decorators to support pre/post conditions that work with kwargs/args."""

from __future__ import annotations

from functools import wraps
from typing import Callable


class ContractError(Exception):
    pass


def _normalize_pred(predicate: Callable):
    return predicate


def pre(predicate: Callable[..., bool], message: str = "Precondition failed"):
    """Decorator factory that enforces a precondition predicate.

  Explanation:
    - Purpose: create a decorator which calls `predicate(*args, **kwargs)`
      before invoking the wrapped function. If the predicate returns False,
      raise `ContractError` with the provided message.
    - Advantages: separate validation logic from function body; easier to
      reuse and test predicates.
    - Implementation detail: uses `functools.wraps` to preserve the wrapped
      function's metadata (name, docstring), which helps debugging and testing.
    """
    def deco(fn: Callable):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            if not predicate(*args, **kwargs):
                raise ContractError(message)
            return fn(*args, **kwargs)

        return wrapped

    return deco


def post(predicate: Callable[[object], bool], message: str = "Postcondition failed"):
    """Decorator factory that enforces a postcondition on the function result.

  Explanation:
    - Purpose: run the decorated function, then apply `predicate(result)` to
      check the return value. Raise `ContractError` if the predicate fails.
    - Useful for asserting invariants about results (e.g., finite, non-empty,
      within a range).
    - Note: like preconditions, postconditions add runtime overhead. Use them
      strategically (development/testing) or make them optional in production.
    """
    def deco(fn: Callable):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            result = fn(*args, **kwargs)
            if not predicate(result):
                raise ContractError(f"{message}: {result!r}")
            return result

        return wrapped

    return deco
