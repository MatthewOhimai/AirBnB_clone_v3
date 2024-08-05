#!/usr/bin/python3


from models import storage
from models import *
from flask import Flask
from api.v1.views import app_views
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
	"""closes the storage"""
	storage.close()


if __name__ == '__main__':
	app.run(host='HBNB_API_HOST', port='HBNB_API_PORT', threaded=True)
	