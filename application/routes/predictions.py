from flask import Blueprint, render_template, request
import pandas as pd
import joblib
from application.forms.prediction import  PredictionForm
from flask_login import current_user
from application import db 
from application.database.predictions import Prediction

model = joblib.load(open('model/fit/model.joblib', 'rb'))
prediction = Blueprint('prediction', __name__, url_prefix='/prediction')

@prediction.route('/')
def index():
    return render_template('prediction.html', form=PredictionForm())

@prediction.route('/predict', methods=['GET', 'POST'])
def predict():
    form = PredictionForm()
    if form.submit():
        X_predict = {}
        for var in ['Year_Built', 'Total_Bsmt_SF', 'Frst_Flr_SF', 'Gr_Liv_Area','Garage_Area', 'Overall_Qual', 'Full_Bath', 'Exter_Qual',
                'Kitchen_Qual', 'Neighborhood']:
            if var in ['Exter_Qual','Kitchen_Qual', 'Neighborhood']:
                X_predict[var]= request.form[var]
            else:
                X_predict[var]= int(request.form[var])
        df_prediction = pd.DataFrame(X_predict, index=[0])
        pred = int(model.predict(df_prediction))
        X_predict['price'] = pred
        Prediction(**X_predict, user_id=current_user.id).save_to_db()
    return render_template('prediction.html', data=f'{pred} $', form=form)

@prediction.route('/history', methods=['GET'])
def history():
    predictions = db.session.query(Prediction).where(Prediction.user_id == current_user.id).all()
    return render_template('history.html', predictions=predictions)
    