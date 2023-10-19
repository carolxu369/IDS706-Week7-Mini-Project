setup:
	pip install -r requirements.txt

test:
	python -m unittest discover

run:
	python my_tool/main.py

clean:
	find . -type f -name "*.pyc" -delete