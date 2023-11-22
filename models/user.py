#!/usr/bin/env python3
"""
    User Module
"""
import hashlib
from models.base import Base


class User(Base):
    """
        User class
    """

    def __init__(self, *args: list, **kwargs: dict):
        """
            Initialize a user instance
            :param args:
            :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email')
        self._password = kwargs.get('password')
        self.firstname = kwargs.get('first_name')
        self.lastname = kwargs.get('last_name')

    def __str__(self) -> str:
        return f"User(id={self.id}, email={self.email}, name={self.display_name()})"
    @property
    def password(self) -> str:
        """
            Getter for the password
            :return:
        """
        return self._password

    @password.setter
    def password(self, pwd: str):
        """
            Setter for new password, encrypts in SHA256
            :param pwd:
            :return:
        """
        if pwd is None or type(pwd) is not str:
            self._password = None
        else:
            self._password = hashlib.sha256(pwd.encode()).hexdigest().lower()



    def display_name(self) -> str:
        """
        Display Username based on email/firstname/lastname
        :return:
        """
        if self.email is None and self.firstname is None \
            and self.lastname is None:
            return ''
        if self.firstname is None and self.lastname is None:
            return '{}'.format(self.email)
        if self.firstname is None:
            return '{}'.format(self.lastname)
        if self.lastname is None:
            return '{}'.format(self.firstname)
        else:
            return '{} {}'.format(self.firstname, self.lastname)
