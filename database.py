from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#postgresql://username:password@localhost:port/database_name
POSTGRES_CONNECTION_URL = """postgresql://postgres:password123@localhost:5432/cs_explorer_db"""

engine = create_engine(POSTGRES_CONNECTION_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()