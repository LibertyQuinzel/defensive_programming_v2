"""Sentinel vs exception examples."""

from __future__ import annotations

from typing import Any, Callable, Iterable

SENTINEL = object()


class NotFoundError(Exception):
    """Raised when a required item is not found."""


def find_in_list(seq: Iterable[Any], predicate: Callable[[Any], bool], default=SENTINEL):
    """Return the first item matching `predicate` or a sentinel when missing."""
    for item in seq:
        if predicate(item):
            return item
    return default


def get_required(seq: Iterable[Any], index: int):
    """Return the item at `index` or raise `NotFoundError`."""
    try:
        return list(seq)[index]
    except IndexError:
        raise NotFoundError(f"Index {index} out of range")
