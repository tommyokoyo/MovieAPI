#!/usr/bin/env python3
"""
    User view module
"""
from api.v1.views import app_views
from flask import jsonify
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def view_all_users():
    """
        GET /api/v1/users
        :return: List of all user objects
    """
    all_users = [user.to_json() for user in User.all()]
    return jsonify(all_users)
