import psycopg2

class DBConnector:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None

    def connect(self):
        self.conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()

    def get_cursor(self):
        if self.conn is None:
            self.connect()
        if self.conn:
            return self.conn.cursor()

    def commit(self):
        if self.conn:
            self.conn.commit()

    def close(self):
        self.disconnect()
