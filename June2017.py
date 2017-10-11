# June 2017

# E - Seat Allocation

def SeatAllocation(x):
    row = int(x[0]) - 1
    column = x[1]
    dict = {'A': 1, 'B': 2, 'C': 3, 'X': 'Taken'}
    row1 = ['1', 'A', 'X', 'C', 'D']
    row2 = ['2', 'A', 'B', 'C', 'D']
    row3 = ['3', 'A', 'B', 'C', 'X']
    row4 = ['4', 'A', 'B', 'C', 'D']
    row5 = ['5', 'X', 'B', 'C', 'D']

    seatsInit = [row1, row2, row3, row4, row5]

    # should probably be optimized
    if seatsInit[row][dict[column]] != 'X':
        seatsInit[row][dict[column]] = 'X'
        print('You are lucky, seat ' + x + ' is not yet taken')
    else:
        print('Seat ' + x + ' is already taken')

    seats = ""
    # For loop to remove ' and ,
    for item in seatsInit:
        seats = seats + str(item)[1:-1].replace(',', '').replace("'", "") + '\n'

    return(seats)

print(SeatAllocation('3C'))
