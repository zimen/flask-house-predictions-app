from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from application import db 
import datetime

class Prediction(db.Model, UserMixin):
    __tablename__ = "Prediction"
    id = db.Column(db.Integer(), primary_key=True, nullable=False, unique=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('User.id'))
    Year_Built = db.Column(db.Integer())
    Total_Bsmt_SF = db.Column(db.Integer())
    Frst_Flr_SF = db.Column(db.Integer())
    Gr_Liv_Area = db.Column(db.Integer())
    Garage_Area = db.Column(db.Integer())
    Overall_Qual = db.Column(db.Integer())
    Full_Bath = db.Column(db.Integer())
    Exter_Qual = db.Column(db.String())
    Kitchen_Qual = db.Column(db.String()) 
    Neighborhood = db.Column(db.String()) 
    price = db.Column(db.Integer()) 
    created_on = db.Column(db.DateTime(), default=datetime.datetime.now())
    
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()