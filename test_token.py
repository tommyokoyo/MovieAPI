#!/usr/bin/env python3
"""
    Token auth test file
"""
from api.v1.auth.token_auth import TokenAuth

print('---JWT test run---')
tokenauth = TokenAuth()
token_given = tokenauth.create_token('9a52dfbc-40d7-4802-87f8-80c7bfa5a22d')
decoded_token = tokenauth.decode_token(token_given)
token_valid = tokenauth.token_validity(token_given)

print(f'The RSA key is: {None}\nsigning key: {tokenauth.secret_word}\nJWT_token: {token_given}\ndecoded_token: {decoded_token}\nToken validity: {token_valid}')
print(f'User id: {decoded_token.get("User")}')

print('---JWT test run completed---')
