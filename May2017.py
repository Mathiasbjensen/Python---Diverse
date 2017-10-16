import numpy as np
import math

# A - Sale price

# def salePrice(prices):
#     prices = np.sort(prices)
#     prices = prices[::-1]
#     new_prices = prices[0::2]
#     total = np.sum(new_prices)
#     return total
# print(salePrice(np.array([9.95, 129.50, 9.95, 40.00, 17.75])))

# ----------------------------------------------------------------------

# B - ISBN-10 check  digit

# def ISBNCheckDigit(isbn):
#     vec = np.array([1,2,3,4,5,6,7,8,9])
#     check1 = isbn*vec
#     check1 = np.sum(check1)
#     checkdone = check1 % 11
#
#     if checkdone == 10:
#         checkDigit = "X"
#
#     else:
#         checkDigit = str(checkdone)
#     return checkDigit
#
# print(ISBNCheckDigit(np.array([1,5,8,4,8,8,3,8,8])))

# ----------------------------------------------------------------------

# C - Partial correlation

# def partialCorrelation(X):
#     N = np.size(X, 0)
#     first = np.dot(np.transpose(X), X)
#     second = 1 / 5 * first
#     C = np.linalg.inv(second)
#     # Initializing P - same size as C.
#     P = np.empty((np.size(C, 0), np.size(C, 1)))
#     row = np.size(P, 0)
#     col = np.size(P, 1)
#
#     # print(P)
#
#     for i in range(row):
#         for j in range(col):
#             if i == j:
#                 P[i][j] = 1
#             else:
#                 P[i][j] = -C[i][j] / math.sqrt(C[j][j] * C[i][i])
#
#     return P
#
# print(partialCorrelation(np.array([[-.1, .4, -1],[3.4, 1.8, -1],[-1.9, -1.5, .7],[.8, 1.6, 4.4],[.7, 1, 3]])))

# ----------------------------------------------------------------------

# D - Zero crossing

def zeroCrossing(signal):
    count = 0
    if signal[0] < 0:
        pos = False
    else:
        pos = True

    for i in range(len(signal)):
        if pos == True and signal[i] < 0:
            pos = False
            count += 1
        elif pos == False and signal[i] > 0:
            pos = True
            count += 1
        else:
            continue

    return count

