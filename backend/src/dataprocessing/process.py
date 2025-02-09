import kagglehub
import os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing import image_dataset_from_directory

# Download dataset
dataset_path = kagglehub.dataset_download(
    "alistairking/recyclable-and-household-waste-classification"
)
dataset_path = dataset_path.rstrip("/")  # Ensure correct path format

# Define dataset directories
train_dir = os.path.join(dataset_path, "train")
test_dir = os.path.join(dataset_path, "test")

# Load datasets into TensorFlow format
img_size = (224, 224)  # Standard input size for CNNs
batch_size = 32

train_ds = image_dataset_from_directory(
    train_dir, image_size=img_size, batch_size=batch_size
)
test_ds = image_dataset_from_directory(
    test_dir, image_size=img_size, batch_size=batch_size
)

# Class names
class_names = train_ds.class_names
print("Class labels:", class_names)
