# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import os

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}", pool_recycle=3600)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String)
    content = Column(String)


async def save_chats(role, msg):
    session = SessionLocal()
    try:
        new_chat = Chat(role=role, content=msg)
        session.add(new_chat)
        session.commit()
    finally:
        session.close()

async def get_job_categories(id: int):
    with engine.connect() as connection:
        id += 1
        query = text("SELECT * FROM jobs WHERE id = :id")
        result = connection.execute(query, {'id': id})
        rows = result.fetchall()
        print(rows)
        return {"job": rows[0][1], "category": rows[0][2]}

async def get_chats():
    session = SessionLocal()
    try:
        chats = session.query(Chat).all()
        return chats
    finally:
        session.close()