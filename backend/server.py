from flask import Flask, request
from flask_cors import CORS
from app import generate_img

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
@app.route('/', methods=['POST'])
def handle_post_request():
    data = request.get_json()
    generate_img(data['city'], data['planet'])
    return data
    # call the python function
    # result = my_function(data)
    # return result

if __name__ == '__main__':
    app.run(port=8080)
