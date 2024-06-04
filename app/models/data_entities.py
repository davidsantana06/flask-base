from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from typing import List

from app.extensions import database

from .base_entities import DeletableEntity
from .entity_mixins import PopulateMixin


class User(database.Model, DeletableEntity, PopulateMixin, UserMixin):
    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(60), nullable=False)

    @staticmethod
    def save(user: 'User') -> None:
        DeletableEntity.save(user)

    @staticmethod
    def delete(user: 'User') -> None:
        DeletableEntity.delete(user)

    @classmethod
    def find_by_id(cls, id: int) -> 'User':
        return cls._find_first([cls.id == id])

    @classmethod
    def find_by_email(cls, email: str) -> 'User':
        return cls._find_first([cls.email == email])

    @classmethod
    def find_all_by_name(cls, name: str) -> List['User']:
        return cls._find_all([cls.name.icontains(name)])

    def __init__(self, name: str, email: str, password: str) -> None:
        self.name = name
        self.email = email
        self.password = password
