# Makefile for Defensive Programming Course
# Provides convenient commands for students and instructors

.PHONY: help setup test test-verbose lint format clean install-dev check-all

help:  ## Show this help message
	@echo "Defensive Programming Course - Development Commands"
	@echo "=================================================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup:  ## Set up development environment
	@echo "🚀 Setting up development environment..."
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt
	.venv/bin/pip install -e .
	@echo "✅ Setup complete! Activate with: source .venv/bin/activate"

install-dev:  ## Install development dependencies
	pip install -e ".[dev]"

test:  ## Run all tests
	@echo "🧪 Running tests..."
	python -m pytest defensive_programming_v2/topics/ -q

test-verbose:  ## Run tests with verbose output
	@echo "🧪 Running tests (verbose)..."
	python -m pytest defensive_programming_v2/topics/ -v

test-topic:  ## Run tests for specific topic (e.g., make test-topic TOPIC=01-guard-clauses)
	@echo "🧪 Running tests for topic: $(TOPIC)"
	python -m pytest defensive_programming_v2/topics/$(TOPIC)/ -v

autograder:  ## Run the course autograder
	@echo "🔍 Running autograder..."
	python -m defensive_programming_v2.autograder

lint:  ## Check code style with flake8
	@echo "🧹 Checking code style..."
	flake8 defensive_programming_v2 --max-line-length=100 --exclude=.venv

format:  ## Format code with black (if available)
	@echo "🎨 Formatting code..."
	@if command -v black >/dev/null 2>&1; then \
		black defensive_programming_v2 --line-length=100; \
	else \
		echo "⚠️  Black not installed. Install with: pip install black"; \
	fi

type-check:  ## Run type checking with mypy (if available)
	@echo "🔍 Type checking..."
	@if command -v mypy >/dev/null 2>&1; then \
		mypy defensive_programming_v2 --ignore-missing-imports; \
	else \
		echo "⚠️  Mypy not installed. Install with: pip install mypy"; \
	fi

check-all: lint type-check test  ## Run all quality checks

clean:  ## Clean up generated files
	@echo "🧹 Cleaning up..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type f -name "autograder_result.json" -delete
	rm -rf build/ dist/

student-workflow:  ## Demonstrate the student workflow for a topic
	@echo "📚 Student Workflow Demo:"
	@echo "1. cd defensive_programming_v2/topics/00-intro"
	@echo "2. python starter.py"
	@echo "3. Edit test_template_for_students_00_intro.py"
	@echo "4. pytest test_template_for_students_00_intro.py -v"
	@echo "5. Edit skeleton.py"
	@echo "6. pytest test_template_for_students_00_intro.py -v"
	@echo "7. pytest instructor_tests/ -v"

# Instructor commands
instructor-tests:  ## Run all instructor Part A tests
	@echo "🎓 Running instructor tests..."
	python defensive_programming_v2/topics/run_partA_tests.py

hidden-tests:  ## Run hidden CI tests
	@echo "🔒 Running hidden tests..."
	python -m pytest defensive_programming_v2/grading/hidden_tests/ -v

release-check: check-all hidden-tests  ## Full release validation