# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib
import submarine_model

app = Flask(__name__)

model = joblib.load("submarine_rock vs mine _model.pkl","rb")

df = pd.DataFrame()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_2():
    global df

    input_features =[request.form.values()]
    features_value=np.array(input_features)

    output = submarine_model.prediction


    # input and predicted value store in df then save in csv file
    df= pd.concat([df,pd.DataFrame({'SONAR FREQUENCY DATA OF SUBMARINE':input_features,'Predicted Output':[output]})] )

    df.to_csv('smp_data_from_app.csv')
    if (output=='M'):
        return render_template('index.html', prediction_text ="{0} The object is mine.".format(output))
    elif (output=='R'):
        return render_template('index.html', prediction_text="{0} The object is rock.".format(output))


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=8080)
    