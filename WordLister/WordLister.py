import numpy
import collections
import json

# vizsgálandó fájl beolvasása
print('\nValdi szavakat listázó "programja".\n')
input_file = input("Vizgálandó TXT fájl neve:\n")
if not input_file.endswith(".txt"):
    raise Exception("\nA fájlnév nem megfelelő!\n")
try:
    with open(input_file, "r", encoding="utf-8") as file:
        nyers = file.read()
except:
    print("\nValami hiba történt a vizgálandó fájl beolvasásánál!\n")

# szavak listázása
line_break = numpy.char.replace(nyers, "\n", " ")
code = numpy.char.replace(line_break, "\ufeff", "")
no_comma = numpy.char.replace(code, ",", "")
word_list = numpy.char.split(no_comma, sep=" ")
words, num = numpy.unique(word_list.tolist(), return_counts=True)

string = collections.OrderedDict()
integer = collections.OrderedDict()
float_num = collections.OrderedDict()
date = collections.OrderedDict()  # ISO 8601
for i, word in numpy.ndenumerate(words):
    if word:
        try:
            e = int(word)
            integer[e] = int(num[i])
        except:
            try:
                v = float(word)
                float_num[v] = int(num[i])
            except:
                try:
                    t = numpy.datetime64(sz)  # ISO 8601
                    d = str(word)
                    date[d] = int(num[i])
                except:
                    s = str(word)
                    string[s] = int(num[i])

# szövegek
str_sort = collections.OrderedDict(reversed(sorted(string.items(), key=lambda t: t[1])))

# egész számok
int_sort = collections.OrderedDict(
    reversed(sorted(integer.items(), key=lambda t: t[1]))
)

# tört számok
float_sort = collections.OrderedDict(
    reversed(sorted(float_num.items(), key=lambda t: t[1]))
)

# dátumok
date_sort = collections.OrderedDict(reversed(sorted(date.items(), key=lambda t: t[1])))

print("\nElemek és gyakorisságuk listája")
print("\nSzavak:")
print(str_sort)
print("\nEgész számok:")
print(int_sort)
print("\nValós számok")
print(float_sort)
print("\nDátumok (ISO 8601):")
print(date_sort)

# kimentés
print("\nSzeretné kimenteni egy JSON fájlba?")
output_file = input("Nem: üres mező. Igen: a JSON fájl neve.\n")
if output_file:
    if not output_file.endswith(".json"):
        raise Exception("\nA fájlnév nem megfelelő!\n")
    else:
        try:
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(json.dumps(dict(str_sort)))
            with open(output_file, "a", encoding="utf-8") as file:
                file.write("\n" + json.dumps(dict(int_sort)))
            with open(output_file, "a", encoding="utf-8") as file:
                file.write("\n" + json.dumps(dict(float_sort)))
            with open(output_file, "a", encoding="utf-8") as file:
                file.write("\n" + json.dumps(dict(date_sort)))
            print("\nA fájl elkészült.\n")
        except:
            print("\nValami hiba történt a fájl létrehozásánál!\n")
