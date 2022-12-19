import sqlalchemy as sa

from database.db_modelbase import SQLBase


class Time(SQLBase):
    __tablename__ = 'times'

    pk = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    last_time = sa.Column(sa.DateTime)
    user_id = sa.Column(sa.String)


class Status(SQLBase):
    __tablename__ = 'statuses'

    pk = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    last_status = sa.Column(sa.String)
    last_time = sa.Column(sa.String)
    user_id = sa.Column(sa.String)
