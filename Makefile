# loading and exporting all env vars from .env file automatically
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

APP_NAME="petlove-case-flask"
IMAGE_NAME="petlove-case-flask"
VERSION="latest"
MAIN_ENTRYPOINT="src/main.py"


################################
# COMMANDS TO RUN LOCALLY
################################

local/install:
	poetry install

local/tests:
	poetry run pytest -s --cov-report=html --cov-report xml:coverage.xml --cov-fail-under=90 --cov-report=term --cov .

local/lint:
	poetry run ruff check .

local/lint/fix:
	poetry run ruff . --fix

local/run:
	poetry run python -m flask --app run.py run

############################################
# COMMANDS TO RUN USING DOCKER (RECOMMENDED)
############################################

docker/install: generate-default-env-file
	docker-compose build ${APP_NAME}

docker/up:
	docker-compose up -d

docker/down:
	docker-compose down --remove-orphans

docker/test:
	docker-compose run ${APP_NAME} poetry run pytest --cov-report=html --cov-report xml:coverage.xml --cov-fail-under=90 --cov-report=term --cov .

docker/lint:
	docker-compose run ${APP_NAME} poetry run ruff check .

docker/lint/fix:
	docker-compose run ${APP_NAME} poetry run ruff . --fix

docker/run:
	docker-compose run ${APP_NAME} poetry run python ${MAIN_ENTRYPOINT}

####################################
# DOCKER IMAGE COMMANDS
####################################

docker/image/build:
	docker build . --target production -t app

docker/image/push:
	docker push app

##################
# HEPFUL COMMANDS
##################

generate-default-env-file:
	@if [ ! -f .env ]; then cp env.template .env; fi;
