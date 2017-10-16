import numpy as np
import math

# A - Pages in a booklet

# def bookPages(pagesContent):
#
#     pagesBooklet = 4 * (math.ceil(pagesContent/4))
#     return pagesBooklet

# -------------------------------------------------------------------

# B - Load balancing
# Only passing 7/10 tests.
# def loadBalance(runtime):
#     #runtime = np.array([5, 2.5, 17, 1.5, 22, 3.5])
#     sum = np.sum(runtime)
#     comp1 = np.array([])
#     difference = sum
#     for i in runtime:
#         if np.abs((np.sum(comp1) + runtime[0]) - np.sum(runtime)) < difference:
#             comp1 = np.append(comp1, runtime[0])
#             runtime = np.delete(runtime, 0)
#         else:
#             continue
#     k = len(comp1)
#     return k
#
# print(loadBalance(np.array([29.2, 43.2, 1.5, 98.4, 16.7, 10.6, 37.2])))

# --------------------------------------------------------------------

# C - Nearest color
# def nearestColor(r, g, b):
#
#     colorNames = np.array(["White", "Grey", "Black", "Red", "Maroon", "Yellow", "Olive",
#                            "Lime", "Green", "Aqua", "Teal", "Blue", "Navy", "Fuchsia", "Purple"])
#
#     R = np.array([100, 50, 0, 100, 50, 100, 50, 0, 0, 0, 0, 0, 0, 100, 50])
#     G = np.array([100, 50, 0, 0, 0, 100, 50, 100, 50, 100, 50, 0, 0, 0, 0])
#     B = np.array([100, 50, 0, 0, 0, 0, 0, 0, 0, 100, 50, 100, 50, 100, 50])
#
#     Dr = np.abs(R - r)
#     Dg = np.abs(G - g)
#     Db = np.abs(B - b)
#     D = np.vstack((Dr, Dg, Db))
#     D = np.amax(D, axis=0)
#     minD = np.amin(D)
#     colorName = colorNames[np.where(D == minD)][0]
#     return colorName
#
# print(nearestColor(75, 0, 0))

# -------------------------------------------------------------------------------------------------

# D - Mountain climb categorization

# def climbCategorization(distance, grade):
#
#     if distance < 2 or grade < 1 or distance*grade < 16:
#         categoryName = "Beginner"
#     elif 2 <= distance < 4 or 1<= grade < 2 or 16 <= (distance*grade) < 32:
#         categoryName = "Easy"
#     elif 4 <= distance < 8 or 2 <= grade < 4  or 32 <= (distance*grade) < 64:
#         categoryName = "Medium"
#     elif 8 <= distance < 12 or 4 <= grade < 6 or 64 <= (distance*grade) < 96:
#         categoryName = "Difficult"
#     else:
#         categoryName = "Extreme"
#
#     return categoryName
#
# print(climbCategorization(6,8))

# -------------------------------------------------------------------------------------------------

# E - Roam numerals

def romanToValue(roman):
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    L = len(roman)
    numbers = []

    for i in range(L):
        numbers.append(dict[roman[i]])

    numbers.reverse()
    runningTotal = 0
    maxSymbol = 0

    for i in range(len(numbers)):
        if numbers[i] >= maxSymbol:
            runningTotal += numbers[i]
            maxSymbol = numbers[i]
        elif numbers[i] < maxSymbol:
            runningTotal -= numbers[i]
    return runningTotal

print(romanToValue('XCIV'))
# dict = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
# roman = "XCIV"
# L = len(roman)
# numbers = []
#
#
# for i in range(L):
#     numbers.append(dict[roman[i]])
#
# numbers.reverse()
# runningTotal = 0
# maxSymbol = 0
#
#
# for i in range(len(numbers)):
#     if numbers[i] >= maxSymbol:
#         runningTotal += numbers[i]
#         maxSymbol = numbers[i]
#     elif numbers[i] < maxSymbol:
#         runningTotal -= numbers[i]
# print(runningTotal)



# Assignment A - Confidence interval

# def confidence(x):
#     m = np.mean(x)
#     s = np.std(x,ddof=1) # Delta Degrees of Freedom
#     n = len(x)
#     conf = []
#     low = m-2*(s/math.sqrt(n))
#     high = m+2*(s/math.sqrt(n))
#     conf.append(low)
#     conf.append(high)
#     return conf
#
# print(confidence([1,2,4,3,1]))