import sqlalchemy as sa
import sqlalchemy.orm as orm

import config
from database.db_modelbase import SQLBase

con_str = f"postgresql+psycopg2://{config.DB_USER}:{config.DB_PASS}" \
          f"@{config.DB_HOST}:{config.DOCKER_PORT}/{config.DB_NAME}"

engine = sa.create_engine(con_str)
factory = orm.sessionmaker(bind=engine)


def db_connection():
    # noinspection PyUnresolvedReferences
    from database.db_models import Time, Status
    SQLBase.metadata.create_all(bind=engine)
