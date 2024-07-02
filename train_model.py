from sklearn.linear_model import LinearRegression
import pickle
import os
import numpy as np

from loading_data import create_training_data

if os.path.exists("X_train.pickle") and os.path.exists("y_train.pickle"):
    print("LOADING TRAINING DATA")
    x_train = np.array(pickle.load(open("X_train.pickle", "rb")))
    y_train = np.array(pickle.load(open("y_train.pickle", "rb")))
else:
    create_training_data()
    print("LOADING TRAINING DATA")
    x_train = np.array(pickle.load(open("X_train.pickle", "rb")))
    y_train = np.array(pickle.load(open("y_train.pickle", "rb")))

def train_model():

    model = LinearRegression()
    model.fit(x_train, y_train)
    pickle.dump(model, open("model.pickle", "wb"))
    open("model.pickle").close()
