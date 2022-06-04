import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_DIR = '../soccer_database'
print(f'os.path.abspath(db_dir): {str(os.path.abspath(DB_DIR))}')
SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.path.abspath(DB_DIR)}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()