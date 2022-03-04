from numpy import *
import matplotlib.pyplot as plt


def convert(x, default=0):
    try:
        return float(x)
    except:
        return default


def loadDataSet(