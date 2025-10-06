"""Starter for Assignment 02: Sentinels

This starter demonstrates a simple sentinel default value and safe handling.
"""

"""
Explanation (short):

- Goal: show how to use a unique sentinel object as a default to detect when a
  caller omitted an argument vs intentionally passed `None`.

- Why this matters: `None` is a valid value in many APIs. Using a `SENTINEL`
  object lets your function distinguish "not provided" from "explicitly
  provided None".

Student steps:
1. Run this file to observe the default and explicit-None behavior.
2. Inspect `choose_value` and notice the identity check `is _SENTINEL`.
3. Uncomment the failing example to see a scenario where absence vs `None`
   matters, and add tests that check for identity (use `is`) rather than
   equality (`==`).

This starter provides a working example and a commented failing example for you
to experiment with.
"""

_SENTINEL = object()


def choose_value(value=_SENTINEL, fallback=None):
    """Return value if provided; otherwise use fallback.

    The function intentionally uses a unique `_SENTINEL` object as the
    default. This allows callers to pass `None` explicitly without being
    confused with the case where the caller omitted the argument.
    """
    if value is _SENTINEL:
        return fallback
    return value


if __name__ == "__main__":
    # Working example: omitted argument -> fallback used
    print(choose_value())

    # Working example: explicit None -> None returned (caller asked for None)
    print(choose_value(None, fallback=123))

    # Failing / confusing example (uncomment to explore): callers sometimes
    # mistakenly check `if value:` which treats falsy-but-valid values like 0
    # or '' like missing. Use identity checks with SENTINEL instead.
    # print(choose_value(0, fallback=123))  # <- uncomment to inspect behavior
