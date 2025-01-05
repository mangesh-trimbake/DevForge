from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, func

# Create the declarative base
Base = declarative_base()

# Define a reusable base model
class BaseModel(Base):
    __abstract__ = True  # This ensures the class is not mapped to a table directly

    id = Column(Integer, primary_key=True, autoincrement=True)  # Common ID column
    created_at = Column(DateTime, default=func.now(), nullable=False)  # Auto timestamp
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    def save(self, session):
        """
        Save the instance to the database.
        """
        session.add(self)
        session.commit()

    def delete(self, session):
        """
        Delete the instance from the database.
        """
        session.delete(self)
        session.commit()

    @classmethod
    def get(cls, session, id):
        """
        Retrieve an instance by primary key.
        """
        return session.query(cls).get(id)

    @classmethod
    def all(cls, session):
        """
        Retrieve all instances of the model.
        """
        return session.query(cls).all()

# Example of extending the base class for a specific model
class User(BaseModel):
    __tablename__ = 'users'
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
