"""Instructor tests (Part A) for Intro (moved into instructor_tests).

These are the canonical tests students should satisfy by implementing
``greet`` in the skeleton (Part B).
"""
from pathlib import Path
import importlib.util
import pytest

# Load the sibling skeleton.py as a module so pytest can run this file directly
skel_path = Path(__file__).parent.parent / "skeleton.py"
spec = importlib.util.spec_from_file_location(f"topics_skeleton_{Path(__file__).parent.parent.name}", skel_path)
skeleton = importlib.util.module_from_spec(spec)
spec.loader.exec_module(skeleton)


def test_greet_regular():
    assert skeleton.greet("Alice") == "Hello, Alice"


def test_greet_empty():
    assert skeleton.greet("") == "Hello, stranger"


def test_greet_type_error():
    with pytest.raises(TypeError):
        skeleton.greet(123)
