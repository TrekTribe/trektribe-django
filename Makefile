requirements:
	pip install -U pipenv
	pipenv sync --dev

style-fix:
	isort .
	black .
	flake8

style-check:
	pylint --load-plugins pylint_django --django-settings-module=website.settings_test --errors-only --recursive=y .
	isort --check-only .
	black --check --diff .
	flake8

tests:
	pytest
	coverage html
	coverage xml
