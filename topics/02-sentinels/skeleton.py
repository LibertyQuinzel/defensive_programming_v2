"""Skeleton for Assignment 02 - Sentinels.

Provide a small utility that demonstrates using a sentinel default value to
distinguish omitted arguments from explicit ``None`` values.
"""

_SENTINEL = object()


def choose_value(value=_SENTINEL, fallback=None):
    """Instructor-target function for Part A (left unimplemented for students).

    Students implement this for Part B to satisfy instructor tests.
    """
    raise NotImplementedError("Implement choose_value(value=_SENTINEL, fallback=None) in the skeleton for Part B")


def validated_choose(value=_SENTINEL, fallback=None):
    """Student-facing helper (implemented) for tests-first workflow.

    Returns ``fallback`` when the caller omits ``value`` (i.e., value is the
    sentinel). Returns the explicit value (including ``None``) otherwise.
    """
    if value is _SENTINEL:
        return fallback
    return value
