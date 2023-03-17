import numpy
n = numpy.random.randint(1, 10) # királynők száma
sakktabla = numpy.zeros((n, n))
oszlop = 0
sor = 0
def biztonsag(n, tabla, sor, oszlop):
    for i in range(oszlop):
        if tabla[sor][i] == 1:
            return False
    for i, j in zip(range(sor, -1, -1), range(oszlop, -1, -1)):
        if tabla[i][j] == 1:
            return False
    for i, j in zip(range(sor, n, 1), range(oszlop, -1, -1)):
        if tabla[i][j] == 1:
            return False
    return True
def megoldas(n, tabla, oszlop):
    if oszlop >= n:
        return True
    for i in range(n):
        if biztonsag(n, tabla, i, oszlop):
            tabla[i][oszlop] = 1
            if megoldas(n, tabla, (oszlop + 1)) == True:
                return True
            tabla[i][oszlop] = 0
    return False
print(megoldas(n, sakktabla, oszlop))
print(sakktabla)