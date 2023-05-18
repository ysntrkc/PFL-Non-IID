import numpy as np
import os
import random
import torch
import torchvision
import torchvision.transforms as transforms
from utils.dataset_utils import check, separate_data, split_data, save_file

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, default='ham10000', help='dataset name')
parser.add_argument('--num_clients', type=int, default=10, help='number of clients')
parser.add_argument('--num_classes', type=int, default=7, help='number of classes')
parser.add_argument('--niid', type=bool, default=False, help='niid')
parser.add_argument('--balance', type=bool, default=True, help='balance')
parser.add_argument('--partition', type=str, default='-', help='partition')

args = parser.parse_args()

random.seed(1)
np.random.seed(1)
num_clients = args.num_clients
num_classes = args.num_classes
dir_path = os.path.dirname(os.path.realpath(__file__)) + f"/{args.dataset}/"

def generate_custom(dir_path, num_clients, num_classes, niid, balance, partition):
    os.makedirs(dir_path, exist_ok=True)

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

    # Get data
    transform = transforms.Compose(
        [
            transforms.Resize((224, 224)),
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

    print(f"{args.dataset} data generated")


if __name__ == "__main__":
    niid = args.niid
    balance = args.balance
    partition = args.partition if args.partition != '-' else None
    generate_custom(dir_path, num_clients, num_classes, niid, balance, partition)

    


    