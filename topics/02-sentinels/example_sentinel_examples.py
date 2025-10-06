"""Sentinel vs exception examples."""

from __future__ import annotations

from typing import Any, Callable, Iterable

SENTINEL = object()


class NotFoundError(Exception):
    """Raised when a required item is not found."""


def find_in_list(seq: Iterable[Any], predicate: Callable[[Any], bool], default=SENTINEL):
        """Return the first item matching `predicate` or a sentinel when missing.

        Explanation:
        - Purpose: provide a lightweight search utility that returns a sentinel
            instead of raising an exception when no matching element exists.
        - Behavior: iterate lazily through `seq` and return the first element for
            which `predicate(element)` is truthy. If none match, return the `default`
            sentinel (defaults to the module-level `SENTINEL`).
        - Why sentinel: callers can check `is SENTINEL` to distinguish between a
            legitimately stored `None` and "not found".

        Example:
        >>> find_in_list([1,2,3], lambda x: x==2)
        2
        >>> find_in_list([], lambda x: True) is SENTINEL
        True
        """
        for item in seq:
                if predicate(item):
                        return item
        return default


def get_required(seq: Iterable[Any], index: int):
        """Return the item at `index` or raise `NotFoundError`.

        Explanation:
        - Purpose: strict accessor variant that treats a missing index as an error.
        - Behavior: attempt to retrieve the element at position `index`. If the
            index is out of range, raise `NotFoundError` with a descriptive message.
        - Use-case: prefer this when a missing value represents an exceptional
            condition rather than a common case.
        """
        try:
                return list(seq)[index]
        except IndexError:
                raise NotFoundError(f"Index {index} out of range")
