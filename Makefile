install:
	flit install --python `which python`

test:
	python -m pytest tests/
