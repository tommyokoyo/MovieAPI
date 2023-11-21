#!/usr/bin/env python3
"""
    Token creation and authentication module
"""
from datetime import datetime, timedelta, timezone
import jwt


class TokenAuth:
    """
        Responsible for Token creation and authorization
    """
    secret_word = 'my_secret'

    def generate_token(self, user_id: str):
        """
            Generates a user token based on user id
            :param user_id:
            :return: JWT token
        """
        message = {
            'iss': 'Open-hub',
            'User': '{}'.format(user_id),
            'iat': datetime.now(timezone.utc),
            'exp': datetime.now(timezone.utc) + timedelta(minutes=5),
        }

        return jwt.encode(message, self.secret_word, algorithm='HS256')

    def decode_token(self, token: str):
        """
            Decodes the token and returns the token values
            :param token:
            :return:
        """
        return jwt.decode(token, self.secret_word, algorithms=['HS256'], do_time_check=True)

    def create_token(self, user_id: str = None) -> str:
        """
            Creates a session token for User
            :param user_id:
            :return: Token
        """
        if user_id is None or type(user_id) is not str:
            return None
        else:
            token_id: str = self.generate_token(user_id)
            return token_id

    def token_validity(self, token: str) -> bool:
        decode_token = self.decode_token(token)
        expiration = decode_token.get('exp', 0)
        expiration_datetime = datetime.utcfromtimestamp(expiration).replace(tzinfo=timezone.utc)
        return datetime.utcnow().replace(tzinfo=timezone.utc) < expiration_datetime
