import numpy
print('\nValdi Torpedó társasjátéka.\n')
print('Kilépés: \'exit\'\n')
print('A tipp formátuma:')
print('első karakter (oszlop): nagybetű (A-H)')
print('második karakter (sor): számok (1-8)\n')
print('Tábla jelmagyarázat:')
print('O: volt tipp, nem talált')
print('X: volt tipp, talált')
print('-: nem volt tipp\n')
fut = True
while fut:
    oszlopok = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    hajok = [[0 for j in range(8)] for i in range(8)]
    hajolista = [2, 2, 3, 3, 4]
    i = 0
    while i < 5:
        s = numpy.random.randint(8)
        o = numpy.random.randint(8)
        tajolas = numpy.random.randint(2)
        if hajok[s][o] == 0:
            if tajolas:
                try:
                    nincs_hajo = True
                    for j in range(s, (s + hajolista[i])):
                        if hajok[j][o]:
                            nincs_hajo = False
                    if nincs_hajo:
                        for j in range(s, (s + hajolista[i])):
                            hajok[j][o] = i + 1
                        i += 1
                except:
                    pass
            else:
                try:
                    nincs_hajo = True
                    for j in range(o, (o + hajolista[i])):
                        if hajok[s][j]:
                            nincs_hajo = False
                    if nincs_hajo:
                        for j in range(o, (o + hajolista[i])):
                            hajok[s][j] = i + 1
                        i += 1
                except:
                    pass
    talalat = [[False for j in range(8)] for i in range(8)]
    max_hajo_mezo = sum(hajolista)
    megtalalt_hajo_mezo = 0
    uszo_hajok_szama = len(hajolista)
    tipp_lehetoseg = 40
    while tipp_lehetoseg > 0:
        print('\nTippelési lépések (lehetőségek) száma: {}.'.format(tipp_lehetoseg))
        print('\nÚszó hajók száma: {}.\n'.format(uszo_hajok_szama))
        talalat_kiir = '  A B C D E F G H \n'
        for i in range(8):
            talalat_kiir += (str(i + 1) + ' ')
            for j in range(8):
                if talalat[i][j] == 1:
                    talalat_kiir += 'X '
                elif talalat[i][j] == -1:
                    talalat_kiir += 'O '
                else:
                    talalat_kiir += '- '
            talalat_kiir += '\n'
        print(talalat_kiir)
        tipp = input('Tipp: ')
        if (len(tipp) == 2) and tipp[0].isupper() and tipp[1].isdigit() and (tipp[1] != '0'):
            try:
                s = int(tipp[1]) - 1
                o = oszlopok[tipp[0]]        
                if talalat[s][o]:
                    print('\nMár volt.\n')
                else:
                    if hajok[s][o]:
                        talalat[s][o] = 1
                        megtalalt_hajo_mezo += 1
                        meg_van_mezo = 0
                        for i in range(len(hajok)):
                            for j in range(len(hajok[i])):
                                if (hajok[i][j] == hajok[s][o]) and (talalat[i][j] == 0):
                                    meg_van_mezo += 1
                                    break
                        if not meg_van_mezo:
                            uszo_hajok_szama -= 1
                        print('\nTalált.\n')
                    else:
                        talalat[s][o] = -1
                        print('\nNem talált.\n')
                    tipp_lehetoseg -= 1
            except:
                print('\nÉrvénytelen érték.\n')
        elif tipp == 'exit':
            break
        else:
            print('\nRossz formátum.\n')
        if megtalalt_hajo_mezo == max_hajo_mezo:
            print('\nSikerült megtalálni az összes hajót.\n')
            break
    if not tipp_lehetoseg:
        print('\nA lépések száma elfogyott.\n')
    print('\nHajók elhelyezkedése:\n')
    hajok_kiir = '  A B C D E F G H \n'
    for i in range(8):
        hajok_kiir += (str(i + 1) + ' ')
        for j in range(8):
            if hajok[i][j]:
                if talalat[i][j]:
                    hajok_kiir += 'X '
                else:
                    hajok_kiir += 'V '
            else:
                if talalat[i][j]:
                    hajok_kiir += 'O '
                else:
                    hajok_kiir += '- '
        hajok_kiir += '\n'
    print(hajok_kiir)
    print('Igen: valami beírva.')
    print('Nem: üres mező.')
    uj = input('Új játék? ')
    if not uj:
        fut = False