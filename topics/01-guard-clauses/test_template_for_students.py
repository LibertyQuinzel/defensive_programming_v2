"""Student test template for Topic 01 - Guard Clauses.

This template provides two sections:

- Part 1: tests-first exercise — write tests for the provided
  implementation `validated_add`.
- Part 2: implementation-first exercise — implement `guarded_divide` to
  satisfy the instructor-provided tests (the canonical spec).

Run the file from the repository root:

    PYTHONPATH=. pytest -q defensive_programming_v2/topics/01-guard-clauses/test_template_for_students.py

Edit or extend these tests before implementing code (TDD workflow).

Learning objectives:
- Practice writing comprehensive test cases for edge cases
- Understand how guard clauses protect against invalid inputs
- Learn to handle type validation in Python (especially bool vs int)
- Implement defensive division with clear error messages
"""

from pathlib import Path
import importlib.util
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


# TODO: Add more comprehensive tests for validated_add
# Suggested test cases (uncomment and implement):

# def test_validated_add_accepts_floats():
#     """Test that floating point numbers work correctly."""
#     # TODO: Test with float inputs like 2.5 + 3.7
#     pass

# def test_validated_add_accepts_mixed_int_float():
#     """Test mixing int and float arguments."""
#     # TODO: Test cases like validated_add(2, 3.5) and validated_add(2.5, 3)
#     pass

# def test_validated_add_rejects_strings():
#     """String inputs should raise TypeError."""
#     # TODO: Test with string inputs like "10" or "hello"
#     pass

# def test_validated_add_rejects_none():
#     """None input should raise TypeError."""
#     # TODO: Test with None as one or both arguments
#     pass

# def test_validated_add_rejects_lists():
#     """List inputs should raise TypeError."""
#     # TODO: Test with list inputs like [1, 2] or []
#     pass

# def test_validated_add_rejects_nan():
#     """NaN (Not a Number) should be rejected."""
#     # TODO: Test with float('nan') as input
#     # Hint: Use float('nan') to create a NaN value
#     pass

# def test_validated_add_rejects_infinity():
#     """Infinite values should be rejected."""
#     # TODO: Test with float('inf') and float('-inf')
#     pass

# def test_validated_add_both_args_invalid():
#     """Test behavior when both arguments are invalid."""
#     # TODO: What happens when both args are invalid? Which error is raised first?
#     pass


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


# Additional test stubs for students to implement
# (These help ensure comprehensive coverage of guarded_divide)

# def test_guarded_divide_float_inputs():
#     """Test division with floating point numbers."""
#     # TODO: Test cases like guarded_divide(7.5, 2.5)
#     pass

# def test_guarded_divide_negative_numbers():
#     """Test division with negative numbers."""
#     # TODO: Test cases like guarded_divide(-10, 2) and guarded_divide(10, -2)
#     pass

# def test_guarded_divide_zero_dividend():
#     """Test that 0 divided by non-zero number works."""
#     # TODO: Test guarded_divide(0, 5) - should this work?
#     pass

# def test_guarded_divide_first_arg_invalid():
#     """Test TypeError when first argument is invalid."""
#     # TODO: Test with invalid first argument
#     pass

# def test_guarded_divide_second_arg_invalid():
#     """Test TypeError when second argument is invalid."""
#     # TODO: Test with invalid second argument
#     pass

# def test_guarded_divide_both_args_invalid():
#     """Test behavior when both arguments are invalid."""
#     # TODO: Which error should be raised first?
#     pass

# def test_guarded_divide_returns_float():
#     """Verify that the return type is always float."""
#     # TODO: Test that integer division returns float (e.g., 5/2 -> 2.5)
#     pass


# End of template
