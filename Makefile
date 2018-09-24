install:
	flit install --python `which python`

test:
	python -m pytest -vv --cov hor2vec/ --cov-report html --cov-report term
