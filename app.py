import joblib
import numpy as np
from flask import Flask, request, jsonify
import os  # Add this import for environment variables

app = Flask(__name__)

# Load the model
model = joblib.load('models/global_model.pkl')

@app.route('/')
def home():
    return "✅ Sales Forecasting API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        input_features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(input_features)
        return jsonify({'Sales_prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Get PORT from environment or default to 5000
    app.run(host='0.0.0.0', port=port)  # Remove debug=True for production
