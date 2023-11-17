from sqlalchemy import create_engine, URL
from sqlalchemy.exc import DBAPIError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import get_settings

url_object = URL.create(
    "postgresql+psycopg2",
    username = get_settings().db_user,
    password = get_settings().db_password,
    host = get_settings().db_host,
    port = get_settings().db_port,
    database = get_settings().db_name,
)

engine = create_engine(
    url_object
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

def get_db_session():
    session = SessionLocal()
    try:
        yield session
    except DBAPIError:
        session.rollback()
    finally:
        session.close()

Base = declarative_base()
