env:
	uv sync

format:
	uvx ruff check . --fix
