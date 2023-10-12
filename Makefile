# requirements
install_requirements:
	python -m pip install --upgrade pip
	pip install pip-tools
	pip install -r app/requirements.txt

add_requirements:
	pip-compile app/requirements.in

# migrations
docker_migrate:
	docker-compose run backend python manage.py migrate

migrate:
	python manage.py makemigrations
	python manage.py migrate



# docker
docker_setup:
	docker volume create uploadimageapi_dbdata
	docker-compose build

enter_backend:
	docker-compose exec -it backend bash


docker_test:
	docker-compose run backend py.test --disable-warnings $(test_path)
