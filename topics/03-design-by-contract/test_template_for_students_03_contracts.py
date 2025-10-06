"""Student test template for Topic 03 - Design by Contract.

Template for testing `reciprocal(x)` in `skeleton.py`.

Run from the repository root:

    PYTHONPATH=. pytest -q defensive_programming_v2/topics/03-design-by-contract/test_template_for_students.py
"""

from pathlib import Path
import importlib.util
import pytest

skel_path = Path(__file__).parent / "skeleton.py"
spec = importlib.util.spec_from_file_location("topic03_contracts", skel_path)
skeleton = importlib.util.module_from_spec(spec)
spec.loader.exec_module(skeleton)


def test_validated_reciprocal_happy():
    assert skeleton.validated_reciprocal(2) == 0.5


def test_validated_reciprocal_type_error():
    with pytest.raises(TypeError):
        skeleton.validated_reciprocal("2")


def test_validated_reciprocal_zero_raises():
    with pytest.raises(ValueError):
        skeleton.validated_reciprocal(0)


#########################################################################
# Part 2: Implementation-first exercise (instructor-provided tests exist for
# `reciprocal`. Students implement the code to satisfy those tests.)
#########################################################################


def test_reciprocal_happy():
    """Happy path: reciprocal returns expected value."""
    assert abs(skeleton.reciprocal(2) - 0.5) < 1e-9


def test_reciprocal_type_error():
    with pytest.raises(TypeError):
        skeleton.reciprocal("not-a-number")


def test_reciprocal_zero():
    with pytest.raises(ValueError):
        skeleton.reciprocal(0)
