from sqlalchemy import create_engine
from sqlalchemy.exc import DBAPIError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ..config import get_settings

url_object = f'postgresql+psycopg2://{get_settings().db_user}:{get_settings().db_password}@{get_settings().db_host}:{get_settings().db_port}/{get_settings().db_name}'

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
