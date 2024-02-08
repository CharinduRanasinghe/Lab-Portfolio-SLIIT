import os
import cv2
import numpy as np
import random
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from google.colab import drive
drive.mount('/content/drive')

data_dir = "C:/Users/chari/OneDrive/Documents/fruits_dataset"

categories = ["Apple", "Banana", "Grapes", "Mango", "Strawberry"]

train_test_split_ratio = 0.8

for category in categories:
    path = os.path.join(data_dir, category)

    train_dir = os.path.join(data_dir, "train", category)
    test_dir = os.path.join(data_dir, "test", category)

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    image_files = [f for f in os.listdir(path) if f.endswith(".jpg")]
    num_images = len(image_files)

    num_train_images = int(num_images * train_test_split_ratio)

    for i, image_file in enumerate(image_files):
        src_path = os.path.join(path, image_file)
        if i < num_train_images:
            dst_path = os.path.join(train_dir, image_file)
        else:
            dst_path = os.path.join(test_dir, image_file)
        os.rename(src_path, dst_path)

data_dir = "C:/Users/chari/OneDrive/Documents/fruits_dataset/train"

def load_data(data_dir):
    data = []

    for category in categories:
        path = os.path.join(data_dir, category)
        label = categories.index(category)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv2.imread(img_path)
            img_array = cv2.resize(img_array, (100, 100)) 
            data.append([img_array, label])

    random.shuffle(data)

    X = []
    y = []

    for features, label in data:
        X.append(features)
        y.append(label)

    X = np.array(X).reshape(-1, 100, 100, 3)  
    X = X / 255.0 
    y = to_categorical(y, num_classes=len(categories)) 

    return X, y

X, y = load_data(data_dir)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = keras.Sequential([
    layers.Flatten(input_shape=(100, 100, 3)),  
    layers.Dense(128, activation='relu'),     
    layers.Dropout(0.5),                     
    layers.Dense(len(categories), activation='softmax')  
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=5, batch_size=32, validation_split=0.2)

test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=2)
print(f"Test accuracy: {test_accuracy * 100:.2f}%")

def preprocess_image(image_path):
    img_array = cv2.imread(image_path)
    img_array = cv2.resize(img_array, (100, 100)) 
    img_array = img_array / 255.0 
    img_array = img_array.reshape(-1, 100, 100, 3) 
    return img_array

image_path = "C:/Users/chari/OneDrive/Documents/fruits_dataset/single_prediction/fruit.jpg"
input_image = preprocess_image(image_path)
predictions = model.predict(input_image)
predicted_class_index = np.argmax(predictions)
predicted_class = categories[predicted_class_index]

print(f"The model predicts this image is a {predicted_class}.")
