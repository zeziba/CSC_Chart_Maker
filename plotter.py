"""
Created By: Charles Engen
    Purpose of this program is to visually display graphs of varying types for
    the Colorado Space Consortium's Pueblo Community College team for the 2016
    Balloon Challenge. It will display one graph at a time until all data has been
    fed to the user.
"""
# Need numpy, matplotlib, pandas in order to run

import os
import os.path as PATH
import sys
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Failed to import matplotlib, please install before using.")
    input()
    sys.exit()
try:
    import pandas
except ImportError:
    print("Failed to import pandas, please install before using.")
    input()
    sys.exit()


def _get_data(path):
    return pandas.read_csv(path)


def get_plot_data(path):
    temp = dict()
    _data = _get_data(path)
    for name in list(_data):
        t = _data["%s" % name].tolist()
        temp[name] = list()
        for index, item in enumerate(t):
            temp[name].append(float(t[index]))
    return temp


def plot_data(path):
    data = get_plot_data(path)
    ti = [t for t in list(data) if "time" in t.lower() or "ms" in t.lower()][0]
    plt.figure()
    for index, name in enumerate(list(data)):
        if "ms" not in name.lower() and "time" not in name.lower():
            plt.plot(data[ti], data[name])
            plt.title("Solar Data")
            plt.ylabel("%s" % name)
            plt.xlabel("%s" % ti)
            plt.show()


if __name__ == "__main__":
    files = [PATH.join(os.getcwd(), "DATA", f) for f in os.listdir(PATH.join(os.getcwd(), "DATA"))]
    for file in files:
        plot_data(file)
