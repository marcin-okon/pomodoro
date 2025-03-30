all:
	pip install -e . --force-reinstall

format:
	ruff format .
	ruff check --fix

check:
	ruff check .
	mypy .

deps:
	pip-compile --resolver=backtracking -v -r ./requirements/requirements.in 
	pip install -r ./requirements/requirements.txt

test:
	pytest ./tests

