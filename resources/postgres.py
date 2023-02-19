from sqlalchemy import create_engine
from contextlib import contextmanager
from dagster import resource
import os


@resource
@contextmanager
def postgres_connection(context):
    ''' Return a Postgres connection. '''

    database_url: str = os.getenv('DATABASE_URL')

    assert database_url is not None, 'DATABASE_URL Environment variable not set.'

    engine = create_engine(database_url)

    with engine.begin() as connection:
        yield connection
