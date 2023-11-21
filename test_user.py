#!/usr/bin/env python3
"""
    User module test
"""
from models import User

# create a sample test user
firstname = 'tommy'
lastname = 'okoyo'
user_email = 'tommyokoyo@gmail.com'
user_password = 'password'
user = User()
user.firstname = firstname
user.lastname = lastname
user.email = user_email
user.password = user_password
print("New user: {} / {}".format(user.id, user.display_name()))
user.save()
