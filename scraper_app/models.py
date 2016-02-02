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


class FlipkartProducts(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "flipkartdata"

    id = Column(Integer, primary_key=True)
    images = Column('images', String)
    mainImage = Column('mainImage', String)
    apparelURL = Column('apparelURL', String)
    title = Column('title', String)
    rating = Column('rating', String)
    finalPrice = Column('finalPrice', String)
    initialPrice = Column('initialPrice', String)
    discount = Column('discount', String)
    requestURL = Column('requestURL', String)
    category = Column('category', String)


class JabongProducts(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "jabongdata"

    id = Column(Integer, primary_key=True)
    product_link = Column('product_link', String)
    image_320 = Column('image_320', String)
    image_500 = Column('image_500', String)
    image_768 = Column('image_768', String)
    image_1024 = Column('image_1024', String)
    image_1280 = Column('image_1280', String)
    brand = Column('brand', String)
    name = Column('name', String)
    previous_price = Column('previous_price', String)
    standard_price = Column('standard_price', String)
    discount = Column('discount', String)
    requestURL = Column('requestURL', String)
    category = Column('category', String)


class PolyvoreProducts(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "polyvoredata"

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    numlikes=Column('numlikes', String)
    requestURL = Column('requestURL', String)
    productName=Column('productName', String)
    productURL=Column('productURL', String)
    productPrice=Column('productPrice', String)
    productImage=Column('productImage', String)
    productNumLikes=Column('productNumLikes', String)


class FlipkartPageProducts(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "flipkartpagedata"
    id = Column(Integer, primary_key=True)
    keyFeatures = Column('keyFeatures', String)
    specs = Column('specs', String)
    rating = Column('rating', String)
    descriptionText= Column('descriptionText', String)
    requestURL=Column('requestURL', String)
class JabongPageProducts(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "jabongpagedata"
    id = Column(Integer, primary_key=True)
    brand = Column('brand', String)
    productTitle = Column('productTitle', String)
    desc1 = Column('desc1', String)
    desc2= Column('desc2', String)
    requestURL=Column('requestURL', String)

