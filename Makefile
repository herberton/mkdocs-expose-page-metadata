.MAIN: build

.PHONY: build
build: 
	python -m build


.PHONY: install
install: 
	pip install -r requirements.txt


.PHONY: publish
publish: install build
	python -m twine upload --repository pypi dist/*