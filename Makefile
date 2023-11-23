env:
	rm -Rf env
	python3 -m venv env
	env/bin/pip install -U pip setuptools
	env/bin/pip install poetry
	source env/bin/activate && python -m poetry install

black:
	python -m black --line-length 88 tableau_sql_parser/
	python -m black --line-length 88 tests/

isort:
	isort tableau_sql_parser/
	isort tests/

lint: 
	flake8 --max-line-length 88 tableau_sql_parser/
	flake8 --max-line-length 88 tests/

format: black isort lint
