import numpy as np
import os
import sys
import random
import torch
import torchvision
import torchvision.transforms as transforms
from utils.dataset_utils import check, separate_data, split_data, save_file


random.seed(1)
np.random.seed(1)
num_clients = 10
num_classes = 5
dir_path = "/media/muhendislik/HDD1/undergrad/code/FedAvg/dataset/brain/"


def generate_brain(dir_path, num_clients, num_classes, niid, balance, partition):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    config_path = dir_path + "config.json"
    train_path = dir_path + "train/"
    test_path = dir_path + "test/"

    if check(
        config_path,
        train_path,
        test_path,
        num_clients,
        num_classes,
        niid,
        balance,
        partition,
    ):
        return

    # Get brain data
    transform = transforms.Compose(
        [
            transforms.Resize((224, 224)),
            transforms.RandomAffine(degrees=10, translate=(0.02, 0.02)),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ]
    )

    trainset = torchvision.datasets.ImageFolder(
        root=dir_path + "rawdata/train", transform=transform
    )
    testset = torchvision.datasets.ImageFolder(
        root=dir_path + "rawdata/test", transform=transform
    )

    trainloader = torch.utils.data.DataLoader(
        trainset, batch_size=len(trainset.imgs), shuffle=False
    )
    testloader = torch.utils.data.DataLoader(
        testset, batch_size=len(testset.imgs), shuffle=False
    )

    for _, t_d in enumerate(trainloader, 0):
        trainset.imgs, trainset.targets = t_d
    for _, t_d in enumerate(testloader, 0):
        testset.imgs, testset.targets = t_d

    del t_d
    del trainloader
    del testloader

    dataset_image = []
    dataset_label = []

    dataset_image.extend(trainset.imgs.cpu().detach().numpy())
    dataset_image.extend(testset.imgs.cpu().detach().numpy())
    dataset_label.extend(trainset.targets.cpu().detach().numpy())
    dataset_label.extend(testset.targets.cpu().detach().numpy())
    dataset_image = np.array(dataset_image)
    dataset_label = np.array(dataset_label)

    del trainset
    del testset

    # dataset = []
    # for i in range(num_classes):
    #     dataset.append([])
    # for i in range(len(dataset_image)):
    #     dataset[dataset_label[i]].append(dataset_image[i])

    # Separate data
    X, y, statistic = separate_data(
        (dataset_image, dataset_label),
        num_clients,
        num_classes,
        niid,
        balance,
        partition,
    )

    del dataset_image
    del dataset_label

    # Split data
    train_data, test_data = split_data(X, y)

    del X
    del y

    # Save data
    save_file(
        config_path,
        train_path,
        test_path,
        train_data,
        test_data,
        num_clients,
        num_classes,
        statistic,
        niid,
        balance,
        partition,
    )

    print("Brain data generated")


if __name__ == "__main__":
    # niid = True if sys.argv[1] == "noniid" else False
    # balance = True if sys.argv[2] == "balance" else False
    # partition = sys.argv[3] if sys.argv[3] != "-" else None
    niid = False
    balance = True
    partition = None
    generate_brain(dir_path, num_clients, num_classes, niid, balance, partition)
