from datetime import datetime

from sqlalchemy import Integer, Column, String, Boolean, DateTime, Double
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    username = Column(String(32), nullable=True)
    first_name = Column(String(64))
    last_name = Column(String(64), nullable=True)
    language = Column(String(2), default='ru')
    is_admin = Column(Boolean, default=False)
    balance = Column(Double, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
