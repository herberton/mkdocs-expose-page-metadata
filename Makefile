.MAIN: build

.PHONY: build
build: 
	python -m build


.PHONY: install
install: 
	pip install -r requirements.txt