import torch
import torchvision
import torchvision.transforms as transforms

def load_dataset(self)
    transform = transforms.Compose(
        [transforms.ToTensor(), 
         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    trainset = torchvision.datasets.CIFAR(root='./data', train=True,
                                          download=True, transform=transform)
    trainloader = torch.utils.data.DataLoader
