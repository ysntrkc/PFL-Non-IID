import pandas as pd
import zipfile
import shutil
import os

# Replace with the path to your isic2019.zip file
zip_file_path = "./isic2019.zip"

# Replace with the path where you want to extract the files
target_dir = "./temp"

# Create the target directory if it doesn't exist
os.makedirs(target_dir, exist_ok=True)

# Extract the contents of the zip file to the target directory
with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
    zip_ref.extractall(target_dir)

# Replace with the path to the "ISIC_2019_Training_Input" folder
input_folder = os.path.join(
    target_dir, "ISIC_2019_Training_Input", "ISIC_2019_Training_Input"
)

# Replace with the path to the "ISIC_2019_Training_GroundTruth.csv" file
ground_truth_file = os.path.join(target_dir, "ISIC_2019_Training_GroundTruth.csv")

# Replace with the path to the output directory for train and test folders
output_dir = "./isic2019/rawdata"

# Replace with the desired split ratio
train_ratio = 0.8

# Load the ground truth CSV file into a pandas DataFrame
ground_truth = pd.read_csv(ground_truth_file)

# Create the output directories
train_dir = os.path.join(output_dir, "train")
test_dir = os.path.join(output_dir, "test")
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Get the unique class labels
class_labels = ground_truth.columns[1:]

# remove "UNK" from class_labels
class_labels = class_labels.drop("UNK")

# Loop through each class label
for class_label in class_labels:
    # Create the class directories within the train and test directories
    train_class_dir = os.path.join(train_dir, class_label)
    test_class_dir = os.path.join(test_dir, class_label)
    os.makedirs(train_class_dir, exist_ok=True)
    os.makedirs(test_class_dir, exist_ok=True)

    # Get the image IDs for the current class
    class_image_ids = ground_truth.loc[ground_truth[class_label] == 1, "image"]

    # Shuffle the image IDs
    class_image_ids = class_image_ids.sample(frac=1, random_state=42).reset_index(
        drop=True
    )

    # Calculate the number of images for the training and testing sets
    num_train = int(len(class_image_ids) * train_ratio)
    num_test = len(class_image_ids) - num_train

    # Copy the training set images to the train directory
    for i in range(num_train):
        image_id = class_image_ids[i]
        src_path = os.path.join(input_folder, f"{image_id}.jpg")
        dst_path = os.path.join(train_class_dir, f"{image_id}.jpg")
        shutil.copy(src_path, dst_path)

    # Copy the testing set images to the test directory
    for i in range(num_train, len(class_image_ids)):
        image_id = class_image_ids[i]
        src_path = os.path.join(input_folder, f"{image_id}.jpg")
        dst_path = os.path.join(test_class_dir, f"{image_id}.jpg")
        shutil.copy(src_path, dst_path)

# Delete the temporary directory
shutil.rmtree(target_dir)
