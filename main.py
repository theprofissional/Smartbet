from flask import Flask, render_template, request, jsonify
import numpy as np
import json
import os

app = Flask(__name__)

DATA_FILE = "history.json"

# نموذج بسيط مبدئي
def basic_model(features):
    total = sum(features)
    if total > 5:
        return {"prediction": "Over 2.5 Goals", "details": "Strong attacking potential ⚽"}
    elif total > 2:
        return {"prediction": "Goal/Goal", "details": "Balanced match, both likely to score"}
    else:
        return {"prediction": "Under 2.5", "details": "Defensive game expected"}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    stats = data.get('features', [])
    result = basic_model(stats)
    return jsonify(result)

@app.route('/save_example', methods=['POST'])
def save_example():
    example = request.get_json()
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
    with open(DATA_FILE, 'r+') as f:
        data = json.load(f)
        data.append(example)
        f.seek(0)
        json.dump(data, f, indent=4)
    return jsonify({'status': 'saved'})

# 🔮 الخطوة القادمة: نظام تدريب النموذج الذاتي
def train_model():
    if not os.path.exists(DATA_FILE):
        print("No data to train yet.")
        return
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    print(f"Training model with {len(data)} examples... (future implementation)")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
