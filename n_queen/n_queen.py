import numpy

n = numpy.random.randint(1, 10)  # királynők száma
chess_table = numpy.zeros((n, n))
column = 0
row = 0


def is_safe(n, table, row, column):
    for i in range(column):
        if table[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if table[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(column, -1, -1)):
        if table[i][j] == 1:
            return False

    return True


def place_queen(n, table, column):
    if column >= n:
        return True

    for i in range(n):
        if is_safe(n, table, i, column):
            table[i][column] = 1

            if place_queen(n, table, (column + 1)) == True:
                return True

            table[i][column] = 0

    return False


print(place_queen(n, chess_table, column))
print(chess_table)
