activate:
	pipenv shell

run:
	export ENV=development && uvicorn main:app --reload --host 0.0.0.0

clean-run:
	export ENV=development && rm -f database.db && uvicorn main:app --reload --host 0.0.0.0

generate_requirements_txt:
	pipenv requirements --dev  > requirements.txt

test:
	export ENV=testing && pytest tests -s -x -vv
	rm -f test.db

test-coverage:
	docker-compose up -d
	sleep 4
	./wait-for-postgres.sh
	export ENV=testing && pytest tests -x -vv --cov=. --cov-report=term-missing
	docker-compose down

install:
	pipenv install --dev

format:
	black . 

lint:
	pylint *.py
