# Upload Image API
API that allows any user to upload an image in PNG or JPG format. Users are able to list their images. There are three builtin account tiers: Basic, Premium and Enterprise:
* users that have "Basic" plan after uploading an image get:
  * a link to a thumbnail that's 200px in height
* users that have "Premium" plan get:
  * a link to a thumbnail that's 200px in height
  * a link to a thumbnail that's 400px in height
  * a link to the originally uploaded image
* users that have "Enterprise" plan get
  * a link to a thumbnail that's 200px in height
  * a link to a thumbnail that's 400px in height
  * a link to the originally uploaded image
  * ability to fetch an expiring link to the image (the link expires after a given number of seconds (the user can specify any number between 300 and 30000))

Apart from the builtin tiers, admins are able to create arbitrary tiers with the following things configurable:
* arbitrary thumbnail sizes
* presence of the link to the originally uploaded file
* ability to generate expiring links

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
