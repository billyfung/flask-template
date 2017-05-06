ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

develop:
    @virtualenv $(ROOT_DIR)/.venv
    @$(ROOT_DIR)/.venv/bin/pip install -U -r requirements.txt
    @$(ROOT_DIR)/.venv/bin/pip install -e .

clean:
    @rm -rf `find . -name __pycache__`
    @rm -f `find . -type f -name '*.py[co]' `
    @rm -f `find . -type f -name '#*#' `
    @rm -f `find . -type f -name '*.orig' `
    @rm -f `find . -type f -name '*.rej' `

install:
    @pip install -U pip
    @pip install -Ur requirements.txt

.PHONY: all build test
