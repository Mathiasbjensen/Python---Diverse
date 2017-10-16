# June 2017
import math
import numpy as np



# B - Temperature Sensor Model

# def Sensor(Ta1, Ta2, T0, r, tlag, t):
#     T = (t >= tlag) * (Ta2 - (Ta2 - T1(Ta1, T0, r, tlag)) * np.exp(-r * (t - tlag))) + (t < tlag) * T1(Ta1, T0, r, t)
#
#     return T
#
#
# def T1(Ta1, T0, r, t):
#     Tlag = Ta1 - (Ta1 - T0) * np.exp(-r * t)
#     return Tlag


def Sensor(Ta1,Ta2,T0,r,tlag,t):
    T = []
    for i in t:
        if t[i] < tlag:
            x = Ta1-(Ta1-T0)*math.exp(-r*t[i])
            T.append(x)

        else:
            y = Ta2-(Ta2-(Ta1-(Ta1-T0)*math.exp(-r*tlag)))*math.exp(-r*(t[i]-tlag))
            T.append(y)

    T = np.asarray(T)
    return T
print(Sensor(16.7,21.,18.5,0.09,2.5,np.array([0,1,2,3,4,5,6,7,8,9])))


# E - Seat Allocation
#
# def SeatAllocation(x):
#     row = int(x[0]) - 1
#     column = x[1]
#
#     dict = {'A': 1, 'B': 2, 'C': 3}
#     row1 = ['1', 'A', 'X', 'C', 'D']
#     row2 = ['2', 'A', 'B', 'C', 'D']
#     row3 = ['3', 'A', 'B', 'C', 'X']
#     row4 = ['4', 'A', 'B', 'C', 'D']
#     row5 = ['5', 'X', 'B', 'C', 'D']
#
#     seatsInit = [row1, row2, row3, row4, row5]
#
#     # should probably be optimized
#     if seatsInit[row][dict[column]] != 'X':
#         seatsInit[row][dict[column]] = 'X'
#         print('You are lucky, seat ' + x + ' is not yet taken')
#     else:
#         print('Seat ' + x + ' is already taken')
#
#     seats = ""
#     # For loop to remove ' and ,
#     # [1:-1] is basically a hackfix to remove  '[' and ']' from the new string.
#     for item in seatsInit:
#         seats = seats + str(item)[1:-1].replace(',', '').replace("'", "") + '\n'
#
#     return(seats)
#
# print(SeatAllocation('3C'))
