# Required Packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Function to get data

def get_data(file_name):
    data = pd.read_csv(file_name)
    null, X_parameter, Y_parameter = np.hsplit(data.values,(0,385))
    for i in range(0, len(X_parameter)):
        X_parameter[i][0] = 1
    return np.mat(X_parameter), np.mat(Y_parameter)
def get_predict_data(file_name):
    data = pd.read_csv(file_name)
    X_parameter = []
    for id in data['id']:
        x = []
        for i in range(0, 384):
            x.append(float(data['value' + '%d' %i][id]))
        X_parameter.append(x)
    return X_parameter
if __name__ == '__main__':
    jResult = []
    results = np.mat(np.zeros((385,1)))
    alpha = 0.09
    file_name = 'test.csv'
    file_name = '../train_2.csv'
    x, y = get_data(file_name)
    m = len(x)
    doubleM_ = float(1)/(m*2)
    alpha_m = alpha/m
    for i in range(1,200000):
        tmp = x*results-y
        jResult.append(doubleM_*np.array(tmp.T*tmp)[0][0])
        results = results - alpha_m*(x.T*tmp)
        if i % 500 == 0:
            print jResult[i-1]
            print 'current :', i