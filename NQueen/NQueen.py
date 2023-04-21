import numpy

n = numpy.random.randint(1, 10)  # királynők száma
chess_table = numpy.zeros((n, n))
column = 0
row = 0


# királynők nem ütik-e ki egymást, adott pozícióból, bal oldalon
def is_safe(n, table, row, column):
    # balra
    for i in range(column):
        if table[row][i] == 1:
            return False

    # balra fel
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if table[i][j] == 1:
            return False

    # balra le
    for i, j in zip(range(row, n, 1), range(column, -1, -1)):
        if table[i][j] == 1:
            return False

    return True


# királynő elhelyezése (adott oszlopnál)
def place_queen(n, table, column):
    # (királynőt sikerült elhelyezni az utolsó oszlopnál)
    if column >= n:
        return True

    # balról jobbra, oszloponként királynők elhelyezése
    # adott oszlopnál soronként próbálkozva
    for i in range(n):  # sorok
        # nem üti ki a balra lévő oszlopokban a királynőket
        if is_safe(n, table, i, column):
            # királynő elhelyezése
            table[i][column] = 1

            # királynők elhelyezése a következő oszlopokban
            if place_queen(n, table, (column + 1)) == True:
                return True

            # a következő oszlopokban nem sikerült elhelyezni a királynőket
            # (kiütik egymást)

            # királynő eltávolítása
            table[i][column] = 0

    return False


print(place_queen(n, chess_table, column))
print(chess_table)
