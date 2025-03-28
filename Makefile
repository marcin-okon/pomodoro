all:
	pip install -e . --force-reinstall

format:
	ruff format ./
	ruff check --fix

deps:
	pip-compile --resolver=backtracking -v -r ./requirements/requirements.in 
	pip install -r ./requirements/requirements.txt


