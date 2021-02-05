unit:
	python -m unittest discover -s tests/unit/ -p "*_test.py" -v

api:
	python -m unittest discover -s tests/api/ -p "*_test.py" -v

e2e:
	behave -v

build:
	docker build . -t yurireeis/just-tests:latest

run:
	docker run yurireeis/just-tests:latest $(ARGS)
