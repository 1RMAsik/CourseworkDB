from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Departments(Base):
    __tablename__ = 'departments'

    departmentid = Column(Integer, primary_key=True)
    departmentname = Column(String)
    photourl = Column(String)

class Products(Base):
    __tablename__ = 'products'

    productid = Column(Integer, primary_key=True)
    productname = Column(String)
    price = Column(Integer)
    photourl = Column(String)

class Sales(Base):
    __tablename__ = 'sales'

    saleid = Column(Integer, primary_key=True)
    productid = Column(Integer)
    sellerid = Column(Integer)
    departmentid = Column(Integer)
    saledate = Column(String)
    quantity = Column(Integer)
    totalamount = Column(Integer)