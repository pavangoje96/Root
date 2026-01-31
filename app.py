from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
# IMPORTANT: This allows your InfinityFree frontend to talk to this API
CORS(app) 

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    try:
        num1 = float(data.get('num1', 0))
        num2 = float(data.get('num2', 0))
        operation = data.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else "Error (Div by 0)"
        else:
            result = "Invalid Operation"
            
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"result": "Error", "message": str(e)}), 400

if __name__ == "__main__":
    # Koyeb uses Gunicorn, but this allows local testing
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
