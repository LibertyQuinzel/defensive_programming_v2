import importlib.util
from pathlib import Path
import pytest

# Load student's skeleton
skel_path = Path(__file__).parents[2] / "topics" / "01-guard-clauses" / "skeleton.py"
spec = importlib.util.spec_from_file_location("hidden_01_skel", skel_path)
skeleton = importlib.util.module_from_spec(spec)
spec.loader.exec_module(skeleton)


def test_guarded_divide_negative_and_float():
    assert skeleton.guarded_divide(-10.0, 2) == -5.0
    assert skeleton.guarded_divide(1e12, 2) == 5e11
