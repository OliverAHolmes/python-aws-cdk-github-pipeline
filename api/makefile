activate:
	pipenv shell

run:
	export ENV=development && uvicorn main:app --reload --host 0.0.0.0

generate_requirements_txt:
	pipenv requirements --dev  > requirements.txt

test:
	export ENV=testing && pytest tests -s -x -vv

test-coverage:
	export ENV=testing && pytest tests -x -vv --cov=. --cov-report=term-missing

install:
	pipenv install --dev

format:
	black . 

lint:
	pylint *.py
