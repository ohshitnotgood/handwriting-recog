from flask import Flask, request
from flask_cors import CORS
import numpy as np
from PIL import Image
from inference import inference

app = Flask(__name__)
CORS(app=app)


@app.post("/inference")
def endpoint():
    """
    Endpoint to run inference
    
    Frontend is expected to send the image as an array which is converted to an image and run inference on.
    
    When the frontend sends data, the image is first written to disk before inference can be run on it.
    
    Result is returned to frontend.
    """
    json = request.json
    imageData = json["imData"]
    imageData = imageData.split(",")
    imageData = np.array(imageData, dtype=np.uint8)
    imageData = np.reshape(imageData, (600, 600, 4))
    data = Image.fromarray(imageData, "RGBA")
    data = data.convert("L")
    data = data.resize((28, 28))
    data.save("./out/savefile.png")
    
    output = inference()
    print(f"Returning {output} as the answer")
    return output
