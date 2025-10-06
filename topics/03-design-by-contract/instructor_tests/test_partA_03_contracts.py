"""Instructor tests (Part A) for design-by-contract (reciprocal) moved to instructor_tests."""
from pathlib import Path
import importlib.util
import pytest

# Load sibling skeleton.py as a module
skel_path = Path(__file__).parent.parent / "skeleton.py"
spec = importlib.util.spec_from_file_location(f"topics_skeleton_{Path(__file__).parent.parent.name}", skel_path)
skeleton = importlib.util.module_from_spec(spec)
spec.loader.exec_module(skeleton)


def test_reciprocal_happy():
    assert abs(skeleton.reciprocal(2) - 0.5) < 1e-9


def test_reciprocal_type_error():
    with pytest.raises(TypeError):
        skeleton.reciprocal("not-a-number")


def test_reciprocal_zero():
    with pytest.raises(ValueError):
        skeleton.reciprocal(0)
