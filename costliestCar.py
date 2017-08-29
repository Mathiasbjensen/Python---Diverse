import itertools
import collections

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