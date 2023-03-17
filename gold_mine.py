import numpy
m = numpy.random.randint(1, 10)
n = numpy.random.randint(2, 10)
aranymezo = numpy.random.randint(1, 100, size=(m, n))
print(aranymezo)
aranyut = [[[] for j in range(n)] for i in range(m)]
aranymennyiseg = numpy.zeros((m, n))
for oszlop in range((n - 1), -1, -1):
    for sor in range(m):
        if oszlop == (n - 1):
            jobbra = 0
        else:
            jobbra = aranymennyiseg[sor][oszlop + 1]
        if (sor == 0) or (oszlop == (n - 1)):
            jobbrafel = 0
        else:
            jobbrafel = aranymennyiseg[sor - 1][oszlop + 1]
        if (sor == (m - 1)) or (oszlop == (n - 1)):
            jobbrale = 0
        else:
            jobbrale = aranymennyiseg[sor + 1][oszlop + 1]
        maxarany = max(jobbra, jobbrafel, jobbrale)
        if maxarany:
            if jobbra == maxarany:
                utarany = [(sor, (oszlop + 1))] + aranyut[sor][oszlop + 1]
            elif jobbrafel == maxarany:
                utarany = [((sor - 1), (oszlop + 1))] + aranyut[sor - 1][oszlop + 1]
            elif jobbrale == maxarany:
                utarany = [((sor + 1), (oszlop + 1))] + aranyut[sor + 1][oszlop + 1]
        else:
            utarany = []
        aranymennyiseg[sor][oszlop] = aranymezo[sor][oszlop] + maxarany
        aranyut[sor][oszlop] = utarany
maximumarany = 0
aranyutvonal = None
for sor in range(m):
    if aranymennyiseg[sor][0] > maximumarany:
        maximumarany = aranymennyiseg[sor][0]
        aranyutvonal = [(sor, 0)] + aranyut[sor][0]
aranymezout = []
for ut in aranyutvonal:
    aranymezout.append(aranymezo[ut[0]][ut[1]])
print(maximumarany, aranymezout, aranyutvonal)