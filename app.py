import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load('dt.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    output = int(prediction[0])

    result = 'Unknown'
    if output == 0:
       result = 'Iris Setosa'
    elif output == 1:
       result = 'Iris Versicolour'
    elif output == 2:
       result = 'Iris Virginica'

    return render_template('index.html', prediction_text='Iris: {}'.format(result))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = int(prediction[0])

    result = 'Unknown'
    if output == 0:
       result = 'Iris Setosa'
    elif output == 1:
       result = 'Iris Versicolour'
    elif output == 2:
       result = 'Iris Virginica'

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
