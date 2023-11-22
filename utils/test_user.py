#!/usr/bin/env python3
"""
    User module test
"""
from storage.users import User
from utils.database_connection import session

# filter by email
user_email = 'okoyotommy@gmail.com'
user = session.query(User).filter_by(email=user_email).first()
print(f'User id: {user.id}\nFirst name: {user.first_name}\nlast name: {user.last_name}\nemail: {user.email}')

