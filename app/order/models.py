from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Column, Integer


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(30))
