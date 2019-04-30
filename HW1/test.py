import numpy as np
import csv
import os


def read_train_data():
    # read data
    text = open('c:/Users/willia96/Desktop/机器学习/NTU_ML2017_Hung-yi-Lee_HW/HW1/data/train.csv', 'r', encoding='big5')
    data = csv.reader(text, delimiter=',')
    res = []
    row = 0
    for item in data:
        if row % 18 == 10:
            tmp = []
            for i in range(3, 27):
                if item[i] == "NR":
                    tmp.append(float(0))
                else:
                    tmp.append(float(item[i]))
            res.append(tmp)
        row = row + 1
    return res


def process_train_data(data):
    x = []
    y = []
    for item in data:
        for i in range(15):
            x.append(item[i:i+9])
            y.append(item[i+9])
    x = np.array(x)
    y = np.array(y)
    print(x.shape, y.shape)


def gd(x, y):
    pass


if __name__ == '__main__':
    process_train_data(read_train_data())



