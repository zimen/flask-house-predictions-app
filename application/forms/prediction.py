from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange
from wtforms.fields import SelectField
import datetime 

max_year = datetime.datetime.today().year + 1

class PredictionForm(FlaskForm):
    """Form for prediction
    """
    overall_qual = IntegerField(label='Qualité générale', validators=[
        DataRequired() , NumberRange(min=0, max=11, message="Value must be between 0 and 5")], default=5)
    
    neighborhood = SelectField(label='Quartier', validators=[
        DataRequired()], choices=['NAmes', 'Gilbert', 'StoneBr', 'NWAmes', 'Somerst', 'BrDale',
                                'NPkVill', 'NridgHt', 'Blmngtn', 'NoRidge', 'SawyerW', 'Sawyer', 'Greens', 'BrkSide', 
                                'OldTown', 'IDOTRR', 'ClearCr', 'SWISU', 'Edwards', 'CollgCr', 'Crawfor', 'Blueste', 
                                'Mitchel', 'Timber', 'MeadowV', 'Veenker', 'GrnHill', 'Landmrk'] , default="NAmes")
    
    year_remod_add = IntegerField(label='Année de construction ou renovation', validators=[
        DataRequired(), NumberRange(min=1800, max=max_year, message=f"Year must be between 1800 and {max_year}")], default=2020)
    
    exterior_1st = SelectField(label='Métériaux extérieur', validators=[
        DataRequired()], choices=['BrkFace', 'VinylSd', 'Wd Sdng', 'CemntBd', 'HdBoard', 'Plywood',
                                'MetalSd', 'AsbShng', 'WdShing', 'Stucco', 'AsphShn', 'BrkComm',
                                'CBlock', 'PreCast', 'Stone', 'ImStucc'] , default="BrkFace")
    
    bsmt_qual = SelectField(label='Hauteur du sous-sol', validators=[
        DataRequired()], choices=['Ex', 'Gd', 'TA', 
                                  'Fa', 'Po (<70 inches)' 'NA'], default="NA")
    
    exter_qual = SelectField(label='Qualité extérieur', validators=[
        DataRequired()], choices=['Ex', 'Gd', 'TA', 'Fa'], default="TA")
    
    kitchen_qual = SelectField(label='Qualité de la cuisine', validators=[
        DataRequired()], choices=['Ex', 'Gd', 'TA', 'Fa', 'Po'], default="TA")
    
    garage_qual = SelectField(label='Qualité du garage', validators=[
        DataRequired()], choices=['TA', 'Fa', 'Gd', 'Ex', 'Po', 'No garage'], default="Ex")
    # Ajouter dictionnaire pour No garage en np.nan 
    
    fireplaces = IntegerField(label='Nombre de cheminée', validators=[
        DataRequired(), NumberRange(min=0, message=f"Entre 0 et infinie")], default=0)
    
    fireplace_qu = SelectField(label='Qualité du garage', validators=[
        DataRequired()], choices=['Gd', "No fireplace", 'TA', 'Po', 'Ex', 'Fa'], default="Ex")
    # Ajouter np.nan en dictionnaire à la place du no fireplace
    
    full_bath = IntegerField(label='Nombre de salle de bain complète', validators=[
        DataRequired(), NumberRange(min=0, message=f"Entre 0 et infinie")], default=0)
    
    half_bath = IntegerField(label='Nombre de demi salle de bain', validators=[
        DataRequired(), NumberRange(min=0, message=f"Entre 0 et infinie")], default=0)
    
    bsmt_full_bath = IntegerField(label='Nombre de salle de bain complète au sous-sol', validators=[
        DataRequired(), NumberRange(min=0, message=f"Entre 0 et infinie")], default=0)
    
    bsmt_half_bath = IntegerField(label='Nombre de demi salle de bain au sous-sol', validators=[
        DataRequired(), NumberRange(min=0, message=f"Entre 0 et infinie")], default=0)
    
    utilities = SelectField(label='Eau et éléctricité', validators=[
        DataRequired()], choices=['AllPub', 'NoSewr', 'NoSeWa'], default="AllPub")
    
    gr_liv_area = IntegerField(label='Surface habitable en m2', validators=[
        DataRequired(), NumberRange(min=0, message="Negative value is not possible")], default=50)
    
    total_bsmt_sf = IntegerField(label='Surface de la cave en m2', validators=[
        DataRequired(), NumberRange(min=0, message="Negative value is not possible")], default=150)
    
    first_flr_sf = IntegerField(label='Surface du 1er étage en m2', validators=[
        DataRequired(), NumberRange(min=0, message="Negative value is not possible")], default=150)
    
    second_flr_sf = IntegerField(label='Surface du 2ème étage en m2', validators=[
        DataRequired(), NumberRange(min=0, message="Negative value is not possible")], default=150)
    
    open_porch_sf = IntegerField(label='Surface du porche', validators=[
        DataRequired(), NumberRange(min=0, message="Negative value is not possible")], default=150)
    
    wood_deck_sf = IntegerField(label='Surface terasse en bois', validators=[
        DataRequired(), NumberRange(min=0, message="Negative value is not possible")], default=0)
    
    pool_area = IntegerField(label='Surface piscine', validators=[
        DataRequired(), NumberRange(min=0, message="Negative value is not possible")], default=0)
    
    heating_qc = SelectField(label='Qualité du chauffage', validators=[
        DataRequired()], choices=['Ex', 'Gd', 'TA', 'Fa', 'Po'], default="TA")
    
    bsmt_exposure = SelectField(label='Qualité murs rez-de-chaussée ou jardin', validators=[
        DataRequired()], choices=['Gd', 'No', 'Mn', 'Av'], default="No")
    
    paved_drive = SelectField(label='Chemin pavé ou gravié', validators=[
        DataRequired()], choices=['P', 'Y', 'N'], default="P")
    
    street = SelectField(label='Rue pavé ou gravié', validators=[
        DataRequired()], choices=['Pave', 'Grvl'], default="Pave")
    
    central_air = SelectField(label='Rue pavé ou gravié', validators=[
        DataRequired()], choices=['Y', 'N'] , default="N")
    
    condition_1 = SelectField(label='Proximité axes routiers', validators=[
        DataRequired()], choices=['Norm', 'Feedr', 'PosN', 'RRNe', 'RRAe', 'Artery', 'PosA', 'RRAn', 'RRNn'], default="Norm")
    
    condition_2 = SelectField(label='Proximité axes routiers', validators=[
        DataRequired()], choices=['Norm', 'Feedr', 'PosA', 'PosN', 'Artery', 'RRNn', 'RRAe', 'RRAn'], default="Norm")
    
    garage_cars = IntegerField(label="Nombre de voiture entrant dans le garage", validators=[
        DataRequired() , NumberRange(min=0, message="Negative value is not possible")], default=0)
    
    garage_area = IntegerField(label="Surface du garage en m2", validators=[
        DataRequired() , NumberRange(min=0, message="Negative value is not possible")], default=55)
    
    garage_finish = SelectField(label="Qualité de l'exterieur", validators=[
        DataRequired()], choices=['Fin', 'Unf', 'RFn'] , default="Fin")
    
    sale_condition = SelectField(label="Qualité de l'exterieur", validators=[
        DataRequired()], choices=['Normal', 'Partial', 'Family', 'Abnorml', 'Alloca', 'AdjLand'], default="Ex")
    
    submit = SubmitField(label='prediction')