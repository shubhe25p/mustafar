from flask import Flask, request, Response
from PIL import Image
from flask_cors import CORS
from app import generate_img
import io
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
@app.route('/', methods=['POST'])
def handle_post_request():
    data = request.get_json()
    imageBinary = generate_img(data['city'], data['planet'])
    img = Image.open(io.BytesIO(imageBinary))

    # create a response object with the modified image
    response = Response(content_type='image/jpeg')
    img.save(response.stream, 'JPEG')

    return response
    # call the python function
    # result = my_function(data)
    # return result

if __name__ == '__main__':
    app.run(port=8080)
