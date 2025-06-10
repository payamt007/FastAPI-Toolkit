venv:
	uv venv -p python3.13 .venv

install-req:
	uv pip install -r pyproject.toml

install-all-req:
	uv pip install -r pyproject.toml --extra dev --extra test

sync-req:
	uv pip sync pyproject.toml

install-dev:
	uv pip install -r pyproject.toml --extra dev

lint:
	pre-commit run --all-files
