# Insurance Charges Prediction Web App

A Flask web application to predict **insurance charges** using a **Gradient Boosting Regressor** model. The app allows manual input and displays predicted charges in both **USD and INR**.
---

## Features

- Predict insurance charges based on:
  - `age`
  - `sex`
  - `bmi`
  - `children`
  - `smoker`
  - `region`
- Display results in **USD and INR**
- Beautiful **Tailwind CSS UI**
- **Background color changes every second**
- **Badge** with name "Naveen Dwivedi"

---

## Tech Stack

- **Backend:** Python, Flask  
- **Machine Learning:** scikit-learn (Gradient Boosting Regressor)  
- **Frontend:** HTML, Tailwind CSS, JavaScript  
- **Model Serialization:** joblib  
- **Deployment:** Render  

---

## Project Structure

insurance-charges-app/
│
├─ app.py # Main Flask application
├─ best_gradient_boosting_model.joblib # Trained model
├─ templates/
│ ├─ index.html # Input form
│ └─ result.html # Prediction result
├─ static/ # Optional static files
└─ README.md # Project documentation

## Running the App Locally

Run the Flask application:

python app.py


## Open your browser and go to:

http://127.0.0.1:5000/

## Project Demo Link:

https://insurance-charges.onrender.com/


## Deployment on Render

Follow these steps to deploy the app:

Sign up at Render
.

Create a new Web Service and connect your GitHub repository.

Set the environment to Python 3.

In Build Command, enter:

pip install -r requirements.txt


## In Start Command, enter:

python app.py


Ensure the best_gradient_boosting_model.joblib file is included in the repository.

Click Deploy.

Your app will be live at the Render URL provided.

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd insurance-charges-app 



