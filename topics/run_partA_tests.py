"""Lightweight runner for Part A instructor tests.

Usage: python3 topics/run_partA_tests.py

This runner loads each `test_partA_*.py` file under topics/* and executes any
callable starting with `test_`. It sets the module package so relative imports
inside the test files (e.g., `from . import skeleton`) work correctly.

This is intentionally minimal and not a replacement for pytest; it's for
convenience in environments without pytest installed.
"""
import sys
import traceback
from pathlib import Path
import importlib.util


ROOT = Path(__file__).parent
# Ensure the repository root (parent of topics) is on sys.path so `import topics` works
import sys
repo_root = str(ROOT.parent)
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)


def load_module_from_path(path: Path):
    # derive package name topics.<folder>
    rel = path.relative_to(ROOT)
    parts = rel.parts
    # parts like ('00-intro', 'test_partA_00_intro.py')
    pkg = f"topics.{parts[0]}"
    mod_name = f"{pkg}.{path.stem}"
    spec = importlib.util.spec_from_file_location(mod_name, path)
    module = importlib.util.module_from_spec(spec)
    # set package so relative imports inside test file work
    module.__package__ = pkg
    sys.modules[mod_name] = module
    try:
        spec.loader.exec_module(module)
    except Exception:
        print(f"ERROR importing {path}:\n")
        traceback.print_exc()
        return None
    return module


def run_tests():
    # Search recursively for test_partA_*.py to include instructor_tests/ subfolders
    test_files = sorted(ROOT.rglob("test_partA_*.py"))
    total = 0
    failed = 0
    import subprocess

    for tf in test_files:
        print(f"Running pytest on {tf}")
        # Run pytest for the single file so fixtures are available
        cmd = [sys.executable, "-m", "pytest", "-q", str(tf)]
        res = subprocess.run(cmd)
        # pytest exit code 0 -> success; non-zero -> failure
        if res.returncode == 0:
            print(f"  PASS {tf}")
        else:
            print(f"  FAIL {tf} (pytest exit code {res.returncode})")
            failed += 1
        # We don't count individual tests here; pytest prints per-file summary.

    print("\nSummary: total tests=", total, "failed=", failed)
    return failed == 0


if __name__ == "__main__":
    ok = run_tests()
    sys.exit(0 if ok else 1)
