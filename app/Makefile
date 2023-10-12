# testing
test:
	py.test --disable-warnings $(test_path)

test_verbose:
	py.test --disable-warnings $(test_path) -vv

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate
