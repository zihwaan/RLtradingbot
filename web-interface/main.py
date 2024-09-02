from flask import Flask, render_template, jsonify, request
from models.trader import Trader
from config.settings import settings
import asyncio

app = Flask(__name__)
trader = Trader()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/hyperparameter_tuning')
def hyperparameter_tuning():
    return render_template('hyperparameter_tuning.html')

@app.route('/data')
def get_data():
    return jsonify(trader.get_state())

@app.route('/train', methods=['POST'])
def train():
    hyperparameters = request.form.to_dict()
    # 학습 로직 구현
    return jsonify({"status": "training completed"})

@app.route('/stream')
def stream():
    def generate():
        for i in range(100):
            yield f"data: Log message {i}\n\n"
            asyncio.sleep(0.1)
    return app.response_class(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=settings.WEB_INTERFACE_PORT)