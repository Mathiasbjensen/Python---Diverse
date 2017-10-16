# January 2017 exam

import numpy as np
import math

# Assignment A - Heron's formula

# def trianglearea(a, b, c):
#     if a+b > c and a+c > b and b+c > a:
#         p = 1/2*(a+b+c)
#         A = math.sqrt(p*(p-a)*(p-b)*(p-c))
#     else:
#         A = 0
#     return A
#
# print(trianglearea(4.5,6.,7.5))

# ----------------------------------------------------------------------------------------

# Assignment B - Day of the week
#
# def polygonarea(x, y):
#     dets = 0
#     length = len(x)
#     for i in range(len(x)):
#         i2 = (i+1) % length
#         dets = dets + (x[i]*y[i2] - y[i]*x[i2])
#
#     A = 1/2*dets
#
#     return A
#
# print(polygonarea([1,3,3,4,7,6,1],[1,1,2,3,3,5,5]))

# ----------------------------------------------------------------------------------------

# Assignment C - Fitting a polynomial

# def fitpolynomial(x, y, n):
#     W = x.reshape(-1,1) ** np.arange(n+1)
#     WT =  np.transpose(W)
#     a = np.dot(np.linalg.inv(np.dot(WT, W)), np.dot(WT, y))
#     return a
#
# print(fitpolynomial(np.array([-2,-1.5,-1,-0.5,0,0.5,1,1.5,2]),
#                     np.array([2.1, 0.6, -1.5, -1.6, -1.9, -2, -1.1, 0.3, 2.7]), 3))

# ----------------------------------------------------------------------------------------

# Assignment D - Predictability of a number of sequence

# def predictability(x):
#     q = []
#     for i in x:
#         np.append(q,x.count(i)+1)
#
#     return P

# N = 15
# q = []
# x = np.array([1,5,5,3,5,1,3,5,4,5,4,1,5,5,4])
# q = np.bincount(x)
# q = q[1:]
# print(q)
#
# for i in range(1,N):
#
# # R ER JO HELT BLÆST
# P = (q[0]/N)

# ----------------------------------------------------------------------------------------

# Assignment E - Syllable counter

# Syllables: equal to number of voewels in a word. Except the last vowel, and 2<= vowels
# only counts as 1.

def syllables(word):
    vowels = "aeiouy"
    l = len(word)
    N = 0
    # Using a "state" to tell whether we've hit a vowel or not. Only adding to N when
    # We've hit a vowel and we hit a consonant.
    vowelState = False
    for i in range(l):
        if word[i] in vowels:
            vowelState = True
        else:
            if vowelState:
                N+=1
                vowelState = False
    return N
