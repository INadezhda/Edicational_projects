import requests
import sqlalchemy
import json
import psycopg2
from sqlalchemy.orm import sessionmaker
from model import create_tables, shop, book, sale, publisher, stock
from pprint import pprint
from sqlalchemy import or_
name_db = ' '
login = ' '
parol = ' '

DSN = f'postgresql://{login}:{parol}@localhost:5432/{name_db}'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()
autopep8 --in-place --aggress
with open('tests_data.json', 'r') as f:
    data = json.load(f)
    # дабавляем данные
    for record in data:
        model = {
            'publisher': publisher,
            'shop': shop,
            'book': book,
            'stock': stock,
            'sale': sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()

    # запрос

    name_publish = input("Введите название  или идентификатор издательства : ")
    if name_publish.isnumeric() == True:
        # subq = session.query(book).join(publisher.book).filter((or_(publisher.id == name_publish,publisher.name==name_publish))).subquery()
        subq = session.query(book).join(publisher.book).filter(
            or_(publisher.name == name_publish, publisher.id == str(name_publish))).subquery()
        for i in session.query(shop).join(stock.shop).join(
                subq, stock.id_book == subq.c.id):
            print(i)
    else:
        subq = session.query(book).join(publisher.book).filter(
            publisher.name == name_publish.title()).subquery()
        for i in session.query(shop).join(stock.shop).join(
                subq, stock.id_book == subq.c.id):
            print(i)
    session.close()
