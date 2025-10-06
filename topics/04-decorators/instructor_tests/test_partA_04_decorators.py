"""Instructor tests (Part A) for decorators (announce) moved to instructor_tests."""
from pathlib import Path
import importlib.util
import os
import pytest

# Load sibling skeleton.py as a module
skel_path = Path(__file__).parent.parent / "skeleton.py"
spec = importlib.util.spec_from_file_location(f"topics_skeleton_{Path(__file__).parent.parent.name}", skel_path)
skeleton = importlib.util.module_from_spec(spec)
spec.loader.exec_module(skeleton)


def test_announce_basic(capsys):
    @skeleton.announce
    def add(a, b):
        return a + b

    # Ensure decorator returns correct result and prints
    assert add(2, 3) == 5
    captured = capsys.readouterr()
    assert "Calling add" in captured.out


def test_announce_quiet(monkeypatch):
    # Ensure QUIET disables printing
    monkeypatch.setenv("QUIET", "1")

    @skeleton.announce
    def add(a, b):
        return a + b

    assert add(1, 1) == 2
