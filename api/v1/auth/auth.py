#!/usr/bin/env python3
"""
    This class manages the API authentication
"""
from typing import List
from flask import request


class Auth:
    """
        Authentication Class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            Defines the routes that don't need authentication
            :param path: request path
            :param excluded_paths:
            :return:
        """
        if path is not None or excluded_paths is None:
            return True
        elif path[-1] is '/':
            if path in excluded_paths:
                return False
        else:
            path += '/'
            if path in excluded_paths:
                return False

        return True

    def session_cookie(self, request=None) -> str:
        """
            Gets the cookie value from the request
            :param request:
            :return:
        """
        if request is not None:
            return request.cookies.get('session-token')
        else:
            return None

    def current_user(self, request=None):
        return None
