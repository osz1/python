# 1-2
# |X|
# 0-3

import itertools

varosok = (0, 1, 2, 3)
tavok = ((0, 3, 5, 4), (3, 0, 4, 5), (5, 4, 0, 3), (4, 5, 3, 0))

# ut = None
# hossz = None
# korok = itertools.permutations(varosok, len(varosok))
# for kor in korok:
    # h = 0
    # for i in range(len(kor[:-1])):
        # for tav in tavok:
            # if tav[kor[i]] == 0:
                # h += tav[kor[i + 1]]
    # for tav in tavok:
        # if tav[kor[-1]] == 0:
            # h += tav[kor[0]]
    # if (hossz == None) or (h < hossz):
        # hossz = h
        # ut = kor
# print(ut, hossz)

# varos = varosok[0]
# ut = None
# hossz = None
# korok = itertools.permutations(varosok[1:], len(varosok[1:]))
# for kor in korok:
    # h = 0
    # for i in range(len(kor[:-1])):
        # for tav in tavok:
            # if tav[kor[i]] == 0:
                # h += tav[kor[i + 1]]
    # for tav in tavok:
        # if tav[kor[-1]] == 0:
            # h += tav[varos]
        # if tav[varos] == 0:
            # h += tav[kor[0]]
    # if (hossz == None) or (h < hossz):
        # hossz = h
        # ut = kor
# print(varos, ut, hossz)

varos = varosok[0]
ut = None
hossz = None
korok = itertools.permutations(varosok[1:], len(varosok[1:]))
for kor in korok:
    h = 0
    for i in range(len(kor[:-1])):
        h += tavok[kor[i]][kor[i + 1]]
    h += tavok[kor[-1]][varos]
    h += tavok[varos][kor[0]]
    if (hossz == None) or (h < hossz):
        hossz = h
        ut = kor
print(varos, ut, hossz)