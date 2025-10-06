"""Student test template for Topic 02 - Sentinels.

Use this template to test `choose_value(value=_SENTINEL, fallback=None)` in
`skeleton.py`.

Run from the repository root:

    PYTHONPATH=. pytest -q defensive_programming_v2/topics/02-sentinels/test_template_for_students.py
"""

from pathlib import Path
import importlib.util
import pytest

skel_path = Path(__file__).parent / "skeleton.py"
spec = importlib.util.spec_from_file_location("topic02_sentinel", skel_path)
skeleton = importlib.util.module_from_spec(spec)
spec.loader.exec_module(skeleton)


def test_validated_choose_omitted_uses_fallback():
    # Part 1: tests-first for the implemented helper
    assert skeleton.validated_choose(fallback=5) == 5


def test_validated_choose_explicit_none():
    assert skeleton.validated_choose(None, fallback=5) is None


def test_validated_choose_zero_is_valid():
    assert skeleton.validated_choose(0, fallback=5) == 0


#########################################################################
# Part 2: Implementation-first exercise (instructor-provided tests exist for
# `choose_value`. Students implement the code to satisfy those tests.)
#########################################################################


def test_choose_value_omitted():
    """Omitted value should return the fallback value."""
    assert skeleton.choose_value(fallback=5) == 5


def test_choose_value_explicit_none():
    """Explicit None should be returned rather than the fallback."""
    assert skeleton.choose_value(None, fallback=5) is None
