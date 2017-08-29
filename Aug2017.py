import numpy as np
import math
import itertools
import collections

# # Assignment A - Color hue
#
# def rgb2hue(R, G, B):
#     H=0
#     delta = max(R,G,B)-min(R,G,B)
#
#     if R == max(R,G,B):
#         H = 60*(G-B)/delta
#
#     elif G == max(R,G,B):
#         H = 120+60*(B-R)/delta
#
#     elif B == max(R,G,B):
#         H = 240+60*(R-G)/delta
#
#     if H < 0:
#         H+=360
#
#     return H
#
#
# print(rgb2hue(0.6, 0.2, 0.3))


# ---------------------------------------------

# # Assignment B - Credit card validation
#
# def cardValidation(cardnumber):
#     checksum = 0
#     d = {'0': '0', '1': '2', '2': '4', '3': '6', '4': '8', '5': '1', '6': '3', '7': '5', '8': '7', '9': '9'}
#     for i in range(len(cardnumber)):
#         if i % 2 == 0:
#             checksum += int(d[cardnumber[i]])
#             print(checksum)
#         else:
#             checksum += int(cardnumber[i])
#
#     return checksum
#
# print(cardValidation("4024007156748096"))

# ---------------------------------------------

# # Assignment C - Perimeter of a polyon
#
# def polygonPerimeter(x, y):
#     P=0
#     for i in range(len(x)-1):
#         j=i+1
#
#         P += math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
#
#     max = len(x)-1
#     P += math.sqrt((x[max]-x[0])**2+(y[max]-y[0])**2)
#
#
#     return P
#
# print(polygonPerimeter([1,3,3,4,7,6,1],[1,1,2,3,3,5,5]))

# ---------------------------------------------

# # Assignment D - Rotation and scaling
#
# def rotateScale(coordinates, center, theta, scale):
#
#     centerab = np.array([coordinates[0, -1] - center[0], coordinates[1, -1] - center[1]])
#
#     myMatrix = np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])
#
#     newCoordinates = myMatrix.dot(centerab) * scale + center
#
#     return newCoordinates
#
# print(rotateScale(np.array([[1,3,3,4,7,6,1],[1,1,2,3,3,5,5]]), np.array([3, 1]), -math.pi/3, 2))
#
# # ---------------------------------------------

# Assignment E - Costliest car within budget

def costliestCar(maxPrice):

    # Defining the 2x3 arrays with keys and values which i'll power set.
    basePrice = 159000
    extraOptionsKey1 = [0, 4000, 8000, 13000, 7000]
    extraOptionsValue1 = ['Access', 'Cruise control', 'Air conditioning', 'Alloy wheels', 'Chrome spoiler']

    extraOptionsKey2 = [22000, 4000, 8000, 13000, 7000]
    extraOptionsValue2 = ['Comfort', 'Cruise control', 'Air conditioning', 'Alloy wheels', 'Chrome spoiler']

    extraOptionsKey3 = [44000, 4000, 8000, 13000, 7000]
    extraOptionsValue3 = ['Sport', 'Cruise control', 'Air conditioning', 'Alloy wheels', 'Chrome spoiler']

    extraOptionsCombinations = []
    stuffKeys = []
    stuffValues = []

# For loops adding all the combinations of keys/values to the key and value list.
    # For Trim Level = Access:
    for L in range(1, len(extraOptionsKey1) + 1):
        for subset in itertools.combinations(extraOptionsKey1, L):
            if 0 not in subset:
                continue
            else:
                stuffKeys.append(subset)

    for L in range(1, len(extraOptionsValue1) + 1):
        for subset in itertools.combinations(extraOptionsValue1, L):
            if 'Access' not in subset:
                continue
            else:
                stuffValues.append(subset)

    # For Trim Level = Comfort:

    for L in range(1, len(extraOptionsKey2) + 1):
        for subset in itertools.combinations(extraOptionsKey2, L):
            # if subset not in stuffKeys:
            if 22000 not in subset:
                continue
            else:
                stuffKeys.append(subset)

    for L in range(1, len(extraOptionsValue2) + 1):
        for subset in itertools.combinations(extraOptionsValue2, L):
            # if subset not in stuffValues:
            if 'Comfort' not in subset:
                continue
            else:
                stuffValues.append(subset)

    # For Trim Level = Sport:

    for L in range(1, len(extraOptionsKey3) + 1):
        for subset in itertools.combinations(extraOptionsKey3, L):
            # if subset not in stuffKeys:
            if 44000 not in subset:
                continue
            else:
                stuffKeys.append(subset)

    for L in range(1, len(extraOptionsValue3) + 1):
        for subset in itertools.combinations(extraOptionsValue3, L):
            # if subset not in stuffValues:
            if 'Sport' not in subset:
                continue
            else:
                stuffValues.append(subset)

    # Adding all the combinations to a dictionary, with price as keys and strings as the values of the dict.

    dict = {}
    for i in range(len(stuffKeys)):
        dict[sum(stuffKeys[i])] = stuffValues[i]

    # Sorting the dictionary by keys, so lowest price will be the first key index.
    od = collections.OrderedDict(sorted(dict.items()))



    # whacky forloop since using while loop through dictionary keys was weird.
    for key in od.keys():
        if key > maxPrice - basePrice:
            carSpecification = od[temp]
            return carSpecification

        else:
            # This temp value is just to be able to get the previous key value.
            temp = key


print(costliestCar(205000))

