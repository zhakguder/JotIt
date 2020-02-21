env:
	pipenv shell
mongod:
	systemctl start mongod
flask:
	FLASK_APP=$PWD/jotIt/http/api/endpoints.py FLASK_ENV=development pipenv run python -m flask run --port 4433
