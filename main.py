import csv
from numpy import *
results = ones((385,1))
m = 25000
def loadData():
    with open('train_2.csv') as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            
def h(xi):
    return 1