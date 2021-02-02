unit:
	python -m unittest discover -s tests/unit/ -p "*_test.py" -v

api:
	python -m unittest discover -s tests/api/ -p "*_test.py" -v

e2e:
	behave -v