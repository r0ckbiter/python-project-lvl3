page-loader:
	poetry run page-loader

install:
	poetry install

lint:
	poetry run flake8 page_loader

build:
	poetry build

package-install:
	python3 -m pip install dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl

test:
	poetry run pytest --cov=page_loader tests --cov-report xml