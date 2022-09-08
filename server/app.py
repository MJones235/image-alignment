from flask import Flask, request
from align_images.align_images import get_aligned_image
from type_converter.base64_image import base64_to_image, image_to_base64
import sys
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def align_images():
    data = request.get_json()
    template = base64_to_image(data['template'].split(',')[1])
    image_split = data['image'].split(',')
    image_prefix = image_split[0] + ','
    image = base64_to_image(image_split[1])
    aligned_image = get_aligned_image(template, image)
    return {
        'aligned-image': image_prefix + image_to_base64(aligned_image)
    }
