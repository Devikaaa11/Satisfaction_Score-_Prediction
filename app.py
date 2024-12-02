from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle 

app = Flask(__name__)

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    try:

        items_purchased = int(request.form['Items Purchased'])
        warranty_extension_input = request.form['Warranty Extension'].strip().lower()
        loyalty_score = int(request.form['Loyalty Score'])

        if warranty_extension_input == 'yes':
            warranty_extension = 1
        elif warranty_extension_input == 'no':
            warranty_extension = 0
        else:
            raise ValueError("Invalid input for Warranty Extension. Please enter 'Yes' or 'no'")
        
        input_features = np.array([[items_purchased, warranty_extension, loyalty_score]])


        prediction = model.predict(input_features)[0]

        return render_template('result.html', prediction = prediction)
    
    except Exception as e:
        return render_template('index.html', error=str(e))
    
if __name__ == '__main__':
    app.run(debug=True)