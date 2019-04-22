import os


DEBUG = True

DATABASE = {
    'dbms': 'postgresql',
    'driver': 'psycopg2',
    'name': 'cadb',
    'host': os.environ['DATABASE_HOST'],
    'port': os.environ['DATABASE_PORT'],
    'user': os.environ['DATABASE_USER'],
    'password': os.environ['DATABASE_PASSWORD']
}