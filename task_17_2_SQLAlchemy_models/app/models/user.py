from module_17_Resource_libraries_2.task_17_2_SQLAlchemy_models.app.backend.db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from module_17_Resource_libraries_2.task_17_2_SQLAlchemy_models.app.models import *


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship('Task', back_populates='user')


print(CreateTable(User.__table__))