from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange
from wtforms.fields import SelectField
import datetime 

max_year = datetime.datetime.today().year + 1

class PredictionForm(FlaskForm):
    """Form for prediction
    """
    Year_Built = IntegerField(label='Année de construction', validators=[
        DataRequired(), NumberRange(min=1800, max=max_year, message=f"Year must be between 1800 and {max_year}")], default=2020)
    
    Total_Bsmt_SF = IntegerField(label='Surface de la cave en m2', validators=[
        DataRequired(), NumberRange(min=0, message="Negative value is not possible")], default=150)
    
    Frst_Flr_SF = IntegerField(label='Surface du 1er étage en m2', validators=[
        DataRequired(), NumberRange(min=0, message="Negative value is not possible")], default=150)
    
    Gr_Liv_Area = IntegerField(label='Surface habitable en m2', validators=[
        DataRequired(), NumberRange(min=0, message="Negative value is not possible")], default=50)
    
    Garage_Area = IntegerField(label="Surface du garage en m2", validators=[
        DataRequired() , NumberRange(min=0, message="Negative value is not possible")], default=55)
    
    Overall_Qual = IntegerField(label='Qualité générale', validators=[
        DataRequired() , NumberRange(min=0, max=11, message="Value must be between 0 and 5")], default=5)
    
    Full_Bath = IntegerField(label='Année de construction', validators=[
        DataRequired(), NumberRange(min=0, message="Negative value is not possible")], default=3)
    
    Exter_Qual = SelectField(label="Qualité de l'exterieur", validators=[
        DataRequired()], choices=[ 'Po', 'Fa','TA', 'Gd','Ex'], default="Ex")
    
    Kitchen_Qual = SelectField(label='Qualité de la cuisine', validators=[
        DataRequired()], choices=[ 'Po', 'Fa','TA', 'Gd','Ex'], default="TA")
    
    Neighborhood = SelectField(label='Quartier', validators=[
        DataRequired()], choices=['NAmes'], default="NAmes")
    
    submit = SubmitField(label='prediction')