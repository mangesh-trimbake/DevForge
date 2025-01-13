from db_base import db, Base_Model

# Product model
class Product(Base_Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price}, description={self.description})"
