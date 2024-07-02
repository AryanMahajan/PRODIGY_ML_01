from loading_data import create_testing_data
from train_model import train_model
from data_cleaning import data_cleaning

import os
import pickle
import csv
import numpy as np


#Cleaning the given data
data_cleaning()

#Checking if the model exists or not
if os.path.exists("model.pickle"):
    print("Model exists")
    model = pickle.load(open("model.pickle", "rb"))
else:
    print("Training Model")
    train_model()
    model = pickle.load(open("model.pickle", "rb"))

#Checking if the data is saved or not
if os.path.exists("X_test.pickle"):
    print("LOADING TEST DATA")
    x_test = np.array(pickle.load(open("X_test.pickle", "rb")))
else:
    create_testing_data()
    print("LOADING TEST DATA")
    x_test = np.array(pickle.load(open("X_test.pickle", "rb")))

predictions = []

prediction = model.predict(x_test)
predictions.append(prediction)
print(predictions)

with open('result.csv', 'a', newline='\n') as f:
    writer = csv.writer(f)
    writer.writerows(predictions)
