#!/usr/bin/python3
<<<<<<< HEAD


from models import storage
from models import *
from flask import Flask
from api.v1.views import app_views
app = Flask(__name__)
=======
"""
app
"""

from flask import Flask, jsonify
from flask_cors import CORS
from os import getenv

from api.v1.views import app_views
from models import storage


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

>>>>>>> ca499d5931e9c613c9f849d99b53b85a705dff64
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
<<<<<<< HEAD
	"""closes the storage"""
	storage.close()


if __name__ == '__main__':
	app.run(host='HBNB_API_HOST', port='HBNB_API_PORT', threaded=True)
	
=======
    """
    teardown function
    """
    storage.close()


@app.errorhandler(404)
def handle_404(exception):
    """
    handles 404 error
    :return: returns 404 json
    """
    data = {
        "error": "Not found"
    }

    resp = jsonify(data)
    resp.status_code = 404

    return(resp)

if __name__ == "__main__":
    app.run(getenv("HBNB_API_HOST"), getenv("HBNB_API_PORT"))
>>>>>>> ca499d5931e9c613c9f849d99b53b85a705dff64
