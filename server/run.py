from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def hello_world():
 return 'Hello to the World of Flask!'

@app.route('/check', methods=['POST'])
def check():
    # res = "check success " + request.data
    data = request.get_json()
    # print(data['input'])
    message = data['input']
    return jsonify(
        message="Output"
    )

if __name__ == '__main__':
 app.run()
