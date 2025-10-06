"""Enhanced autograder: runs pytest for assignment tests and writes detailed JSON results.

This autograder runs pytest against the course topics and provides:
- Detailed error messages with hints for common issues
- Per-topic breakdown of test results
- Guidance for next steps when tests fail
"""
import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).parent
RESULT_FILE = ROOT / "autograder_result.json"


def parse_pytest_output(output: str) -> Dict[str, any]:
    """Parse pytest output to extract detailed information about test results."""
    lines = output.split('\n')
    
    # Count test results
    passed = failed = errors = skipped = 0
    failed_tests = []
    
    for line in lines:
        if '::' in line and ('PASSED' in line or 'FAILED' in line or 'ERROR' in line):
            if 'PASSED' in line:
                passed += 1
            elif 'FAILED' in line:
                failed += 1
                # Extract test name
                test_name = line.split('::')[-1].split()[0]
                failed_tests.append(test_name)
            elif 'ERROR' in line:
                errors += 1
        elif 'skipped' in line.lower():
            skipped += 1
    
    return {
        'passed': passed,
        'failed': failed,
        'errors': errors,
        'skipped': skipped,
        'failed_tests': failed_tests
    }


def get_helpful_hints(stderr: str, failed_tests: List[str]) -> List[str]:
    """Provide helpful hints based on common error patterns."""
    hints = []
    
    # Common import issues
    if "ModuleNotFoundError" in stderr or "ImportError" in stderr:
        hints.append("💡 Import Issue: Make sure PYTHONPATH is set correctly:")
        hints.append("   export PYTHONPATH=$(pwd):$PYTHONPATH")
        hints.append("   Or install in editable mode: pip install -e .")
    
    # No tests collected
    if "no tests collected" in stderr.lower():
        hints.append("💡 No Tests Found: Check that you're running from the correct directory")
        hints.append("   and that test files start with 'test_'")
    
    # NotImplementedError suggests students haven't implemented functions yet
    if "NotImplementedError" in stderr:
        hints.append("💡 Implementation Needed: Some functions still raise NotImplementedError")
        hints.append("   Check skeleton.py files and implement the required functions")
    
    # TypeError often indicates type validation issues
    if "TypeError" in stderr and failed_tests:
        hints.append("💡 Type Validation: Consider these common issues:")
        hints.append("   - Are you checking for bool before int? (bool is a subclass of int)")
        hints.append("   - Are you validating input types with isinstance()?")
        hints.append("   - Are you handling NaN/infinity values?")
    
    # ValueError often indicates business logic issues
    if "ValueError" in stderr and failed_tests:
        hints.append("💡 Value Validation: Check these common issues:")
        hints.append("   - Division by zero checks")
        hints.append("   - Empty string handling")
        hints.append("   - Range validation for numeric inputs")
    
    if not hints:
        hints.append("💡 Check the error messages above for specific guidance")
        hints.append("   Review the assignment documentation for requirements")
    
    return hints


def generate_success_message(stats: Dict[str, any]) -> List[str]:
    """Generate encouraging message for successful test runs."""
    messages = []
    
    if stats['passed'] > 0:
        messages.append(f"🎉 Great work! {stats['passed']} tests passed")
    
    if stats['failed'] == 0 and stats['errors'] == 0:
        messages.append("✅ All tests are passing - you're ready to submit!")
        messages.append("💡 Next steps:")
        messages.append("   - Run style check: flake8 defensive_programming_v2 --max-line-length=100")
        messages.append("   - Review your code for clarity and comments")
        messages.append("   - Make sure you've completed all TODO items")
    else:
        messages.append("🔄 Keep going - you're making progress!")
    
    return messages


def run() -> int:
    """Run the autograder and generate detailed feedback."""
    print("🔍 Running Defensive Programming Course Autograder...")
    print("=" * 60)
    
    # Run pytest with verbose output
    cmd = [
        sys.executable, "-m", "pytest", 
        "topics/",
        "-v", "--tb=short", "--maxfail=10"
    ]
    
    proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    
    # Parse results
    stats = parse_pytest_output(proc.stdout)
    hints = get_helpful_hints(proc.stderr, stats['failed_tests'])
    
    # Create detailed result
    result = {
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "summary": {
            "tests_passed": stats['passed'],
            "tests_failed": stats['failed'],
            "tests_errors": stats['errors'],
            "tests_skipped": stats['skipped'],
            "failed_test_names": stats['failed_tests']
        },
        "hints": hints,
        "success": proc.returncode == 0
    }
    
    # Write detailed JSON result
    RESULT_FILE.write_text(json.dumps(result, indent=2))
    
    # Print human-readable summary
    print("\n📊 Test Summary:")
    print(f"   ✅ Passed: {stats['passed']}")
    print(f"   ❌ Failed: {stats['failed']}")
    print(f"   ⚠️  Errors: {stats['errors']}")
    print(f"   ⏭️  Skipped: {stats['skipped']}")
    
    if proc.returncode == 0:
        success_messages = generate_success_message(stats)
        for msg in success_messages:
            print(msg)
    else:
        print("\n💡 Helpful Hints:")
        for hint in hints:
            print(f"   {hint}")
        
        if stats['failed_tests']:
            print("\n❌ Failed Tests:")
            for test in stats['failed_tests'][:5]:  # Show first 5 failed tests
                print(f"   - {test}")
            if len(stats['failed_tests']) > 5:
                print(f"   ... and {len(stats['failed_tests']) - 5} more")
    
    print(f"\n📄 Detailed results saved to: {RESULT_FILE}")
    print("=" * 60)
    
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(run())
