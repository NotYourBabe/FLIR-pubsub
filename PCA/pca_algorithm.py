from numpy import *
import matplotlib.pyplot as plt


def convert(x, default=0):
    try:
        return float(x)
    except:
        return default


def loadDataSet(fileName, delim='\t'):
    fr = open(fileName)
    stringArr = [line.strip().split(delim) for line in fr.readlines()]
    datArr = [[ convert(eachVal) for eachVal i