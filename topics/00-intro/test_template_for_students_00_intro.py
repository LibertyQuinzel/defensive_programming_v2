"""Student test template for Topic 00 - Intro.

This template is a starting point for students to write tests-first for the
`greet` function implemented in `skeleton.py`.

Run from the repository root:

    PYTHONPATH=. pytest -q defensive_programming_v2/topics/00-intro/test_template_for_students.py

Edit and extend these tests as part of your TDD workflow.
"""

from pathlib import Path
import importlib.util
import pytest

skel_path = Path(__file__).parent / "skeleton.py"
spec = importlib.util.spec_from_file_location("topic00_skeleton", skel_path)
skeleton = importlib.util.module_from_spec(spec)
spec.loader.exec_module(skeleton)


def test_validated_greet_happy():
    # Part 1: tests-first exercise for the implemented helper
    assert skeleton.validated_greet("Alice") == "Hello, Alice"


def test_validated_greet_empty():
    assert skeleton.validated_greet("") == "Hello, stranger"


def test_validated_greet_type_error():
    with pytest.raises(TypeError):
        skeleton.validated_greet(123)


#########################################################################
# Part 2: Implementation-first exercise (instructor-provided tests exist for
# `greet`. Students implement the code to satisfy those tests.)
#########################################################################


def test_greet_happy():
    """Happy path: simple greeting returns the expected string."""
    assert skeleton.greet("Alice") == "Hello, Alice"


def test_greet_empty():
    """Empty name returns the friendly default."""
    assert skeleton.greet("") == "Hello, stranger"


def test_greet_type_error():
    """Non-string names should raise TypeError."""
    with pytest.raises(TypeError):
        skeleton.greet(123)
