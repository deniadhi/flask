from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import joblib
import json


app = Flask(__name__)


@app.route('/flask_api/', methods=['POST'])
def makecalc():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)

if __name__ == '__main__':
    model = joblib.load('flask_model.pkl') 
    app.run(debug=True)
