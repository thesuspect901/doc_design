from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class UserORM(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    is_registered = Column(Integer)


class ChatORM(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class MessageORM(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)

    text = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey("users.id"))
    chat_id = Column(Integer, ForeignKey("chats.id"))