from sqlalchemy import create_engine

from server.setting import DATABASE, DEBUG


db_uri = f'{DATABASE["dbms"]}+{DATABASE["driver"]}://{DATABASE["user"]}:{DATABASE["password"]}@{DATABASE["host"]}:{DATABASE["port"]}/mydatabase'
engine = create_engine(db_uri, echo=DEBUG)
