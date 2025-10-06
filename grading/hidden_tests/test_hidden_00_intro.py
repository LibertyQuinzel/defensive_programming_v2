import importlib.util
from pathlib import Path
import pytest

# Load the student's skeleton
skel_path = Path(__file__).parents[2] / "topics" / "00-intro" / "skeleton.py"
spec = importlib.util.spec_from_file_location("hidden_00_skel", skel_path)
skeleton = importlib.util.module_from_spec(spec)
spec.loader.exec_module(skeleton)


def test_greet_unicode():
    # Accept names with unicode characters
    assert skeleton.greet("Ćharlie") == "Hello, Ćharlie"


def test_greet_type_error():
    with pytest.raises(TypeError):
        skeleton.greet(None)
