import numpy as np
import os
from imageio.v2 import imread
from skimage.transform import resize
from scipy.ndimage import rotate

# Specify the image folder path
imageFolder = './data/nangua_70kv_2.8ma/nangua'

# Get list of image files
imageFiles = [f for f in os.listdir(imageFolder) if f.endswith('.tif')]

# Get dimensions from the first image to create a 3D body
firstImage = imread(os.path.join(imageFolder, imageFiles[0]))
m, n = 1024, 1024
numImages = len(imageFiles)

# Initialize the 3D body
imageStack = np.zeros((m, n, numImages), dtype=float)

# Process for bendi images
imageFolder_bendi = './data/nangua_70kv_2.8ma/bendi'
imageFiles_bendi = [f for f in os.listdir(imageFolder_bendi) if f.endswith('.tif')]
numImages_bendi = len(imageFiles_bendi)
bendi = np.zeros((1536, 1536), dtype=float)

for j, fname in enumerate(imageFiles_bendi):
    imageFileName_bendi = os.path.join(imageFolder_bendi, fname)
    imageData_bendi = imread(imageFileName_bendi).astype(float)
    bendi += imageData_bendi

bendi /= numImages_bendi

# Process for kongqi images
imageFolder_kongqi = './data/nangua_70kv_2.8ma/kongqi'
imageFiles_kongqi = [f for f in os.listdir(imageFolder_kongqi) if f.endswith('.tif')]
numImages_kongqi = len(imageFiles_kongqi)
kongqi = np.zeros((1536, 1536), dtype=float)

for k, fname in enumerate(imageFiles_kongqi):
    imageFileName_kongqi = os.path.join(imageFolder_kongqi, fname)
    imageData_kongqi = imread(imageFileName_kongqi).astype(float)
    kongqi += imageData_kongqi

kongqi /= numImages_kongqi

# Process each image and put them into a 3D array
for i, fname in enumerate(imageFiles):
    imageFileName = os.path.join(imageFolder, fname)
    imageData = imread(imageFileName).astype(float)
    imageData = (imageData - bendi) / (kongqi - bendi)
    
    imageData = resize(imageData, (m, n))
    imageData = rotate(imageData, -90, reshape=False)
    imageData = -np.log(imageData * 10)
    imageStack[:, :, i] = imageData

# Assuming 'projs', 'label', 'recon', 'projs1' are used elsewhere, we'll manage scope manually
projs = np.transpose(imageStack, (1, 2, 0))
projs -= np.min(projs)

# Further processing can be done as needed

# Saving projs or any other variable manipulation should be handled as required
#保存数据projs至temp文件夹
np.save('./temp/projs.npy', projs)