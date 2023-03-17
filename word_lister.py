import numpy
import collections
import json
print('\nValdi szavakat listázó \"programja\".\n')
be_fajl = input('Vizgálandó TXT fájl neve:\n')
if not be_fajl.endswith('.txt'):
    raise Exception('\nA fájlnév nem megfelelő!\n')
try:
    with open(be_fajl, 'r', encoding='utf-8') as fajl:
        nyers = fajl.read()
except:
    print('\nValami hiba történt a vizgálandó fájl beolvasásánál!\n')
sor_tord = numpy.char.replace(nyers, '\n', ' ')
kod = numpy.char.replace(sor_tord, '\ufeff', '')
vesszotlen = numpy.char.replace(kod, ',', '')
szolista = numpy.char.split(vesszotlen, sep=' ')
elem, db = numpy.unique(szolista.tolist(), return_counts=True)
szo = collections.OrderedDict()
e_szam = collections.OrderedDict()
v_szam = collections.OrderedDict()
datum = collections.OrderedDict() # ISO 8601
for i, sz in numpy.ndenumerate(elem):
    if sz:
        try:
            e = int(sz)
            e_szam[e] = int(db[i])
        except:
            try:
                v = float(sz)
                v_szam[v] = int(db[i])
            except:
                try:
                    t = numpy.datetime64(sz) # ISO 8601
                    d = str(sz)
                    datum[d] = int(db[i])
                except:
                    s = str(sz)
                    szo[s] = int(db[i])
szo_rend = collections.OrderedDict(reversed(sorted(szo.items(), key=lambda t: t[1])))
esz_rend = collections.OrderedDict(reversed(sorted(e_szam.items(), key=lambda t: t[1])))
vsz_rend = collections.OrderedDict(reversed(sorted(v_szam.items(), key=lambda t: t[1])))
d_rend = collections.OrderedDict(reversed(sorted(datum.items(), key=lambda t: t[1])))
print('\nElemek és gyakorisságuk listája')
print('\nSzavak:')
print(szo_rend)
print('\nEgész számok:')
print(esz_rend)
print('\nValós számok')
print(vsz_rend)
print('\nDátumok (ISO 8601):')
print(d_rend)
print('\nSzeretné kimenteni egy JSON fájlba?')
ki_fajl = input('Nem: üres mező. Igen: a JSON fájl neve.\n')
if ki_fajl:
    if not ki_fajl.endswith('.json'):
        raise Exception('\nA fájlnév nem megfelelő!\n')
    else:
        try:
            with open(ki_fajl, 'w', encoding='utf-8') as fajl:
                fajl.write(json.dumps(dict(szo_rend)))
            with open(ki_fajl, 'a', encoding='utf-8') as fajl:
                fajl.write('\n' + json.dumps(dict(esz_rend)))
            with open(ki_fajl, 'a', encoding='utf-8') as fajl:
                fajl.write('\n' + json.dumps(dict(vsz_rend)))
            with open(ki_fajl, 'a', encoding='utf-8') as fajl:
                fajl.write('\n' + json.dumps(dict(d_rend)))
            print('\nA fájl elkészült.\n')
        except:
            print('\nValami hiba történt a fájl létrehozásánál!\n')