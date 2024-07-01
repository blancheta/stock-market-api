from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(30))
