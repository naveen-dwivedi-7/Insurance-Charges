# app.py
from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the Gradient Boosting model
with open("best_gradient_boosting_model.pkl", "rb") as f:
    model = pickle.load(f)

# Region mapping used during model training
region_map = {'northwest':0, 'northeast':1, 'southwest':2, 'southeast':3}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Manual input only
    age = int(request.form.get('age',30))
    bmi = float(request.form.get('bmi',25.0))

    data = {
        'age': age,
        'sex': int(request.form.get('sex',1)),
        'bmi': bmi,
        'children': int(request.form.get('children',0)),
        'smoker': int(request.form.get('smoker',0)),
        'region': {'northwest':0,'northeast':1,'southwest':2,'southeast':3}[request.form.get('region','northwest')]
    }

    df = pd.DataFrame([data])
    prediction_usd = model.predict(df)[0]

    # Convert USD to INR
    usd_to_inr_rate = 83  # Update with live rate if needed
    prediction_inr = prediction_usd * usd_to_inr_rate

    return render_template("result.html",
                           prediction_usd=round(prediction_usd,2),
                           prediction_inr=round(prediction_inr,2))


if __name__ == "__main__":
    app.run(debug=True)
