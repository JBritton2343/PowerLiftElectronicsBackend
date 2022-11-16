from sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User (db.Model):
    __tablename__ = 'User'
    
    id = db.Column(db.Integer, primary_key=True)
    fist = db.Column(db.String(25), nullable=False)
    last= db.Column(db.String(25), nullable=False)
    address= db.Column(db.String(250), nullable=False)
    email= db.Column(db.String(120), unique=True, nullable=False)
    password= db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
    def serialize(self):
        return{
            "id":self.id,
            "first": self.fist,
            "last": self.last,
            "address": self.address,
            "email": self.email

        }

class Items (db.Model):
    __tablename__ = 'Items'
    id = db.Column(db.Integer, primary_key=True)
    product_name=db.Column(db.String(150), nullable=False)
    quantity = db.Column(db.Integer, nullable=True)
    unit_price = db.Column(db.float, nullable=False)
    def __repr__(self):
        return '<Items %r>' % self.product_name
    def serialize(self):
        return{
            "id": self.id,
            "item": self.product_name,
            "quantity": self.quantity,
            "unit_price": self.unit_price
        }
            