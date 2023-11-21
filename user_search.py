#!/usr/bin/env python3
"""
    User module test
"""
from models.user import User

# search for user using email
user_email = 'okoyotommy@gmail.com'
found_users = User.search({'email': user_email})
print(found_users)
for user in found_users:
    print(user.id)
