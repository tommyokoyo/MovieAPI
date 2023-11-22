#!/usr/bin/env python3
"""
    Session Authentication Module
"""
from api.v1.auth.auth import Auth
from storage.users import User

class SessionAuth(Auth):
    """
        Responsible for session authorization and validation
        inherits from auth class
    """
