import importlib.util
from pathlib import Path
import pytest
import os

# Load student's skeleton
skel_path = Path(__file__).parents[2] / "topics" / "04-decorators" / "skeleton.py"
spec = importlib.util.spec_from_file_location("hidden_04_skel", skel_path)
skeleton = importlib.util.module_from_spec(spec)
spec.loader.exec_module(skeleton)


def test_announce_wrap_and_quiet(monkeypatch, capsys):
    @skeleton.announce
    def add(a, b):
        return a + b

    # Normal call prints
    res = add(2, 2)
    assert res == 4
    out = capsys.readouterr().out
    assert "Calling add" in out

    # QUIET should suppress printing
    monkeypatch.setenv("QUIET", "1")
    res2 = add(3, 3)
    assert res2 == 6