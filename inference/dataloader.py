from torch.utils.data import DataLoader, Dataset
from torchvision.datasets import MNIST
from torchvision import transforms
from hyperparameters import val_batch_size, training_batch_size


mnist_train = MNIST("./data/", download=True, train=True, transform=transforms.ToTensor())
train_loader = DataLoader(mnist_train, shuffle=True, batch_size=training_batch_size)


mnist_val = MNIST("./data/", download=True, train=False, transform=transforms.ToTensor())
val_loader = DataLoader(mnist_val, shuffle=True, batch_size=val_batch_size)

if __name__ == "__main__":
    print(len(train_loader), len(val_loader))