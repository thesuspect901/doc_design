from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .orm_models import Base

# SQLite database
DATABASE_URL = "sqlite:///discord.db"

# створення engine
engine = create_engine(DATABASE_URL, echo=False)

# фабрика сесій
SessionLocal = sessionmaker(bind=engine)


def init_db():
    """
    Створює всі таблиці в БД
    """
    Base.metadata.create_all(engine)