import psycopg2

import config


class DBWorker:
    def __enter__(self):
        self.conn = psycopg2.connect(user=config.DB_USER,
                                     password=config.DB_PASS,
                                     host=config.DB_HOST,
                                     port=config.DB_PORT,
                                     database=config.DB_NAME)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        return self

    def get_time(self):
        self.cursor.execute(f"SELECT last_time "
                            f"FROM times "
                            f"WHERE user_id = '{config.USER_ID}' "
                            f"ORDER BY pk DESC;")
        results = self.cursor.fetchone()
        if results:
            return results[0]

    def get_status(self):
        self.cursor.execute(f"SELECT * "
                            f"FROM statuses "
                            f"WHERE user_id = '{config.USER_ID}' "
                            f"ORDER BY pk DESC;")
        results = self.cursor.fetchone()
        return results

    def insert_status(self, status, dt):
        self.cursor.execute('INSERT INTO statuses '
                            '(last_status, last_time, user_id)'
                            'VALUES(%s, %s, %s)', (status, dt, config.USER_ID))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
