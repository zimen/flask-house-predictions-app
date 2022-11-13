from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from application import db 
import datetime

class Prediction(db.Model, UserMixin):
    __tablename__ = "Prediction"
    id = db.Column(db.Integer(), primary_key=True, nullable=False, unique=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('User.id'))
    created_on = db.Column(db.DateTime(), default=datetime.datetime.now())
    
    overall_qual = db.Column(db.Integer())
    neighborhood = db.Column(db.String()) 
    year_remod_add = db.Column(db.Integer())
    exterior_1st = db.Column(db.String()) 
    bsmt_qual = db.Column(db.String()) 
    exter_qual = db.Column(db.String())
    kitchen_qual = db.Column(db.String()) 
    garage_qual = db.Column(db.Integer())
    fireplaces = db.Column(db.Integer())
    fireplace_qu = db.Column(db.String())
    full_bath = db.Column(db.Integer())
    half_bath = db.Column(db.Integer())
    bsmt_full_bath = db.Column(db.Integer())
    bsmt_half_bath = db.Column(db.Integer())
    utilities = db.Column(db.String())
    gr_liv_area = db.Column(db.Integer())
    total_bsmt_sf = db.Column(db.Integer())
    first_flr_sf = db.Column(db.Integer())
    second_flr_sf = db.Column(db.Integer())
    open_porch_sf = db.Column(db.Integer())
    wood_deck_sf = db.Column(db.Integer())
    pool_area = db.Column(db.Integer())
    heating_qc = db.Column(db.String())
    bsmt_exposure = db.Column(db.String())
    paved_drive = db.Column(db.String())
    street = db.Column(db.String())
    central_air = db.Column(db.String())
    condition_1 = db.Column(db.String())
    condition_2 = db.Column(db.String())
    garage_cars = db.Column(db.Integer())
    garage_finish = db.Column(db.String())
    garage_area = db.Column(db.Integer())
    sale_condition = db.Column(db.String())
    price = db.Column(db.Integer()) 
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()