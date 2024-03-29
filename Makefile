.MAIN: build

.PHONY: build
build:
	rm -rf ./dist
	python -m build


.PHONY: install
install: 
	pip install -r requirements.txt


.PHONY: publish
publish: install build
	python -m twine upload --skip-existing --repository pypi dist/*