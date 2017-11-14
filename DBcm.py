import MySQLdb


class ConnectionError(Exception):
    pass


class CredentialError(Exception):
    pass


class SQLError(Exception):
    pass


class UseDatabase:

    def __init__(self, config):
        self.config = config

    def __enter__(self):
        try:
            self.conn = self.config
            self.cursor = self.conn.cursor()
            return self.cursor
        except MySQLdb.InterfaceError as err:
            raise ConnectionError(err)
        except MySQLdb.ProgrammingError as err:
            raise CredentialError(err)

    def __exit__(self, exc_type, exc_value, exc_trace):
        self.conn.commit()
        self.cursor.close()
        if exc_type is MySQLdb.ProgrammingError:
            raise SQLError(exc_value)
        elif exc_type:
            raise exc_type(exc_value)
