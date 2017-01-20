init:
	pip3 install -r requirements.txt

run:
	python3 -m powerball.main

test:
	python3 -m pytest tests -v
