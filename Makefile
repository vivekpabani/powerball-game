init:
	pip3 install -r requirements.txt

test:
	python3 -m pytest tests -v
