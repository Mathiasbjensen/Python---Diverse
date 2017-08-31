from tkinter import *
import re
import math
import numpy as np
import itertools
import collections

# def callback(sv):
#     print(sv.get())
#
# root = Tk()
# sv = StringVar()
# sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
# e = Entry(root, textvariable=sv)
# e.pack()
# root.mainloop()

#my_string = "hello python world , i'm a beginner world, skod"
#print(my_string.split("world",1)[1])

#price = " |   $499.99   | "
#print(re.findall(r"[$](\w+)",price))

# name = "sofffie"
#
# print(name.count('f'))

#A = np.array([[1,2,6,10],[3,7,7,13],[7,9,11,14]])

#print(np.size(A,axis=0))
#print(np.size(A,axis=1))

#print(np.shape(A))
#print(A)


#d = {'0':'0', '1':'2', '2':'4', '3':'6', '4':'8', '5':'1', '6':'3', '7':'5', '8':'7', '9':'9'}

#
# checksum=""
# checksum+=d['0']
# print(checksum)
# print(len(checksum))

# x=[1,3]
# y=[1,1]
# i=0
# j=1
#
# print(math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2))

# print(np.array([[1, 2, 6, 10], [3, 7, 7, 13]]))
#
# print(np.array([[1, 2, 6, 10], [3, 7, 7, 13]])*np.array([[1, 2, 6, 10], [3, 7, 7, 13]]))

#
# coordinates = np.array([[1,3,3,4,7,6,1],[1,1,2,3,3,5,5]])
# center = np.array([3,1])
# theta = -math.pi/3
# scale = 2
# centerab = np.array([coordinates[0,-1]-center[0],coordinates[1,-1]-center[1]])
#
# myMatrix = np.array([[math.cos(theta), -math.sin(theta)],[math.sin(theta), math.cos(theta)]])
#
#
# #print(coordinates)
# #print(coordinates[1,-1])
#
#
# #print(centerab)
#
# newCoordinates = myMatrix.dot(centerab)*scale+center
#
# print(newCoordinates)

# -----------------------------------

# extraOptions = ['Cruise control', 'Air conditioning', 'Alloy wheels', 'Chrome spoiler']
# extraOptionsCombinations = []
# stuff=[]
# # Start at 1 to avoid '()'
# for L in range(1, len(extraOptions)+1):
#     for subset in itertools.combinations(extraOptions, L):
#         stuff.append(subset)
#
# print("skod")
# print(stuff[13])


# ----------------------------------------

extraOptionsKey1 = [0,4000,8000,13000,7000]
extraOptionsValue1 = ['Access', 'Cruise control', 'Air conditioning', 'Alloy wheels', 'Chrome spoiler']

extraOptionsKey2 = [22000,4000,8000,13000,7000]
extraOptionsValue2 = ['Comfort', 'Cruise control', 'Air conditioning', 'Alloy wheels', 'Chrome spoiler']

extraOptionsKey3 = [44000,4000,8000,13000,7000]
extraOptionsValue3 = ['Sport', 'Cruise control', 'Air conditioning', 'Alloy wheels', 'Chrome spoiler']

extraOptionsCombinations = []
stuffKeys=[]
stuffValues=[]

# For Trim Level = Access:
for L in range(1, len(extraOptionsKey1)+1):
    for subset in itertools.combinations(extraOptionsKey1, L):
        if 0 not in subset:
            continue
        else:
            stuffKeys.append(subset)

for L in range(1, len(extraOptionsValue1)+1):
    for subset in itertools.combinations(extraOptionsValue1, L):
        if 'Access' not in subset:
            continue
        else:
            stuffValues.append(subset)


# For Trim Level = Comfort:

for L in range(1, len(extraOptionsKey2)+1):
    for subset in itertools.combinations(extraOptionsKey2, L):
        #if subset not in stuffKeys:
        if 22000 not in subset:
            continue
        else:
            stuffKeys.append(subset)

for L in range(1, len(extraOptionsValue2)+1):
    for subset in itertools.combinations(extraOptionsValue2, L):
        #if subset not in stuffValues:
        if 'Comfort' not in subset:
            continue
        else:
            stuffValues.append(subset)

# For Trim Level = Sport:

for L in range(1, len(extraOptionsKey3)+1):
    for subset in itertools.combinations(extraOptionsKey3, L):
        #if subset not in stuffKeys:
        if 44000 not in subset:
            continue
        else:
            stuffKeys.append(subset)

for L in range(1, len(extraOptionsValue3)+1):
    for subset in itertools.combinations(extraOptionsValue3, L):
        #if subset not in stuffValues:
        if 'Sport' not in subset:
            continue
        else:
            stuffValues.append(subset)

# Adding all the combinations to a dictionary, with price as keys and strings as the values of the dict.

dict = {}
for i in range(len(stuffKeys)):
    dict[sum(stuffKeys[i])]=stuffValues[i]

# Sorting the dictionary by keys, so lowest price will be the first key index.
od = collections.OrderedDict(sorted(dict.items()))

print(od[0])

maxPrice = 170500

#whacky forloop since using while loop through dictionary keys was weird.
for key in od.keys():
    #print(key)
    if key > maxPrice-159000:
        #print(key)
        #print(od[temp])
        break

    else:
        # This temp value is just to be able to get the previous key value.
        temp=key






# print("skod")
print(len(stuffValues))
# print(len(stuffKeys))
print(*stuffKeys, sep='\n')

# print(stuffKeys[13])
# print("This will hopefully be the sum, lol:")
# print(sum(stuffKeys[13]))
# print("THIS SHOULD BE STRINGS:")
# print(stuffValues[13])
#
# dict={}
# dict[sum(stuffKeys[13])]=stuffValues[13]
# print("Here comes the dictionary!")
# print(dict[28000])

for i in dict:
    print("Key: %s, value: %s" % (i, dict[i]))


# -----------------------------------------




