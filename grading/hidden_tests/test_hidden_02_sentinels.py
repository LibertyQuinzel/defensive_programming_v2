import importlib.util
from pathlib import Path
import pytest

# Load student's skeleton
skel_path = Path(__file__).parents[2] / "topics" / "02-sentinels" / "skeleton.py"
spec = importlib.util.spec_from_file_location("hidden_02_skel", skel_path)
skeleton = importlib.util.module_from_spec(spec)
spec.loader.exec_module(skeleton)


def test_choose_value_identity():
    sentinel = object()
    # explicit None should remain None
    assert skeleton.choose_value(None, fallback=sentinel) is None
    # omitted should return fallback
    assert skeleton.choose_value(fallback=sentinel) is sentinel
