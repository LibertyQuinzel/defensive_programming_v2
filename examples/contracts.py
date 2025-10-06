"""Design by contract helpers and examples."""

from __future__ import annotations

import math
from typing import Callable


class ContractError(Exception):
    """Raised when a contract (pre/post) is violated."""


# Simple decorator factories for pre/post conditions
def pre(check: Callable[..., bool], msg: str = "Precondition failed"):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            if not check(*args, **kwargs):
                raise ContractError(msg)
            return fn(*args, **kwargs)

        wrapper.__name__ = fn.__name__
        return wrapper

    return decorator


def post(check: Callable[[object], bool], msg: str = "Postcondition failed"):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            if not check(result):
                raise ContractError(f"{msg}: {result!r}")
            return result

        wrapper.__name__ = fn.__name__
        return wrapper

    return decorator


# Example function with pre/post conditions
@pre(
    lambda x: (
        (isinstance(x, (int, float)) and not isinstance(x, bool))
        and float(x) != 0.0
    ),
    "x must be a non-zero numeric",
)
@post(
    lambda r: isinstance(r, float) and math.isfinite(r),
    "result must be finite float",
)
def reciprocal(x: float) -> float:
    """Return 1/x with contract checks applied via decorators."""
    return 1.0 / float(x)
