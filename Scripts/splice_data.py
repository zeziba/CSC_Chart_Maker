"""
Created By: Charles Engen
Date: November 17. 2016

Use this module by calling with python3 as follows
    python3 splice_data.py {number of slices to make: overrides inbuit number}

"""


import pandas
import os.path as path
import sys

fMin = 900


with open("LOG0_new.CSV", "r") as old_file:
    count = 0
    data = pandas.read_csv(old_file)
    dMax = int(data.max(numeric_only=True)[0])
    cSize = 30 if len(sys.argv) <= 1 else int(list(sys.argv)[1])
    ranges = [int(dMax / cSize) * i for i in range(1, 30 if len(sys.argv) <= 1 else int(list(sys.argv)[1]) + 1)]
    for index, i in enumerate(ranges):
        if index > 0:
            data[ranges[index - 1]: i - 1].to_csv("LOG0_spC%s.CSV" % index, sep=",", index=False)
        else:
            data[0: i].to_csv("LOG0_spC%s.CSV" % index, sep=",", index=False)
