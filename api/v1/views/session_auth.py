#!/usr/bin/env python3
"""
    Handles routes for all session authentication
"""
from models.user import User
from flask import request, jsonify
from api.v1.views import app_views


@app_views.route('/auth/login', methods=['POST'], strict_slashes=False)
def login():
    """
        POST /auth/login
        :return: session token
    """
    user_email = request.json.get('email')
    user_password = request.json.get('password')

    if user_email is None or user_email == '':
        return jsonify({'error': 'email missing'}), 400
    elif user_password is None or user_password == '':
        return jsonify({'error': 'Password missing'}), 400
    else:
        User.load_from_file()
        found_user = User.search({'email': user_email})

        if not found_user:
            return jsonify({'error': 'No user found for this email'}), 404
        else:
            for user in current_user:
                if user.is_valid_password(user_password):
                    from api.v1.auth.token_auth import TokenAuth
                    session_token = TokenAuth.create_token(user.id)
                    response = jsonify(user.to_json())
                    response.set_cookie('session-token', session_token)
                    return response, 200
                else:
                    return jsonify({'error': 'Wrong password'}), 401
