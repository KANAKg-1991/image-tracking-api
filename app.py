from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask API is running!"

@app.route('/track_image', methods=['POST'])
def track_image():
    data = request.json
    image_url = data.get('image_url')
    return jsonify({"message": f"Tracking started for {image_url}"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=True)