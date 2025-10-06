"""Design by contract helpers and examples."""

from __future__ import annotations

import math
from typing import Callable


class ContractError(Exception):
    """Raised when a contract (pre/post) is violated."""


# Simple decorator factories for pre/post conditions
def pre(check: Callable[..., bool], msg: str = "Precondition failed"):
    """Decorator factory to enforce a precondition on a function.

    Explanation:
    - Purpose: return a decorator that checks a predicate against the function
      arguments before the function runs. If the predicate returns False, a
      `ContractError` is raised with `msg`.
    - Usage: `@pre(lambda x: x>0, "x must be > 0")` placed above a function
      ensures arguments satisfy the precondition every call.
    - Note: the decorator preserves the function's contract but does not
      automatically preserve metadata; in simple examples we set `__name__` to
      help with basic introspection. For production use, prefer `functools.wraps`.
    """
    def decorator(fn):
        def wrapper(*args, **kwargs):
            if not check(*args, **kwargs):
                raise ContractError(msg)
            return fn(*args, **kwargs)

        wrapper.__name__ = fn.__name__
        return wrapper

    return decorator


def post(check: Callable[[object], bool], msg: str = "Postcondition failed"):
    """Decorator factory to enforce a postcondition on a function's result.

    Explanation:
    - Purpose: return a decorator that runs `fn`, then applies `check` to the
      result. If the check fails, raise `ContractError` with the `msg` and the
      offending result included for easier debugging.
    - Use-case: assert invariants about return values (e.g., result is finite,
      non-empty, within range).
    - Note: postconditions add runtime cost, so consider enabling them during
      development and disabling in hot production paths if performance matters.
    """
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
        """Return 1/x with contract checks applied via decorators.

        Explanation:
        - This function is decorated with a `@pre` that ensures `x` is a non-zero
            numeric value and a `@post` that asserts the returned value is a finite
            float.
        - The decorators raise `ContractError` if pre/post conditions are violated.
        - This implementation shows how to attach declarative contracts to a
            function without cluttering its body with checks.
        """
        return 1.0 / float(x)
