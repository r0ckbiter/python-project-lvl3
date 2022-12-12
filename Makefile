page-loader:
	poetry run page-loader

install:
	poetry install

lint:
	poetry run flake8 page_loader

test:
	poetry run pytest

build:
	poetry build

package-install:
	python3 -m pip install dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl

test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml