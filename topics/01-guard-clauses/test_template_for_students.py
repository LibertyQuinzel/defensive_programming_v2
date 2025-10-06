"""Student test template for Topic 01 - Guard Clauses.

This template provides two sections:

- Part 1: tests-first exercise — write tests for the provided
  implementation `validated_add`.
- Part 2: implementation-first exercise — implement `guarded_divide` to
  satisfy the instructor-provided tests (the canonical spec).

Run the file from the repository root:

    PYTHONPATH=. pytest -q defensive_programming_v2/topics/01-guard-clauses/test_template_for_students.py

Edit or extend these tests before implementing code (TDD workflow).
"""

from pathlib import Path
import importlib.util
import math
import pytest

# Load the sibling skeleton.py as a module so tests run against that file
skel_path = Path(__file__).parent / "skeleton.py"
spec = importlib.util.spec_from_file_location("topic01_skeleton", skel_path)
skeleton = importlib.util.module_from_spec(spec)
spec.loader.exec_module(skeleton)


#########################################################################
# Part 1: Tests-first exercise (students must write tests for `validated_add`)
#########################################################################


def test_validated_add_happy():
    """A simple happy-path test for the provided implementation.

    Students: this file is a template. Replace or extend these tests with
    your own assertions before running the instructor Part A spec.
    """
    assert skeleton.validated_add(2, 3) == 5.0


def test_validated_add_rejects_bool():
    """Booleans should be rejected by validated_add (students should assert this)."""
    with pytest.raises(TypeError):
        skeleton.validated_add(True, 1)


#########################################################################
# Part 2: Implementation-first exercise (instructor-provided tests exist for
# `guarded_divide`. Students implement the code to satisfy those tests.)
#########################################################################


def test_guarded_divide_happy():
    """Happy path: simple division returns the numeric quotient."""
    assert skeleton.guarded_divide(10, 2) == 5


def test_guarded_divide_type_error_for_string():
    """Non-numeric operands (e.g., strings) should raise TypeError."""
    with pytest.raises(TypeError):
        skeleton.guarded_divide("10", 2)


def test_guarded_divide_value_error_for_zero_divisor():
    """Dividing by zero should raise ValueError (per assignment contract)."""
    with pytest.raises(ValueError):
        skeleton.guarded_divide(1, 0)


def test_guarded_divide_reject_bool():
    """Booleans should be rejected because bool subclasses int in Python."""
    with pytest.raises(TypeError):
        skeleton.guarded_divide(True, 1)


def test_guarded_divide_reject_nan():
    """If your implementation rejects NaN/inf, assert that here.

    This test accepts either TypeError or ValueError depending on your chosen
    contract; update it to match your implementation if you prefer one.
    """
    nan = float("nan")
    with pytest.raises((TypeError, ValueError)):
        skeleton.guarded_divide(nan, 1)


# End of template
