import torch
from model import MNISTClassifier
from PIL import Image
from torchvision import transforms
from hyperparameters import device

model_path = "./model/model_state.pt"


model = MNISTClassifier()

def inference():
    model.load_state_dict(torch.load(model_path))
    model.eval()
    model.to("cuda")
    image = Image.open("./out/savefile.png")
    img_transform = transforms.Compose([transforms.ToTensor()])
    img_tensor = img_transform(image).unsqueeze(0).to(device)
    output = model(img_tensor)
    predicted_label = torch.argmax(output)
    return str(predicted_label.item())

if __name__ == "__main__":
    print(inference())
    