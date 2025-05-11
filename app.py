from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)

# Load the saved ML model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form.get(feat)) for feat in [
            'cement', 'slag', 'flyash', 'water', 'superplasticizer',
            'coarseagg', 'fineagg', 'age'
        ]]

        prediction = model.predict([features])[0]
        prediction = round(prediction, 2)

        return render_template('index.html', prediction_text=f"Predicted Strength: {prediction} MPa")
    
    except:
        return render_template('index.html', prediction_text="Error: Invalid input")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
