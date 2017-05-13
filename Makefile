.PHONY: all clean clean-build setup

TMPRUN=ah/auctionhouse

all:
	python3 $(TMPRUN)/server.py /home/christian/AH/ah

clean:
	find . -name "*.pyc" -exec rm --force {} +
	find . -name "*.pyo" -exec rm --force {} +

clean-build:
	rm -rf build/
	rm -rf dist/

setup:
	python3 setup.py sdist
