# Student Guide: Defensive Programming Course

Welcome to the Defensive Programming course! This guide will help you navigate the learning materials and complete the assignments successfully.

## 📚 What You'll Learn

By the end of this course, you'll master:
- **Guard clauses**: Early validation to prevent errors
- **Sentinel objects**: Elegant alternatives to exceptions
- **Design by contract**: Pre/post-conditions for robust code
- **Decorators**: Reusable validation patterns
- **Test-driven development (TDD)**: Writing tests before code

## 🚀 Quick Start

### 1. Setup Your Environment
Run the automated setup script:
```bash
./setup_student.sh
```

Or set up manually:
```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -e .

# Set PYTHONPATH
export PYTHONPATH=$(pwd):$PYTHONPATH
```

### 2. Verify Your Setup
```bash
# Test basic functionality
python -m pytest defensive_programming_v2/topics/00-intro/test_template_for_students_00_intro.py -v

# Run the autograder
python -m defensive_programming_v2.autograder
```

## 📖 Learning Workflow

### For Each Topic (00-intro through 04-decorators):

#### Step 1: Read and Understand
1. **Read the assignment**: `topics/XX-name/assignment.md`
   - Contains learning objectives
   - Explains concepts with examples
   - Lists acceptance criteria

2. **Explore examples**: Run `topics/XX-name/starter.py`
   - Shows working implementations
   - Demonstrates key concepts
   - Safe to experiment with

#### Step 2: Write Tests (Tests-First Approach)
3. **Open the test template**: `topics/XX-name/test_template_for_students_XX_name.py`
   - Contains basic test stubs
   - Add your own test cases
   - Focus on edge cases and error conditions

4. **Run your tests** (they should fail initially):
   ```bash
   pytest -v topics/XX-name/test_template_for_students_XX_name.py
   ```

#### Step 3: Implement Code
5. **Edit the skeleton**: `topics/XX-name/skeleton.py`
   - Implement functions to pass your tests
   - Follow the TDD cycle: Red → Green → Refactor

6. **Run tests iteratively**:
   ```bash
   # Run your tests
   pytest -v topics/XX-name/test_template_for_students_XX_name.py
   
   # Run instructor tests (the "spec")
   pytest -v topics/XX-name/instructor_tests/
   ```

#### Step 4: Validate and Submit
7. **Run all topic tests**:
   ```bash
   pytest -v topics/XX-name/
   ```

8. **Check with autograder**:
   ```bash
   python -m defensive_programming_v2.autograder
   ```

## 🎯 Success Tips

### Understanding the Exercise Types

**Tests-First Exercises** (Part 1):
- You write tests for provided implementations
- Focus on discovering edge cases
- Learn to think like a tester

**Implementation-First Exercises** (Part 2):
- Instructor provides tests (the specification)
- You implement code to satisfy the tests
- Focus on meeting requirements

### Common Patterns to Remember

1. **Type Checking**: Always validate input types
   ```python
   if not isinstance(value, (int, float)):
       raise TypeError("Expected numeric type")
   ```

2. **Boolean Rejection**: In Python, `bool` subclasses `int`
   ```python
   # This catches booleans too!
   if isinstance(value, bool):
       raise TypeError("Boolean values not allowed")
   ```

3. **Early Returns**: Use guard clauses for cleaner code
   ```python
   def process(data):
       if not data:
           return "No data"
       if len(data) < 2:
           return "Insufficient data"
       # Main logic here...
   ```

### Debugging Tips

1. **Import Issues**: Ensure `PYTHONPATH` is set correctly
2. **Test Failures**: Read error messages carefully - they contain hints
3. **Type Errors**: Check your type annotations and isinstance() calls
4. **Logic Errors**: Use print statements or debugger to trace execution

## 📊 Assessment and Grading

### How You're Evaluated
- **Functionality**: Do your implementations pass the tests?
- **Code Quality**: Is your code readable and well-structured?
- **Test Quality**: Do your tests cover edge cases?
- **Following Instructions**: Did you meet the assignment requirements?

### Running the Full Test Suite
```bash
# All instructor tests
python defensive_programming_v2/topics/run_partA_tests.py

# Hidden CI tests
pytest -v defensive_programming_v2/grading/hidden_tests/

# Style check
flake8 defensive_programming_v2 --max-line-length=100
```

## 🆘 Getting Help

### When You're Stuck
1. **Re-read the assignment**: Often contains the answer
2. **Check the examples**: Similar patterns are demonstrated
3. **Read test error messages**: They provide specific feedback
4. **Review the starter code**: Shows the expected approach

### Common Mistakes to Avoid
- Forgetting to validate input types
- Not handling edge cases (empty strings, zero, negative numbers)
- Ignoring boolean edge cases
- Not following the exact function signatures
- Skipping the TDD workflow

### Troubleshooting Checklist
- [ ] Virtual environment activated?
- [ ] PYTHONPATH set correctly?
- [ ] All dependencies installed?
- [ ] Running from the correct directory?
- [ ] Following the exact test requirements?

## 🎓 Beyond the Course

### Next Steps
- Explore static type checking with `mypy`
- Learn about property-based testing with `hypothesis`
- Study design patterns and clean code principles
- Practice with larger codebases

### Additional Resources
- Python's built-in `isinstance()` and `type()` functions
- `functools.wraps` for preserving metadata in decorators
- `math.isfinite()` for robust numeric validation
- PEP 484 (Type Hints) for modern Python typing

---

**Remember**: Defensive programming is about anticipating problems before they occur. Think like a skeptical user of your own code!

Good luck, and happy coding! 🐍✨