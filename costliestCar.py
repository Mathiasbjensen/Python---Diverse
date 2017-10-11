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
            if 0 in subset:
                stuffKeys.append(subset)

        for subset1 in itertools.combinations(extraOptionsValue1, L):
            if 'Access' in subset1:
                stuffValues.append(subset1)

    # For Trim Level = Comfort:
    for L in range(1, len(extraOptionsKey2) + 1):
        for subset in itertools.combinations(extraOptionsKey2, L):
            if 22000 in subset:
                stuffKeys.append(subset)

        for subset1 in itertools.combinations(extraOptionsValue2, L):
            if 'Comfort' in subset1:
                stuffValues.append(subset1)

    # For Trim Level = Sport:
    for L in range(1, len(extraOptionsKey3) + 1):
        for subset in itertools.combinations(extraOptionsKey3, L):
            if 44000 in subset:
                stuffKeys.append(subset)

        for subset1 in itertools.combinations(extraOptionsValue3, L):
            if 'Sport' in subset1:
                stuffValues.append(subset1)

    #print(*stuffValues, sep='\n')

    # Adding all the combinations to a dictionary, with price as keys and strings as the values of the dict.

    dict = {}
    for i in range(len(stuffKeys)):
        dict[sum(stuffKeys[i])] = stuffValues[i]

    # Sorting the dictionary by keys, so lowest price will be the first key index.
    od = collections.OrderedDict(sorted(dict.items()))

    dictList = list(od.keys())
    highestPossiblePrice = dictList[-1]

    if maxPrice > highestPossiblePrice + basePrice:
        return od[dictList[-1]]

    # whacky forloop since using while loop through dictionary keys was weird.
    for key in od.keys():
        if key > maxPrice - basePrice:
            skod = str(od[temp])
            skod2 = skod.replace("(", "")
            skod3 = skod2.replace(")", "")
            skod4 = skod3.replace("'", "")
            return skod4

        else:
            # This temp value is just to be able to get the previous key value.
            temp = key


print(costliestCar(170500))