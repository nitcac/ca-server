import os


def get_db_setting():
    DATABASE = {
        'dbms': 'postgresql',
        'driver': 'psycopg2',
        # 'name': os.environ['DATABASE_NAME'],
        # 'host': os.environ['DATABASE_HOST'],
        # 'port': os.environ['DATABASE_PORT'],
        # 'user': os.environ['DATABASE_USER'],
        # 'password': os.environ['DATABASE_PASSWORD']
    }

    db_keys = (
        ('DATABASE_NAME', 'name'),
        ('DATABASE_HOST', 'host'),
        ('DATABASE_PORT', 'port'),
        ('DATABASE_USER', 'user'),
        ('DATABASE_PASSWORD', 'password')
    )

    for (envkey, dictkey) in db_keys:
        if envkey in os.environ:
            DATABASE[dictkey] = os.environ[envkey]

    return DATABASE

DEBUG = True