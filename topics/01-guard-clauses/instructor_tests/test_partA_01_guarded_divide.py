"""Instructor tests (Part A) for guard-clauses.

These tests assert the defensive behavior students must implement in `skeleton.guarded_divide`.
"""
from pathlib import Path
import importlib.util
import pytest

# Load the sibling skeleton.py as a module so pytest can run this file directly
skel_path = Path(__file__).parent.parent / "skeleton.py"
spec = importlib.util.spec_from_file_location(f"topics_skeleton_{Path(__file__).parent.name}", skel_path)
skeleton = importlib.util.module_from_spec(spec)
spec.loader.exec_module(skeleton)


def test_guarded_divide_happy():
    assert skeleton.guarded_divide(10, 2) == 5


def test_guarded_divide_type_error():
    with pytest.raises(TypeError):
        skeleton.guarded_divide("10", 2)


def test_guarded_divide_divide_by_zero():
    with pytest.raises(ValueError):
        skeleton.guarded_divide(1, 0)
