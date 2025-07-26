
from flask import Flask, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Dummy ML model (replace with real joblib model if needed)
def dummy_predict(x):
    return "positive" if sum(x) > 0 else "negative"

@app.route('/')
def index():
    return "Welcome to the ML Appp veerababu narni!"

@app.route('/predict', methods=['GET'])
def predict():
    sample_input = [1, -1, 3]
    prediction = dummy_predict(sample_input)
    return jsonify({'prediction': prediction})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200
    #👇 Uncomment to simulate failure:
    #return jsonify({'status': 'unhealthy'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
