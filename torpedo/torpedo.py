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

run = True
while run:
    columns = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    ships = [[0 for j in range(8)] for i in range(8)]
    ship_list = [2, 2, 3, 3, 4]

    i = 0
    while i < 5:
        row = numpy.random.randint(8)
        col = numpy.random.randint(8)
        direction = numpy.random.randint(2)  # vízszintes vagy függőleges
        if ships[row][col] == 0:
            if direction:
                try:
                    no_ship = True
                    for j in range(row, (row + ship_list[i])):
                        if ships[j][col]:
                            no_ship = False
                    if no_ship:
                        for j in range(row, (row + ship_list[i])):
                            ships[j][col] = i + 1
                        i += 1
                except:
                    pass
            else:
                try:
                    no_ship = True
                    for j in range(col, (col + ship_list[i])):
                        if ships[row][j]:
                            no_ship = False
                    if no_ship:
                        for j in range(col, (col + ship_list[i])):
                            ships[row][j] = i + 1
                        i += 1
                except:
                    pass

    hit = [[False for j in range(8)] for i in range(8)]
    max_ship_field = sum(ship_list)
    found_ship_field = 0
    alive_ships = len(ship_list)

    guess_count = 40
    while guess_count > 0:
        print('\nTippelési lépések (lehetőségek) száma: {}.'.format(guess_count))
        print('\nÚszó hajók száma: {}.\n'.format(alive_ships))
        display_hit = '  A B C D E F G H \n'
        for i in range(8):
            display_hit += (str(i + 1) + ' ')
            for j in range(8):
                if hit[i][j] == 1:
                    display_hit += 'X '
                elif hit[i][j] == -1:
                    display_hit += 'O '
                else:
                    display_hit += '- '
            display_hit += '\n'
        print(display_hit)

        guess = input('Tipp: ')
        if (len(guess) == 2) and guess[0].isupper() and guess[1].isdigit() and (guess[1] != '0'):
            try:
                row = int(guess[1]) - 1
                col = columns[guess[0]]        
                if hit[row][col]:
                    print('\nMár volt.\n')
                else:
                    if ships[row][col]:
                        hit[row][col] = 1
                        found_ship_field += 1

                        # megtalát hajó további mezőinek keresése.
                        remain_fields = 0
                        for i in range(len(ships)):
                            for j in range(len(ships[i])):
                                if (ships[i][j] == ships[row][col]) and (hit[i][j] == 0):
                                    remain_fields += 1
                                    break

                        if not remain_fields:
                            alive_ships -= 1
                            print('\nTalált süllyedt.\n')

                        print('\nTalált.\n')
                    else:
                        hit[row][col] = -1
                        print('\nNem talált.\n')
                    guess_count -= 1
            except:
                print('\nÉrvénytelen érték.\n')
        elif guess == 'exit':
            break
        else:
            print('\nRossz formátum.\n')

        if found_ship_field == max_ship_field:
            print('\nSikerült megtalálni az összes hajót.\n')
            break

    if not guess_count:
        print('\nA lépések száma elfogyott.\n')

    print('\nHajók elhelyezkedése:\n')
    display_ships = '  A B C D E F G H \n'
    for i in range(8):
        display_ships += (str(i + 1) + ' ')
        for j in range(8):
            if ships[i][j]:
                if hit[i][j]:
                    display_ships += 'X '
                else:
                    display_ships += 'V '
            else:
                if hit[i][j]:
                    display_ships += 'O '
                else:
                    display_ships += '- '
        display_ships += '\n'

    print(display_ships)

    print('Igen: valami beírva.')
    print('Nem: üres mező.')
    new_game = input('Új játék? ')
    if not new_game:
        run = False