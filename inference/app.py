from flask import Flask, request
from flask_cors import CORS
import numpy as np
from PIL import Image
from inference import inference

app = Flask(__name__)
CORS(app=app)


@app.post("/inference")
def endpoint():
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
