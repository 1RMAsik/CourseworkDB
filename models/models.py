from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Departments(Base):
    __tablename__ = 'departments'

    departmentid = Column(Integer, primary_key=True)
    departmentname = Column(String)
    photourl = Column(String)
