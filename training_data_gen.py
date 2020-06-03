import numpy as np
import os
from matplotlib import pyplot as plt
import cv2
import random
import pickle


file_list = []
class_list = []

DATADIR = "/Users/ahaan/Documents/Ahaan/Food_Classification/selenium_pictures"

# All the categories you want your neural network to detect
CATEGORIES = ['banana', 'burger', 'butter_chicken', 'chocolate_cake', 'dal', 'donut', 'dosa', 'fish_curry', 'fried_rice', 'hakka_noodles', 'icecream', 'idli', 'naan', 'paratha', 'penne_alfredo', 'pesto_pasta', 'pizza', 'salad', 'tacos', 'waffles']

# The size of the images that your neural network will use
IMG_SIZE = 64

training_data = []
validation_data = []


def create_training_data():
    test = np.zeros(len(CATEGORIES)).tolist()
    test[0] = 1
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = test
        test = test[-1:] + test[:-1]
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img))
                img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                if(np.random.rand(1) > 0.2):
                    training_data.append([new_array, class_num])
                else:
                    validation_data.append([new_array, class_num])
            except Exception as e:
                pass


create_training_data()

random.shuffle(training_data)
random.shuffle(validation_data)

X_train = []  # features
y_train = []  # labels

X_validation = []
y_validation = []

for features, label in training_data:
    X_train.append(features)
    y_train.append(label)

for features, label in validation_data:
    X_validation.append(features)
    y_validation.append(label)

X_train = np.array(X_train)
X_validation = np.array(X_validation)
y_train = np.array(y_train)
y_validation = np.array(y_validation)

# Creating the files containing all the information about your model
pickle_out = open("X_train.pickle", "wb")
pickle.dump(X_train, pickle_out)
pickle_out.close()

pickle_out = open("y_train.pickle", "wb")
pickle.dump(y_train, pickle_out)
pickle_out.close()

pickle_out = open("X_validation.pickle", "wb")
pickle.dump(X_validation, pickle_out)
pickle_out.close()

pickle_out = open("y_validation.pickle", "wb")
pickle.dump(y_validation, pickle_out)
pickle_out.close()
