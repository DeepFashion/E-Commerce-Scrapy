from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings


DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))


def create_deals_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class Deals(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "images"

    id = Column(Integer, primary_key=True)
    images = Column('images', String)
    mainImage = Column('mainImage', String)
    apparelURL = Column('apparelURL', String)
    title = Column('title', String)
    rating = Column('rating', String)
    finalPrice = Column('finalPrice', String)
    initialPrice = Column('initialPrice', String)
    discount = Column('discount', String)
    # link = Column('link', String, nullable=True)
    # location = Column('location', String, nullable=True)
    # original_price = Column('original_price', String, nullable=True)
    # price = Column('price', String, nullable=True)
    # end_date = Column('end_date', DateTime, nullable=True)