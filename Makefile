


.PHONY: test clean coverage


all: test


test:
	nosetests -v


coverage:
	rm -f .coverage
	nosetests -v --with-coverage --cover-package=marver --cover-inclusive


clean:
	rm -f .coverage
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
