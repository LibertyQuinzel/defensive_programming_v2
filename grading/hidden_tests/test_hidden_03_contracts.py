import importlib.util
from pathlib import Path
import pytest

# Load student's skeleton
skel_path = Path(__file__).parents[2] / "topics" / "03-design-by-contract" / "skeleton.py"
spec = importlib.util.spec_from_file_location("hidden_03_skel", skel_path)
skeleton = importlib.util.module_from_spec(spec)
spec.loader.exec_module(skeleton)


def test_reciprocal_precision():
    r = skeleton.reciprocal(3)
    assert abs(r - 1/3) < 1e-12


def test_reciprocal_negative():
    r = skeleton.reciprocal(-4)
    assert abs(r + 0.25) < 1e-12
