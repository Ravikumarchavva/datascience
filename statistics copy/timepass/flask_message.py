import json
from flask_sqlalchemy import *
from flask import *
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///contact.db"
db = SQLAlchemy(app)
print("hi")
class chec(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.TEXT, nullable=False)
print("1")

with app.app_context():
    data = chec(id=2,name='sai')
    db.session.add(data)
    db.session.commit()
