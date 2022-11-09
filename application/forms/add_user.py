from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, SubmitField, StringField
from wtforms.validators import DataRequired

class AddUser(FlaskForm):
    """[Form to add user]
    """
    lastname = StringField(label='Nom', validators=[DataRequired()])
    firstname = StringField(label='Prénom', validators=[DataRequired()])
    email = EmailField(label='Email', validators=[DataRequired()])
    password_hash = PasswordField(label='Mot de passe', validators=[DataRequired()])
    password_hash2 = PasswordField(label='Confirmez votre mot de passe', validators=[DataRequired()])
    submit = SubmitField(label='Ajouter')