# 1-2
# |X|
# 0-3

import itertools

cities = (0, 1, 2, 3)
distances = ((0, 3, 5, 4), (3, 0, 4, 5), (5, 4, 0, 3), (4, 5, 3, 0))

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

city = cities[0]
path = None
shortest_length = None

travels = itertools.permutations(cities[1:], len(cities[1:]))
for travel in travels:
    length = 0
    for i in range(len(travel[:-1])):
        length += distances[travel[i]][travel[i + 1]]
    length += distances[travel[-1]][city]
    length += distances[city][travel[0]]

    if (shortest_length == None) or (length < shortest_length):
        shortest_length = length
        path = travel

print(city, path, shortest_length)
