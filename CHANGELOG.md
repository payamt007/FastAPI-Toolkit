## v0.3.0 (2024-02-20)

### Feat

- Updated ruff settings
- Added Flower for celery
- Added db to celery task
- Activated CORS
- Added websocket
- Added file upload feature
- Add route validation
- First stable release

### Fix

- removed unused annotations
- fixed celery worker error
- fixed typos from pyproject.toml
- fixed migration problem, added alchemy relationships

## v0.1.0 (2024-02-19)

## v0.1.0a0 (2024-02-19)

### Feat

- Added commitizen auto versioning
- altered pre commit
- implemented mypy
- added ruff pre commit and removed isort
- Changed db config
- Added auth with alchemy change
- Added User table and a get user route
- Added basic auth boilerplate

### Fix

- removed async driver in ci/cd
- altered ci-cd to activate in develop
- added protected rout
- changed all db models to sync
- isort

## v0.2.0 (2024-02-19)

### Feat

- First stable release

## v0.1.0a0 (2024-02-19)

### Feat

- Added commitizen auto versioning
- altered pre commit
- implemented mypy
- added ruff pre commit and removed isort
- Changed db config
- Added auth with alchemy change
- Added User table and a get user route
- Added basic auth boilerplate
- Added pre commit
- Used Big app model
- Added foreign key to models
- Updated README.md
- Dynamically loaded db url in alembic.ini
- Added dev github action
- Added volume for postgrsql container
- Added eventlet to celery worker
- Added celery beat
- Ran celery in docker container
- Ran celery in localhost
- Ran test is docker container in FastAPI way
- Runned test with requests lib inside docker
- Runned plain  local test
- added .env.test
- added .env file
- used postgresql
- runned in sqlite mode

### Fix

- removed async driver in ci/cd
- altered ci-cd to activate in develop
- added protected rout
- changed all db models to sync
- isort
- updated description to song model
- rebased main
- Fixed typos in README.md
- changed actions run in main branch
- changed db driver
- changed db env setting
- changed alembic config to localhost
- changed alembic config
- changed alembic for with poetry
- changed alembic for custom action
- changed alembic
- commented waiting for db
- changed actions level
- changed db host in wait for in actions
- changed branch name in action file
- changed ci step
- removed unused files
