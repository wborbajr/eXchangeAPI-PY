include .env

.PHONY: default server debug test flake8 dkup dkbuild dkstop dkdown dkdownv dkdownrmi dklogs dkimages dkps 

default:
	@echo "Default:"

############################
# Docker
############################

dkup:
	docker-compose -f docker-compose.yml up -d
	
dkbuild:
	docker-compose -f docker-compose.yml --build --force-recreate
	
dkstop:
	# Stop services only
	docker-compose stop

dkdown:
	# Stop and remove containers, networks..
	docker-compose down 

dkdownv: 
	# Down and remove volumes
	docker-compose down --volumes 

dkdownrmi:
	# Down and remove images <all|local>
	docker-compose down --rmi all 

dklogs:
	docker-compose logs -f

dkimages: 
	docker-compose images	

dkps:
	docker-compose ps

############################
# Poetry
############################

server:
	poetry run uvicorn exchangeapi.bootstrap:app --host=$(SERVER_HOST) --port=$(SERVER_PORT) --log-level=info

debug:
	poetry run uvicorn exchangeapi.bootstrap:app --host=$(SERVER_HOST) --port=$(SERVER_PORT) --reload --debug --log-level=debug

test:
	PYTHONPATH=. poetry run pytest tests

coverage:
	poetry run pytest --cov=app tests/

install:
	poetry update
	poetry install

update:
	poetry update

init_db:
	poetry run sh -c "PYTHONPATH=. python ./scripts/init_db.py"

doc:
	poetry run mkdocs serve

build_doc:
	poetry run mkdocs build

build_image:
	poetry run docker build -t beehive3 .

format_code:
	poetry run black .

