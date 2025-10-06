"""Decorators to support pre/post conditions that work with kwargs/args."""

from __future__ import annotations

from functools import wraps
from typing import Callable


class ContractError(Exception):
    pass


def pre(predicate: Callable[..., bool], message: str = "Precondition failed"):
    """Decorator factory that enforces a precondition predicate."""
    def deco(fn: Callable):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            if not predicate(*args, **kwargs):
                raise ContractError(message)
            return fn(*args, **kwargs)

        return wrapped

    return deco


def post(predicate: Callable[[object], bool], message: str = "Postcondition failed"):
    """Decorator factory that enforces a postcondition on the function result."""
    def deco(fn: Callable):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            result = fn(*args, **kwargs)
            if not predicate(result):
                raise ContractError(f"{message}: {result!r}")
            return result

        return wrapped

    return deco
