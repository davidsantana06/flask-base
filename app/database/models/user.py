from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from typing import List

from app.extensions import database
from app.lib.database import PopulateMixin

from ..inheritable.model import Model


Users = List['User']


class User(database.Model, Model, UserMixin, PopulateMixin):
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(String(30), nullable=False)
    password = Column(String(60), nullable=False)

    @staticmethod
    def save(user: 'User') -> None:
        Model.save(user)

    @staticmethod
    def delete(user: 'User') -> None:
        Model.delete(user)

    @classmethod
    def find_all(cls) -> Users:
        return cls.query.order_by(User.name).all()

    @classmethod
    def find_first_by_id(cls, id: int) -> 'User':
        return cls.query.filter(User.id == id).first()

    @classmethod
    def find_first_or_404_by_id(cls, id: int) -> 'User':
        return cls.query.filter(User.id == id).first_or_404()

    def __init__(self, name: str, password: str) -> None:
        self.name = name
        self.password = password
