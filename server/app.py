from flask import Flask, request
from align_images.align_images import get_aligned_image
from type_converter.base64_image import base64_to_image, image_to_base64
import sys

app = Flask(__name__)

@app.route('/', methods=['POST'])
def align_images():
    data = request.get_json()
    template = base64_to_image(data['template'])
    image = base64_to_image(data['image'])
    aligned_image = get_aligned_image(template, image)
    return {
        'aligned-image': image_to_base64(aligned_image)
    }
