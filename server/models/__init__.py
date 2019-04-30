from server.setting import get_db_setting, DEBUG

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


def get_db_uri():
    db = get_db_setting()
    return '{dbms}+{driver}://{user}:{password}@{host}:{port}/{name}'.format(
        dbms=db['dbms'], driver=db['driver'], user=db['user'], 
        password=db['password'], host=db['host'], port=db['port'], name=db['name']
    )

engine = create_engine(get_db_uri(), echo=DEBUG)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class SessionManager:
    def __enter__(self):
        self.session = Session()
        return self.session

    def __exit__(self, ex_type, ex_value, trace):
        self.session.close()
