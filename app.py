from flask import Flask, request, render_template

import numpy as np
import pickle
import joblib

# Create Flask object to run
app = Flask(__name__,template_folder= 'templates' )

@app.route('/')
def home():
    return render_template('indexcredit.html')

@app.route('/predict',methods=['POST'])
def predict():
  try:
    knnIrisModel = joblib.load('assesment.pkl')
    int_features = [float(x) for x in request.form.values()]

    V4 = request.form.get('V4')
    V14 = request.form.get('V14')




    final_features = [[float(V4),float(V14)]]
    print(final_features)

    prediction = knnIrisModel.predict(final_features)
    output =prediction[0]
    if output == 0:
      output = 'normal'
    if output == 1:
      output = 'fraud'
    return render_template('indexcredit.html', prediction_text= output)
  except:
    return render_template('indexcredit.html', prediction_text= 'invalid input')
    
if __name__ == "__main__":
	app.run()
