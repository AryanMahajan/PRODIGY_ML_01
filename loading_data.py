import csv
import pickle
import numpy as np

def create_training_data():
  # Loads, processes, and pickles test data into lists of lists of integers.

    area, bathrooms, bedrooms, sales_price = [], [], [], []
    with open(r"Data\train.csv", 'r') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        next(rows)  # Skip the header row
        for row in rows:
            area.append(int(row[1]))
            bathrooms.append(int(row[2]))
            bedrooms.append(int(row[3]))
            sales_price.append(int(row[4]))

    x_train = np.array([[a, b, c] for a, b, c in zip(area, bathrooms, bedrooms)])
    y_train = np.array(sales_price)

    pickle_x_train_out = open("X_train.pickle", "wb")
    pickle.dump(x_train, pickle_x_train_out)
    pickle_x_train_out.close()

    pickle_y_train_out = open("y_train.pickle", "wb")
    pickle.dump(y_train, pickle_y_train_out)
    pickle_y_train_out.close()

def create_testing_data():
  # Loads, processes, and pickles test data into lists of lists.

    area, bathrooms, bedrooms = [], [], []
    with open(r"Data\test.csv", 'r') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        next(rows)  # Skip the header row
        for row in rows:
            area.append(int(row[1]))  # Assuming area can also have decimals
            bathrooms.append(int(row[2]))  # Convert bathroom value to float
            bedrooms.append(int(row[3]))  # Assuming bedrooms can also have decimals


    x_test = np.array([[a, b, c] for a, b, c in zip(area, bathrooms, bedrooms)])

    pickle_x_test_out = open("X_test.pickle", "wb")
    pickle.dump(x_test, pickle_x_test_out)
    pickle_x_test_out.close()

def create():
    create_training_data()
    create_testing_data()

create()