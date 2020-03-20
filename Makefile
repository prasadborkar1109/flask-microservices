VIRTUALENV = $(shell which virtualenv)

venv:
	$(VIRTUALENV) venv

launch:
	. env/bin/activate; python services/users.py
	. env/bin/activate; python services/bookings.py
	. env/bin/activate; python services/movies.py
	. env/bin/activate; python services/showtimes.py