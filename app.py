from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask API is running!"

@app.route('/track_image', methods=['POST'])
def track_image():
    data = request.json
    image_url = data.get('image_url')
    return jsonify({"message": "Tracking started for " + image_url})

if __name__ == '__main__':
    app.run(debug=True)