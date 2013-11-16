from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, Table

from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    logs = relationship("Log", uselist=True)

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True)
    codes = Column(Text, nullable=False)
    values = Column(Text, nullable=False)
    types = Column(Text, nullable=False)
    times = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User")

if __name__ == "__main__":
    pass