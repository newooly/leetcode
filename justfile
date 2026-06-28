algorithms:
    python3 -m unittest discover -s algorithms -p "*.py"

check:
    # Check Python code formatting and linting issues
    python3 -m ruff check .
    python3 -m ruff format --check .

fix:
    # Fix Python code formatting and linting issues
    python3 -m ruff check --fix .
    python3 -m ruff format .

actions:
    # Run the ruff workflow using act
    act pull_request -j ruff -W .github/workflows/ruff.yml --container-architecture linux/amd64
