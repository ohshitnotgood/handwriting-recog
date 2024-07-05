Inference server running a convolutional neural network to do image recognition on single digits.

Inference model trained on the classic MNIST dataset.

When the frontend sends data, the image is first written to disk before inference can be run on it.


Dependencies:
    - PyTorch
    - Pillow
    - numpy
    - Flask
    - flask-cors