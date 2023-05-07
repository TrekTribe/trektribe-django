# Trek Tribe


## Project setup

- Clone the repository and enter in its directory

    ```
    git clone git@github.com:dennybiasiolli/trektribe.git
    cd trektribe
    ```

- Create a virtual environment for this project (Python 3.10.x suggested)

    ```
    mkdir -p $HOME/.virtualenvs/trektribe
    python -m venv $HOME/.virtualenvs/trektribe
    ```

- Enable the virtual environment (each time you work on the project)

    `source $HOME/.virtualenvs/trektribe/bin/activate`

- Install required dependencies

    ```
    pip install --upgrade pip
    pip install -r requirements_dev.txt
    ```

- Create/update database with migrations

    A SQLite database for debugging is created if not existent,
    PostgreSQL databases must be created before launching this command

    `python manage.py migrate`

- Loading default data (if any)

    `python manage.py loaddata trektribe`

- Create an admin

    `python manage.py createsuperuser`

    and follow instructions on the command line

- Start a local instance of django

    `python manage.py runserver`

- Open admin page

    Open `http://localhost:8000/admin/` from a browser and login with admin credentials


## Local settings

Create a `website/settings_local.py` file with a content like this:

```py
import os

os.environ['DB_ENGINE'] = 'django.db.backends.postgresql'
os.environ['DB_NAME'] = 'database_name'
os.environ['DB_USER'] = 'youruser'
os.environ['DB_PASSWORD'] = ''
os.environ['DB_HOST'] = 'localhost'
os.environ['DB_PORT'] = '5432'

from .settings import *  # noqa
```

And launch `manage.py` commands with

`DJANGO_SETTINGS_MODULE=website.settings_local python manage.py ...`


## Sync project

- Update `main` branch (check for unstaged changes)

    ```
    git checkout main
    git pull
    ```

- Enable the virtual environment (see instructions above in the setup section)

- Update database

    `python manage.py migrate`

## Enabling Git Hooks (optional)

You can create your own git hooks in the `.git/hooks/` directory, or you can use pre-defined hooks with

```sh
# use hooks from `.githooks` directory
git config --local core.hooksPath .githooks/

# use a single hook
ln -sf ../../.githooks/pre-commit .git/hooks/pre-commit
ln -sf ../../.githooks/pre-push .git/hooks/pre-push
```

This will add a pre-commit hook checking for `make style` before each commit,
and a pre-push hook checking for `make test` before each push.

You can skip hooks when committing/pushing with `--no-verify`
according to [git commit man page)](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt--n).


## Test / style with makefile

- `make tests` for testing the whole codebase and providing a coverage report

- `make style-check` check the code style for the entire codebase

- `make style-fix` tries to fix common errors in the codebase


## Environment variables

- `SECRET_KEY`
- `DEBUG`: set to `True`, `true` or `1` to enable debug
- `ALLOWED_HOSTS`
- `CSRF_TRUSTED_ORIGINS`
- `DB_ENGINE`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`
- `ADMIN_BASE_URL`: base url for admin mode, defaults to `admin`
