import numpy
honap = numpy.arange('2021-11', '2021-12', dtype='datetime64[D]')
for nap in honap:
    nev = numpy.genfromtxt('raktárkészlet.txt',  dtype=str, delimiter=';', skip_header=1, usecols=0, encoding='utf-8')
    ar = numpy.genfromtxt('raktárkészlet.txt',  dtype=int, delimiter=';', skip_header=1, usecols=1, encoding='utf-8')
    mennyiseg = numpy.genfromtxt('raktárkészlet.txt',  dtype=int, delimiter=';', skip_header=1, usecols=2, encoding='utf-8')
    datum = str(nap).replace('-', '.')
    rnev = numpy.random.choice(nev)
    rmenny = numpy.random.randint(1, 15)
    idx =  numpy.where(nev == rnev)
    rar = rmenny * ar[idx][0]
    ir = '\n' + rnev + ';' + str(rmenny) + ';' + str(rar) + ';' + datum
    if rmenny <= mennyiseg[idx]:
        with open('rendelések.txt', 'a', encoding='utf-8') as fajl:
                fajl.write(ir + ';igen')
        mennyiseg[idx] -= rmenny
        numpy.savetxt('raktárkészlet.txt', numpy.stack((nev, ar, mennyiseg), axis=-1), fmt='%s', delimiter=';', header='TERMÉK_NEVE|TERMÉK_ÁRA|RENDELKEZÉSRE_ÁLLÓ_MENNYISÉG', encoding='utf-8')
    else:
        with open('rendelések.txt', 'a', encoding='utf-8') as fajl:
                fajl.write(ir + ';nem')
termek = numpy.genfromtxt('rendelések.txt',  dtype=str, delimiter=';', skip_header=1, usecols=0, encoding='utf-8')
menny = numpy.genfromtxt('rendelések.txt',  dtype=int, delimiter=';', skip_header=1, usecols=1, encoding='utf-8')
fiz = numpy.genfromtxt('rendelések.txt',  dtype=int, delimiter=';', skip_header=1, usecols=2, encoding='utf-8')
vegr = numpy.genfromtxt('rendelések.txt',  dtype=str, delimiter=';', skip_header=1, usecols=3, encoding='utf-8')
siker = numpy.genfromtxt('rendelések.txt',  dtype=str, delimiter=';', skip_header=1, usecols=4, encoding='utf-8')
termeklista = numpy.unique(termek)
termekmenny = numpy.zeros(len(termeklista))
termekbev = numpy.zeros(len(termeklista))
sikeres = 0
sikertelen = 0
for idx, x in numpy.ndenumerate(termek):
    if siker[idx] == 'igen':
        termekmenny[numpy.where(termeklista == x)] += menny[idx]
        termekbev[numpy.where(termeklista == x)] += fiz[idx]
        sikeres += 1
    else:
        sikertelen += 1
print('melyik termékből hány darab került eladásra\n', numpy.stack((termeklista, termekmenny), axis=-1))
print('melyik termékből mennyi maradt raktáron a hónap végére\n', numpy.genfromtxt('raktárkészlet.txt',  dtype=str, delimiter=';', skip_header=1, usecols=(0, -1), encoding='utf-8'))
print('mi volt a legnépszerűbb termék a hónapban', termeklista[numpy.where(termekmenny == max(termekmenny))])
print('melyik termék mennyi bevételt hozott a webshopnak a hónapban\n', numpy.stack((termeklista, termekbev), axis=-1))
print('mennyi volt a webshop teljes bevétele a hónapban', numpy.sum(fiz))
print('hány sikeres és hány sikertelen rendelés végrehajtás volt összesen')
print('sikeres', sikeres, '\nsikertelen', sikertelen)
print('melyik napon történt a legtöbb megrendelés', vegr[numpy.where(menny == max(menny))])