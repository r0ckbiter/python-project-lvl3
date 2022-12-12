build:
	poetry build

page-loader:
	poetry run page-loader

package-install:
	python3 -m pip install dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 page_loader

test:
	poetry run pytest --cov=page_loader tests --cov-report xml