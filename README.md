# LeetCode

A personal archive of LeetCode solutions and practice problems.

## Setup

Create and activate a Python virtual environment:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

## Tooling

This repository uses a small set of local development tools.

### Homebrew dependencies

```sh
brew install act   # run GitHub Actions locally
brew install just  # project command runner
```

### Justfile

Common project commands are defined in the `justfile`, including linting, formatting, and executing LeetCode test files.

Example usage:

```sh
just check       # check lint and formatting
just fix         # fix lint and formatting
just algorithms  # run all tests in algorithms/
```
