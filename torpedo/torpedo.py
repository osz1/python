import numpy

N = 8
COLUMNS = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
SHIP_LIST = [2, 2, 3, 3, 4]  # hajók

# hajók elhelyezése
ships = []


def ship_placing():
    i = 0
    while i < len(SHIP_LIST):
        # véletlen hely
        row = numpy.random.randint(N)
        col = numpy.random.randint(N)

        # vízszintes vagy függőleges
        is_vertical = numpy.random.randint(2)

        if ships[row][col] == 0:
            if is_vertical:  # függőleges
                try:
                    no_ship = True

                    # van-e hajó a véletlen helyen
                    for j in range((row - 1), (row + SHIP_LIST[i] + 1)):
                        for c in ((col - 1), col, (col + 1)):
                            try:
                                if ships[j][c]:
                                    no_ship = False
                            except:
                                no_ship = False

                    # hajó elhelyezése
                    if no_ship:
                        for j in range(row, (row + SHIP_LIST[i])):
                            ships[j][col] = i + 1
                        i += 1
                except:
                    pass
            else:  # vízszintes
                try:
                    no_ship = True

                    # van-e hajó a véletlen helyen
                    for j in range((col - 1), (col + SHIP_LIST[i] + 1)):
                        for r in ((row - 1), row, (row + 1)):
                            try:
                                if ships[r][j]:
                                    no_ship = False
                            except:
                                no_ship = False

                    # hajó elhelyezése
                    if no_ship:
                        for j in range(col, (col + SHIP_LIST[i])):
                            ships[row][j] = i + 1
                        i += 1
                except:
                    pass


guesses = [[False for j in range(N)] for i in range(N)]  # tippek

max_ship_field = sum(SHIP_LIST)  # összes hajómező
found_ship_field = 0  # megtalált hajómezők
alive_ships = len(SHIP_LIST)  # úszó hajók


# mező megjelenítése
def display_field():
    grid = "  A B C D E F G H \n"
    for i in range(len(guesses)):  # 8
        grid += str(i + 1) + " "
        for j in range(len(guesses[i])):  # 8
            if guesses[i][j] == 1:
                grid += "X "
            elif guesses[i][j] == -1:
                grid += "O "
            else:
                grid += "- "
        grid += "\n"
    return grid


# tippelés helyessége
def correct_guess(guess):
    if len(guess) != 2:
        return False
    return guess[0].isupper() and guess[1].isdigit() and (guess[1] != "0")


# megtalát hajó további mezőinek keresése
def ship_is_alive(ship):
    for i in range(len(ships)):
        for j in range(len(ships[i])):
            if (ships[i][j] == ship) and (guesses[i][j] == 0):
                return True
    return False


# hajók felfedése
def reveal_ships():
    grid = "  A B C D E F G H \n"
    for i in range(N):
        grid += str(i + 1) + " "
        for j in range(N):
            if ships[i][j]:  # hajó van a mezőn
                if guesses[i][j]:
                    grid += "X "
                else:
                    grid += "V "
            else:  # nincs hajó a mezőn
                if guesses[i][j]:
                    grid += "O "
                else:
                    grid += "- "
        grid += "\n"
    return "\nHajók elhelyezkedése:\n" + grid


print("\nValdi Torpedó társasjátéka.\n")
print("Kilépés: 'exit'\n")
print("A tipp formátuma:")
print("első karakter (oszlop): nagybetű (A-H)")
print("második karakter (sor): számok (1-" + str(N) + ")\n")
print("Tábla jelmagyarázat:")
print("O: volt tipp, nem talált")
print("X: volt tipp, talált")
print("-: nem volt tipp\n")

run = True
while run:
    # hajók elhelyezése
    ships = [[0 for j in range(N)] for i in range(N)]
    ship_placing()

    # tippelés kezdődik
    guess_count = 40  # tippek száma (csökken)
    while guess_count > 0:
        print("\nTippelési lépések (lehetőségek) száma: {}.".format(guess_count))
        print("\nÚszó hajók száma: {}.\n".format(alive_ships))
        print(display_field())

        # tippelés
        guess = input("Tipp: ")
        if correct_guess(guess):  # helyes tipp
            try:
                row = int(guess[1]) - 1
                col = COLUMNS[guess[0]]

                if guesses[row][col]:
                    print("\nMár volt.\n")
                else:
                    if ships[row][col]:  # talált
                        guesses[row][col] = 1
                        found_ship_field += 1

                        # süllyedt-e
                        if ship_is_alive(ships[row][col]):
                            print("\nTalált.\n")
                        else:
                            alive_ships -= 1
                            print("\nTalált süllyedt.\n")

                    else:  # nem talált
                        guesses[row][col] = -1
                        print("\nNem talált.\n")

                    guess_count -= 1

            except:  # a tipp nincs a játékteren belül
                print("\nÉrvénytelen érték.\n")

        elif guess == "exit":  # kilépés a programból
            print(reveal_ships())
            break
        else:
            print("\nRossz formátum.\n")

        if found_ship_field == max_ship_field:
            print("\nSikerült megtalálni az összes hajót.\n")
            break

    # tippelés vége

    if not guess_count:
        print("\nA lépések száma elfogyott.\n")

    print(reveal_ships())

    print("Igen: valami beírva.")
    print("Nem: üres mező.")

    new_game = input("Új játék? ")
    if not new_game:
        print("\nVége!\n")
        run = False
