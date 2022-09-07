import numpy as np
import cv2
import base64

def base64_to_image(base64_img):
    img_bytes = base64.b64decode(base64_img)
    img_arr = np.frombuffer(img_bytes, dtype=np.uint8)
    return cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

def image_to_base64(image):
    _, img_arr = cv2.imencode('.jpg', image)
    img_bytes = img_arr.tobytes()
    return base64.b64encode(img_bytes).decode('ascii')