black:
	python -m black --line-length 88 src/

isort:
	isort src/

lint: 
	flake8 --max-line-length 88 src/

format: black isort lint
