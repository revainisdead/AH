.PHONY: all clean clean-build setup

TMPRUN=ah/auctionhouse

all:
	python3 $(TMPRUN)/server.py

clean:
	find . -name "*.pyc" -exec rm --force {} +
	find . -name "*.pyo" -exec rm --force {} +
	find . -name "__pycache__" -exec rm --force --recursive {} +
	rm -rf build/
	rm -rf dist/

setup:
	python3 setup.py sdist
