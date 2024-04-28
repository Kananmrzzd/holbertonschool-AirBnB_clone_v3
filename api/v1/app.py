#!/usr/bin/python3
"""API"""
from flask import Flask, Blueprint
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found_error(error):
    return {"error": "Not found"}, 404


@app.teardown_appcontext
def close_db(exc):
    storage.close()


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", '0.0.0.0')
    port = getenv("HBNB_API_PORT", '5000')
    app.run(host=host, port=port, threaded=True)
