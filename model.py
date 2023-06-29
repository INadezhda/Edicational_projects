# import sqlalchemy
import sqlalchemy as sq
import requests
from datetime import datetime, time, date
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=50))

    def __str__(self):
        return f'{self.name}'


class book(Base):
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=60))
    id_publisher = sq.Column(
        sq.Integer,
        sq.ForeignKey('publisher.id'),
        nullable=False)
    publisher = relationship("publisher", backref='book')

    def __str__(self):
        return f'{self.title}'


class shop(Base):
    __tablename__ = 'shop'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40))

    def __str__(self):
        return f'{self.name}'


class stock(Base):
    __tablename__ = 'stock'
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    shop = relationship('shop', backref='stock')
    book = relationship("book", backref='stock')

    def __str__(self):
        return f'{self.count},{self.book},{self.shop}'


class sale(Base):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.DateTime, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    stock = relationship('stock', backref='sale')

    def __str__(self):
        return f'{self.date_sale}:{self.count},{self.price},{self.stock}'


def create_tables(engine):
    Base.metadata.create_all(engine)
