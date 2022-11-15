# Exercise 2
from sqlite3.dbapi2 import Connection
from typing import List


class DataAccessObject:
    def __init__(self, connection: Connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def __del__(self):
        self.connection.close()

    def create(self, name: str, password: str, email: str) -> None:
        pass

    def read(self) -> List:
        pass

    def update(self, name: str, **kwargs) -> None:
        pass

    def delete(self, name: str) -> None:
        pass


class UserDAO(DataAccessObject):
    def __init__(self, connection: Connection):
        super().__init__(connection)

    def create(self, name: str, password: str, email: str):
        # create query string
        query = f"INSERT INTO users (name, password, email) VALUES ('{name}', '{password}', '{email}')"

        # execute query
        self.cursor.execute(query)
        self.connection.commit()

    def read(self):
        result = self.cursor.execute("SELECT * FROM users")
        return result.fetchall()

    def update(self, name: str, **kwargs):
        # retrieve values from keyword args
        password = kwargs.get('password', '')
        email = kwargs.get('email', '')

        # create strings for setting each parameter
        name_param = f"name = '{name}'" if name else ""
        password_param = f"password = '{password}'" if password else ""
        email_param = f"email = '{email}'" if email else ""

        # concatenate the strings
        params = [name_param, password_param, email_param]
        params_string = ",".join([param for param in params if param])

        # create query string
        query = "UPDATE users " \
                f"SET {params_string} " \
                f"WHERE name = '{name}'"

        # execute query
        self.cursor.execute(query)
        self.connection.commit()

    def delete(self, name: str):
        query = "DELETE FROM users " \
                f"WHERE name = '{name}'"

        self.cursor.execute(query)
        self.connection.commit()
