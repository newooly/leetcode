# leetcode

Archive of leetcode 

## Setup

create venv: `python3 -m venv .venv`

### github actions

```sh
brew install act
```

Test:
```sh
act pull_request -j ruff -W .github/workflows/ruff.yml
```