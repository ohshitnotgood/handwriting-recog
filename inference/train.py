from torch import optim
from model import MNISTClassifier
from hyperparameters import learning_rate, device, n_epoch
from torch import nn
from dataloader import train_loader
import torch

model = MNISTClassifier()
model.to("cuda")

optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
loss_fn = nn.CrossEntropyLoss()

def train():
    for epoch in range(n_epoch):
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(images)  
            loss = loss_fn(outputs, labels)
            loss.backward()  
            optimizer.step() 

        print(f"Epoch:{epoch} loss is {loss.item()}")
    
    torch.save(model.state_dict(), './model/model_state_ep2.pt')


if __name__ == "__main__":
    train()

