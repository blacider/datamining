# Required Packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
# Function to get data
values = 0.01
results = np.zeros((1,385))[0]
def get_data(file_name):
    data = pd.read_csv(file_name)
    X_parameter = []
    Y_parameter = []
    for id in data['id']:
        x = []
        for i in range(0, 384):
            x.append(float(data['value' + '%d' %i][id]))
        X_parameter.append(x)
    for single_price_value in data['reference']:
        Y_parameter.append(float(single_price_value))
    return X_parameter, Y_parameter
def get_predict_data(file_name):
    data = pd.read_csv(file_name)
    X_parameter = []
    for id in data['id']:
        x = []
        for i in range(0, 384):
            x.append(float(data['value' + '%d' %i][id]))
        X_parameter.append(x)
    return X_parameter
def h(x_p):
    x_ = [1]
    return np.dot(results, np.array(np.concatenate((x_, x_p))))
def reg(x, y):
    hh = []
    for i in range(0, len(x)):
        hh.append(h(x[i]))
    for j in range(0, len(results)):
        sum = 0.0
        for i in range(0, len(x)):
            sum += (hh[i]-y[i])*(x[i][j-1] if j > 0 else 1)
            sum /= len(x)
            sum *= 0.01
        results[j] -= sum

