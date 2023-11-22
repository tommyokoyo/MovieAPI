from sqlalchemy import Column, Integer, String
from utils.database_connection import Base, session
import uuid
from datetime import datetime
import hashlib

TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S'


class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    def __init__(self, firstname, lastname, email, password):
        self.id = str(uuid.uuid4())
        self.first_name = firstname
        self.last_name = lastname
        self.email = email
        self.password = password

    def is_valid_password(self, pwd: str) -> bool:
        """
            Validates a password
            :param pwd:
            :return:
        """
        if pwd is None or type(pwd) is not str:
            return False
        if self.password is None:
            return False
        # pwd_e = pwd.encode()
        # return hashlib.sha256(pwd_e).hexdigest().lower() == self.password
        return pwd == self.password

    def get_user(self, email):
        return session.query(User).filter_by(email=email).first()

    def to_json(self, for_serialization: bool = False) -> dict:
        """
            Convert the object to a JSON dictionary
            :param for_serialization:
            :return: Dict
        """
        result = {}

        for key, value in self.__dict__.items():
            if not for_serialization and key[0] == '_':
                continue
            if type(value) is datetime:
                result[key] = value.strftime(TIMESTAMP_FORMAT)
            else:
                result[key] = value

        return result
