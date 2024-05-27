from flask import request, jsonify
from app import app
from app.model import generate_text


@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        prompt = data.get('prompt')
        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400

        response = generate_text(prompt)
        return jsonify(response)
    except Exception as e:
        # Log the error and return a message
        print(f"Error: {e}")
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500
