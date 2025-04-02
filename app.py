from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask API is running!"

@app.route('/track_image', methods=['POST'])
def track_image():
    data = request.json
    image_url = data.get('image_url')

    if not image_url:
        return jsonify({"error": "No image URL provided"}), 400

    # Google Reverse Image Search URL তৈরি করা
    tracking_link = f"https://www.google.com/searchbyimage?image_url={image_url}"

    return jsonify({"message": "Tracking started", "tracking_url": tracking_link})

if __name__ == '__main__':
    app.run(debug=True)