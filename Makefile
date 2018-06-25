install:
	flit install --python `which python`

test:
	python -m pytest --cov hor2vec/  --cov-report html --cov-report term
