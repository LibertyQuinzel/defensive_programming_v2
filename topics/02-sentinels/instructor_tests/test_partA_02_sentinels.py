"""Instructor tests (Part A) for sentinels (moved to instructor_tests).
"""
from pathlib import Path
import importlib.util
import pytest

# Load sibling skeleton.py as a module
skel_path = Path(__file__).parent.parent / "skeleton.py"
spec = importlib.util.spec_from_file_location(f"topics_skeleton_{Path(__file__).parent.parent.name}", skel_path)
skeleton = importlib.util.module_from_spec(spec)
spec.loader.exec_module(skeleton)


def test_choose_value_omitted():
    # omitted value should return fallback
    assert skeleton.choose_value(fallback=5) == 5


def test_choose_value_explicit_none():
    # explicit None value should return None (not fallback)
    assert skeleton.choose_value(None, fallback=5) is None
