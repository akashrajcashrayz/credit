from google.colab import drive
drive.mount('/content/drive')
from flask import Flask, request, render_template
!pip install flask-ngrok
from flask_ngrok import run_with_ngrok

import numpy as np
import pickle
import joblib

# Create Flask object to run
app = Flask(__name__,template_folder= 'drive/My Drive/lstmrpoject' )
run_with_ngrok(app)

@app.route('/')
def home():
    return render_template('indexcredit.html')

@app.route('/predict',methods=['POST'])
def predict():
  try:
    knnIrisModel = joblib.load('/content/drive/My Drive/dataset/assesment.pkl')
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
