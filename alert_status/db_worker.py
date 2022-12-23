import psycopg2

import config


class DBWorker:
    def __enter__(self):
        self.conn = psycopg2.connect(user=config.DB_USER,
                                     password=config.DB_PASS,
                                     host=config.DB_HOST,
                                     port=config.DB_LOCAL_PORT,
                                     database=config.DB_NAME)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        return self

    def get_status(self):
        self.cursor.execute(f"SELECT status "
                            f"FROM alert_status "
                            f"ORDER BY pk DESC;")
        results = self.cursor.fetchone()
        return results[0]

    def insert_status(self, status):
        self.cursor.execute(f"INSERT INTO alert_status (status) "
                            f"VALUES ('{status}');")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
