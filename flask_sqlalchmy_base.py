from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column, Integer, DateTime, func

# Initialize SQLAlchemy without an app
db = SQLAlchemy()

# Monkey patch the `db` instance to add the `configure` method
def configure_sqlalchemy(self, uri=None):
    """
    Dynamically bind the engine to the db instance if not already bound.
    """
    if not hasattr(self, 'engine') and uri:
        self.engine = create_engine(uri)
        self.session = scoped_session(sessionmaker(bind=self.engine))

# Add the configure method to `db`
db.configure = configure_sqlalchemy

@as_declarative()
class Base_Model:
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
