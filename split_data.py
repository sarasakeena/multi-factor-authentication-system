import os
import random
import shutil
from itertools import islice

outputFolderPath = "Datasett/SplitData"
inputFolderPath = "Datasett/all"
splitRatio = {"train": 0.7, "val": 0.2, "test": 0.1}
classes = ["fake", "real"]

# Remove the output folder if it exists and recreate it
if os.path.exists(outputFolderPath):
    shutil.rmtree(outputFolderPath)
os.makedirs(outputFolderPath)

# Create necessary directories
for split in ["train", "val", "test"]:
    os.makedirs(f"{outputFolderPath}/{split}/images", exist_ok=True)
    os.makedirs(f"{outputFolderPath}/{split}/labels", exist_ok=True)

# Get the list of unique image names (without extensions)
listNames = os.listdir(inputFolderPath)
uniqueNames = list(set(name.split('.')[0] for name in listNames))

# Shuffle the list randomly
random.shuffle(uniqueNames)

# Split data according to given ratios
lenData = len(uniqueNames)
lenTrain = int(lenData * splitRatio['train'])
lenVal = int(lenData * splitRatio['val'])
lenTest = lenData - (lenTrain + lenVal)  # Ensuring all images are used

# Split into train, val, test
lengthToSplit = [lenTrain, lenVal, lenTest]
Input = iter(uniqueNames)
Output = [list(islice(Input, elem)) for elem in lengthToSplit]

print(f'Total Images: {lenData} \nSplit: {len(Output[0])} {len(Output[1])} {len(Output[2])}')

# Copy images and labels
sequence = ['train', 'val', 'test']
for i, out in enumerate(Output):
    for fileName in out:
        # Copy image if exists
        image_path = f'{inputFolderPath}/{fileName}.jpg'
        if os.path.exists(image_path):
            shutil.copy(image_path, f'{outputFolderPath}/{sequence[i]}/images/{fileName}.jpg')
        else:
            print(f"Warning: {image_path} not found, skipping.")

        # Copy label if exists
        txt_path = f'{inputFolderPath}/{fileName}.txt'
        if os.path.exists(txt_path):
            shutil.copy(txt_path, f'{outputFolderPath}/{sequence[i]}/labels/{fileName}.txt')
        else:
            print(f"Warning: {txt_path} not found, skipping.")

print("Split Process Completed...")

# Create data.yaml file
dataYaml = f"""path: ../Data
train: ../train/images
val: ../val/images
test: ../test/images

nc: {len(classes)}
names: {classes}
"""

with open(f"{outputFolderPath}/data.yaml", 'w') as f:
    f.write(dataYaml)

print("Data.yaml file Created...")
