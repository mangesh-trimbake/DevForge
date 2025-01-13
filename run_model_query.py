
from models import * 



def create_db():
    # Create the database tables
    db.create_all()


def run_query():
    products = Product.query.all()


if __name__ == '__main__':
    # Manually bind the engine
    DATABASE_URI = 'sqlite:///products.db'  # Use the same URI as in app.py
    configure_db(uri=DATABASE_URI)
    create_db()

    run_query()
