from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column, Integer, DateTime, func

# Initialize SQLAlchemy without an app
db = SQLAlchemy()

@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
