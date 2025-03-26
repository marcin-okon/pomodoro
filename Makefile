format:
	ruff format ./src
	ruff check --fix

deps:
	pip-compile --resolver=backtracking -v -r ./requirements/requirements.in 
	pip install -r ./requirements/requirements.txt
