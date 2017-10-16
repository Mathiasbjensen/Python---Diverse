vector = [1,2,3,4,5,-1,-2,-3,-4,-5]

# Operation on all elements in vector:

opx = [3*i for i in vector]
print(opx)

# Do an operation but keep the initial element
opx2 = [[i, i**2] for i in vector]
print(opx2)

# Filter the list using a predicate

filter = [i for i in vector if i > 2]
print(filter)

filterx2 = [3*i for i in vector if i > 2]
print(filterx2)