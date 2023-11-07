#!/usr/bin/env python3
"""
    This file contains functions for high level view of the
    API and also perform high level functions
    Note: Be careful executing some functions as it will overwrite
          the existing data or the whole storage area
"""

from utils.database_connection import Base, engine
from sqlalchemy.exc import SQLAlchemyError


def is_database_alive() -> bool:
    """
        This function Checks the database connection
        :return: Boolean value
    """
    try:
        conn = engine.connect()
        conn.close()
        return True
    except ConnectionError as error:
        print(f'Connection Error: {error}')
        return False


def create_tables() -> bool:
    """
        This function is used to create the database schema
        Note: calling this function overwrites the whole database
        :return: Boolean value
    """
    if is_database_alive():
        try:
            Base.metadata.create_all(engine)
            return True
        except SQLAlchemyError as error:
            print(f'An error occurred: {error}')
            return False
