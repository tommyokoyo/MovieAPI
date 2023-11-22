#!/usr/bin/env python3
"""
    Handles routes for all session authentication
"""
from storage.users import User
from flask import request, jsonify, abort
from api.v1.views import app_views
from utils.database_connection import session


@app_views.route('/auth/signin', methods=['POST'], strict_slashes=False)
def signin():
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
        try:
            user = session.query(User).filter_by(email=user_email).first()

            if not user:
                return jsonify({'error': 'No user found for this email'}), 404
            else:
                if user.is_valid_password(user_password):
                    from api.v1.auth.token_auth import TokenAuth
                    session_token = TokenAuth().create_token(user.id)
                    if session_token is None:
                        return jsonify({'error': 'No session token'})

                    response = jsonify(user.to_json())
                    response.set_cookie('session-token', str(session_token))
                    return response, 200
                else:
                    return jsonify({'error': 'Wrong password'}), 401

        except LookupError:
            print('Error encountered')
            abort(500)


@app_views.route('/auth/signup', methods=['POST'], strict_slashes=False)
def signup():
    """
        POST /auth/signup
        :return: session token
    """
    first_name = request.json.get('firstname')
    last_name = request.json.get('lastname')
    user_email = request.json.get('email')
    user_password = request.json.get('password')

    if first_name is None or first_name == '':
        return jsonify({'error': 'email missing'}), 400
    elif last_name is None or last_name == '':
        return jsonify({'error': 'Password missing'}), 400
    if user_email is None or user_email == '':
        return jsonify({'error': 'email missing'}), 400
    elif user_password is None or user_password == '':
        return jsonify({'error': 'Password missing'}), 400

    existing_user = session.query(User).filter_by(email=user_email).first()
    if existing_user:
        return jsonify({'error': 'Email is already registered'}), 400

    new_user = User(
        firstname=first_name,
        lastname=last_name,
        email=user_email,
        password=user_password
    )

    session.add(new_user)
    session.commit()

    return jsonify({'Success': 'User created successfully'})
