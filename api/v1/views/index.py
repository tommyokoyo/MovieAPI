#!/usr/bin/env python3
"""
    Index views module
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/', methods=['GET'], strict_slashes=False)
def root_route() -> str:
    """
        GET /api/v1/
        :return: Not Found
    """
    return jsonify({'error': 'Not Mapped'})


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """
        GET /api/v1/status
        :return: The Status of the API
    """
    return jsonify({'status': 'OK'})


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def unauthorized() -> str:
    """
        GET /api/v1/unauthorized
        :return: Raise 401 error
    """
    abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() -> str:
    """
        GET /api/v1/forbidden
        :return: Raise 403 error
    """
    abort(403)
