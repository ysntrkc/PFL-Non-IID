import pandas as pd
import shutil
import zipfile
import os
import random

# Replace with the path to your ham10000.zip file
zip_file_path = "./ham10000.zip"

# Replace with the path where you want to save the extracted files
target_dir = "./ham10000"

# Create the target directory if it doesn't exist
os.makedirs(target_dir, exist_ok=True)

# Extract the contents of the zip file to the target directory
with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
    zip_ref.extractall(target_dir)

ham10000_dir = "./ham10000"
images_part_1_dir = f"{ham10000_dir}/HAM10000_images_part_1"
images_part_2_dir = f"{ham10000_dir}/HAM10000_images_part_2"

# remove the files and forders in the ham10000_dir except the two folders and HAM10000_metadata.csv
for filename in os.listdir(ham10000_dir):
    if (
        filename != "HAM10000_images_part_1"
        and filename != "HAM10000_images_part_2"
        and filename != "HAM10000_metadata.csv"
    ):
        try:
            shutil.rmtree(os.path.join(ham10000_dir, filename))
        except:
            os.remove(os.path.join(ham10000_dir, filename))

all_images_dir = f"{ham10000_dir}/ham10000"

# Create the "ham10000" folder in "ham10000" folder if it doesn't exist
os.makedirs(all_images_dir, exist_ok=True)

# Loop through the files in the "HAM10000_images_part_1" folder and copy them to the "ham10000" folder
for filename in os.listdir(images_part_1_dir):
    src_path = os.path.join(images_part_1_dir, filename)
    dst_path = os.path.join(all_images_dir, filename)
    shutil.copy(src_path, dst_path)

# Loop through the files in the "HAM10000_images_part_2" folder and copy them to the "ham10000" folder
for filename in os.listdir(images_part_2_dir):
    src_path = os.path.join(images_part_2_dir, filename)
    dst_path = os.path.join(all_images_dir, filename)
    shutil.copy(src_path, dst_path)


# Read the "HAM10000_metadata.csv" file
metadata_df = pd.read_csv(
    f"{ham10000_dir}/HAM10000_metadata.csv", usecols=["image_id", "dx"]
)

# Create a new column called "path" which contains the path to the images
metadata_df["path"] = metadata_df["image_id"].map(lambda x: f"{all_images_dir}/{x}.jpg")

# Create a dictionary to store the destination directories for each "dx" value
dx_dirs = {}

# Loop through the rows in the metadata DataFrame
for index, row in metadata_df.iterrows():
    # Get the image ID and dx value for the current row
    image_id = row["image_id"]
    dx = row["dx"]

    # Create the destination directory for the current "dx" value if it doesn't exist
    if dx not in dx_dirs:
        dx_dirs[dx] = os.path.join(all_images_dir, dx)
        os.makedirs(dx_dirs[dx])

    # Move the image to its destination directory
    shutil.move(f"{all_images_dir}/{image_id}.jpg", f"{dx_dirs[dx]}/{image_id}.jpg")

# create "rawdata" folder
os.makedirs("./rawdata", exist_ok=True)

train_dir = "./rawdata/train"
test_dir = "./rawdata/test"

classes = ["akiec", "bcc", "bkl", "df", "mel", "nv", "vasc"]

# Create the "train" and "test" folders if they don't exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Loop through the class folders
for class_folder in dx_dirs:
    # list all images in the current class folder
    images = os.listdir(dx_dirs[class_folder])

    # shuffle the images
    images = random.sample(images, len(images))

    # calculate the number of train images (80% of the images) and test images (20% of the images)
    num_train_images = int(len(images) * 0.8)
    num_test_images = len(images) - num_train_images

    # Create the train and test subfolders in the "train" and "test" folders respectively
    os.makedirs(f"{train_dir}/{class_folder}", exist_ok=True)
    os.makedirs(f"{test_dir}/{class_folder}", exist_ok=True)

    # Loop through the images in the current class folder
    for i, image in enumerate(images):
        # Get the source path of the image
        src_path = os.path.join(dx_dirs[class_folder], image)

        # Set the destination path of the image
        if i < num_train_images:
            dst_path = os.path.join(train_dir, class_folder, image)
        else:
            dst_path = os.path.join(test_dir, class_folder, image)

        # Move the image
        shutil.move(src_path, dst_path)

# remove "ham10000" folder
shutil.rmtree(target_dir)

# create "ham10000" folder
os.makedirs(target_dir, exist_ok=True)

# move "./rawdata" to "./ham10000"
shutil.move("./rawdata", target_dir)
