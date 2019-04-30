import os


_default_db_data = {
    'user':  'hamada', 
    'password':  '', 
    'host':  'db', 
    'port':  '5432', 
    'name':  'CADB'
}

def get_db_setting(defaults=_default_db_data):
    DATABASE = {
        'dbms': 'postgresql',
        'driver': 'psycopg2',
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
        else:
            DATABASE[dictkey] = defaults[dictkey]

    return DATABASE

DEBUG = True

SECRET_KEY = os.environ['SECRET_KEY']