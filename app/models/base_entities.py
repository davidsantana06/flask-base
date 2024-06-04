from flask_sqlalchemy.model import Model
from re import findall
from sqlalchemy import (
    Column, ColumnElement, DateTime, Integer, UnaryExpression,
    and_
)
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql import func
from typing import List

from app.extensions import database


class Entity(Model):
    @declared_attr
    def __tablename__(cls):
        cls_name_words = findall(r'[A-Z][a-z]*', cls.__name__)
        table_name = '_'.join(cls_name_words).lower()
        return table_name

    @staticmethod
    def save(entity: 'Entity') -> None:
        try:
            database.session.add(entity)
            database.session.commit()
        except Exception as e:
            database.session.rollback()
            raise e

    @classmethod
    def _find_first(cls, filter_clauses: List[ColumnElement[bool]]) -> 'Entity':
        return cls.query.filter(and_(*filter_clauses)).first()

    @classmethod
    def _find_all(
        cls, 
        filter_clauses: List[ColumnElement[bool]] = [], 
        order_clauses: List[UnaryExpression] = []
    ) -> List['Entity']:
        query = cls.query.filter(and_(*filter_clauses))

        if order_clauses:
            query = query.order_by(*order_clauses)

        return query.all()


class DeletableEntity(Entity):
    @declared_attr
    def created_at(cls):
        return Column(DateTime, nullable=False, default=func.now())

    @declared_attr
    def updated_at(cls):
        return Column(DateTime, nullable=False, default=func.now())

    @declared_attr
    def status(cls):
        return Column(Integer, nullable=False, default=1)

    @staticmethod
    def delete(entity: 'DeletableEntity') -> None:
        try:
            entity.status = 0
            database.session.add(entity)
            database.session.commit()
        except Exception as e:
            database.session.rollback()
            raise e

    @classmethod
    def _find_first(
        cls, 
        filter_clauses: List[ColumnElement[bool]]
    ) -> 'DeletableEntity':
        return super()._find_first([*filter_clauses, cls.status == 1])

    @classmethod
    def _find_all(
        cls, 
        filter_clauses: List[ColumnElement[bool]] = [], 
        order_clauses: List[UnaryExpression] = []
    ) -> List['DeletableEntity']:
        return super()._find_all([*filter_clauses, cls.status == 1], order_clauses)
