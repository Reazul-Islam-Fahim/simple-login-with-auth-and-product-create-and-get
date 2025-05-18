from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="user")

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=True)
    quantity = Column(Integer, nullable=True)
