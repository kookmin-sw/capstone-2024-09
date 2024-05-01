# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

DATABASE_URL = "mysql+pymysql://root:root@mysql_db/consult_data?charset=utf8mb4"
engine = create_engine(DATABASE_URL, poolclass=NullPool)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


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
    session = SessionLocal()
    try:
        metadata = MetaData()
        jobs = Table('jobs', metadata, autoload_with=engine)
        query = select(jobs).where(jobs.c.id == id)
        result = session.execute(query)
        row = result.fetchone()
        if row is None:
            return {"error": "No chat with id 1 found"}
        job = row[1].encode('utf-8').decode('utf-8')
        job_category = row[2].encode('utf-8').decode('utf-8')
        return {"job": job, "category": job_category}
    finally:
        session.close()