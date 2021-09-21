from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open('linear_reg.pkl', 'rb'))

@app.route('/')
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        CRIM = request.form['CRIM']
        ZN = request.form['ZN']        
        CHAS = request.form['CHAS']
        NOX = request.form['NOX']
        RM = request.form['RM']
        AGE = request.form['AGE']
        DIS = request.form['DIS']
        RAD = request.form['RAD']
        PT_RATIO = request.form['PT_RATIO']
        LSTAT = request.form['LSTAT'] 

        try:    
            prediction = model.predict([[ CRIM, ZN, CHAS, NOX,
                                            RM, AGE, DIS, RAD, PT_RATIO, LSTAT]])
        
            return render_template('result.html',prediction_text="PREDICTED HOUSE PRICE :  {}".format(prediction[0] * 1000 ))
            
            print(prediction[0])
            
        except:
            return render_template('index.html')
        
        
    else:
        return render_template('index1.html')

if __name__=="__main__":
    app.run(debug=True)

