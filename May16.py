import math
import numpy as np

# D - Matrix search

def matrixSearch(A,x):

    rows,columns = np.shape(A)

    # Algorithm to find x
    i = 0
    j = columns-1
    while i <= rows-1 and j > -1:

        if A[i,j] == x:
            return [i+1,j+1]
        # Go left if bigger than x
        elif A[i,j] > x:
            j-=1

        # go one step down if smaller than x

        elif A[i,j] < x:
            i+=1

    return [0,0]


print(matrixSearch(np.array([[1,2,6,10],[3,7,7,13],[7,9,11,14]]), 9))














# ----------------------------------------------------------

# # D - Birthday problem
#
# def birthday(n):
#     k = 365
#     P = 1 - math.exp(math.lgamma(k+1)-math.lgamma(k-n+1)-n*math.log(k))
#
#     return P
#
# print(birthday(23))



# ----------------------------------------------------------

# # C -  Guess the gender
#
# def genderGuess(name):
#     vowels = "aeiouy"
#     if name[-1] in vowels:
#
#         if name.count('f') >= 2:
#
#             return 0.35
#
#         else:
#             return 0.87
#
#     if name[0] == "k":
#         return 0.69
#
#     else:
#         return 0.25
#
#
# print(genderGuess("affonso"))

# ----------------------------------------------------------

# # B - Alpha to phone number
#
# phoneDict = dict.fromkeys(['A', 'B', 'C'], '2')
# phoneDict.update(dict.fromkeys(['D','E','F'],'3'))
# phoneDict.update(dict.fromkeys(['G','H','I'],'4'))
# phoneDict.update(dict.fromkeys(['J','K','L'],'5'))
# phoneDict.update(dict.fromkeys(['M','N','O'],'6'))
# phoneDict.update(dict.fromkeys(['P','Q','R','S'],'7'))
# phoneDict.update(dict.fromkeys(['T','U','V'],'8'))
# phoneDict.update(dict.fromkeys(['W','X','Y','Z'],'9'))
#
#
#
# def alphaToPhone(alpha):
#     phone = ""
#     for i in range(len(alpha)):
#         if alpha[i].isdigit():
#             phone += alpha[i]
#         else:
#
#             phone += phoneDict[alpha[i]]
#
#     return phone
#
# print(alphaToPhone("4525DTU1"))

# ---------------------------------------------------------------

# # A - Exponential series expansion
#
# def eseries(x, N):
#     f = 0
#     for i in range(0,N):
#         f += x**i/math.factorial(i)
#
#
#
#     return f
#
# print(eseries(1.23,5))