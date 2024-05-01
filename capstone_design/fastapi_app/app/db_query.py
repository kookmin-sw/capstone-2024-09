# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
import os

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

print(db_user)
print(db_password)
print(db_host)
print(db_name)

engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")

async def save_chats(role, msg):
    session = SessionLocal()
    try:
        metadata = MetaData()
        chats = Table('chats', metadata, autoload_with=engine)
        query = chats.insert().values(role=role, content=msg)
        session.execute(query)
        session.commit()
    finally:
        session.close()

async def get_job_categories(id):
    with engine.connect() as connection:
        query = text("SELECT * FROM jobs WHERE id = :id")
        result = connection.execute(query, id=id)
        for row in result:
            print(dict(row))
        return {"data": [dict(row) for row in result]}