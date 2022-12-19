import datetime

from sqlalchemy.exc import IntegrityError
import sqlalchemy.orm

from database.db_models import Time
from database.db_session import engine, factory


class DBSaver:
    def __enter__(self):
        self.connection = engine.connect()
        self.session: sqlalchemy.orm.Session = factory()
        return self

    def save(self, user_id):
        self.session.begin()
        current_time = Time(
            last_time=datetime.datetime.now(),
            user_id=user_id
        )
        self.session.add(current_time)
        try:
            self.session.commit()
        except IntegrityError:
            self.session.rollback()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
