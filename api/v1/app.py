#!/usr/bin/env python3
"""
    Route Module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r'/api/v1/*': {'origins': '*'}})


@app.errorhandler(401)
def unauthorized_error(error) -> str:
    """
        Request Unauthorized handler
        :param error:
        :return: JSON{"error": "Unauthorized"}
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_error(error) -> str:
    """
        Request Forbidden error handler
        :param error:
        :return: JSON{"error": "Forbidden"}
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error) -> str:
    """
        Request Not found error handler
        :param error:
        :return: JSON{"error": "Unauthorized"}
    """
    return jsonify({"error": "Not Found"}), 404


if __name__ == '__main__':
    host = getenv('API_HOST', '0.0.0.0')
    port = getenv('API_PORT', 5001)
    app.run(host=host, port=port, debug=True)
