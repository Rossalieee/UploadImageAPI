# Upload Image API
## Environment
### Initial setup
You will need to have at least Python 3.10 and [Docker](https://www.docker.com/) installed.

You also need to have [Make](https://www.gnu.org/software/make/) installed. \
If you are on Windows you need to install [Chocolatey](https://chocolatey.org/install) and run this command: `choco install make`.

### Docker
After cloning this repo you need to first run `make docker_setup` to build a Docker image.
If you want to start Docker you need to run: `docker-compose up` .

### Django
Run `make enter_backend` to enter backend Docker container.
Then you need to run migrations: `make migrate`.

To access [Django administration panel](http://localhost:8000/admin) you first need to create
a superuser for yourself.
Run `python manage.py createsuperuser` and fill the form.

Visit [Django administration panel](http://localhost:8000/admin) and log in. Then you can select your account tier in users administration panel.

### Pytest
If you want to run tests enter backend Docker container using command `make enter_backend` and run `make test`.

### URLs
http://localhost:8000/admin/ \
http://localhost:8000/api/images/ \
http://localhost:8000/api/expiring-links/ 