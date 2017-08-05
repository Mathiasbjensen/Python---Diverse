import numpy as np
import math

def Sensor(Ta1, Ta2, T0, r, t, tlag):


    for i in range(0,9):
        if t[i] < tlag:
            T = Ta1-(Ta1-T0)*math.exp(-r*t[i])

        if t[i] >= tlag:


    return T

# Not done