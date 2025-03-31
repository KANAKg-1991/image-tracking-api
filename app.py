from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask API is running!"

@app.route('/health')
def health():
    return jsonify({"status": "API is working fine!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)