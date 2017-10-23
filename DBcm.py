import MySQLdb

class UseDatabase:

    def __init__(self, config):
        self.config = config

    def __enter__(self):
        self.conn = self.config
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace):
        self.conn.commit()
        self.cursor.close()
