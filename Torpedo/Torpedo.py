import numpy

N = 8
COLUMNS = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
SHIP_LIST = [2, 2, 3, 3, 4]  # hajók

max_ship_field = sum(SHIP_LIST)  # összes hajómező

# hajók
ships = []

# elegendő hely és szomszéd hajó hiányának ellenőrzése egy hajó elhelyezéséhez
def enough_space(ship, row, col, is_vertical):
    if ships[row][col] == 0:  # nincs hajó
        if is_vertical:  # függőleges
            if (row + ship) < len(ships):  # van elegendő hely
                for i in range((row - 1), (row + ship + 1)):
                    for j in ((col - 1), col, (col + 1)):
                        try:
                            if ships[i][j]:  # van hajó
                                return False
                        except:
                            pass

                return True  # nincs hajó
            else:  # nincs elegendő hely
                return False

        else:  # vízszintes
            if (col + ship) < len(ships[row]):  # van elegendő hely
                for j in range((col - 1), (col + ship + 1)):
                    for i in ((row - 1), row, (row + 1)):
                        try:
                            if ships[i][j]:  # van hajó
                                return False
                        except:
                            pass

                return True  # nincs hajó
            else:  # nincs elegendő hely
                return False

    return False  # van hajó




# hajók elhelyezése
def ship_placing():
    s = 0
    while s < len(SHIP_LIST):
        # véletlen mező
        row = numpy.random.randint(N)
        col = numpy.random.randint(N)

        # függőleges-e (vagy vízszintes)
        is_vertical = numpy.random.randint(2)

        # elegendő hely van-e és a környezetben nincs-e hajó
        if enough_space(SHIP_LIST[s], row, col, is_vertical):
            if is_vertical:  # függőleges
                # hajó elhelyezése
                for i in range(row, (row + SHIP_LIST[s])):
                    ships[i][col] = s + 1
            else:  # vízszintes
                # hajó elhelyezése
                for j in range(col, (col + SHIP_LIST[s])):
                    ships[row][j] = s + 1

            s += 1


guesses = []  # tippek

found_ship_field = 0  # megtalált hajómezők
alive_ships = len(SHIP_LIST)  # úszó hajók (megjelenítése)


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
                if guesses[i][j]:  # volt tipp
                    grid += "X "
                else:  # nem volt tipp
                    grid += "V "
            else:  # nincs hajó a mezőn
                if guesses[i][j]:  # volt tipp
                    grid += "O "
                else:  # nem volt tipp
                    grid += "- "
        grid += "\n"
    return "\nHajók elhelyezkedése:\n" + grid


print("\nValdi Torpedó társasjátéka.\n")
print("Kilépés: 'q'\n")
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

    guesses = [[False for j in range(N)] for i in range(N)]  # tippek

    found_ship_field = 0  # megtalált hajómezők (talált tipp esetén nő)

    # úszó hajók száma ("süllyedéseknél" csökken)
    alive_ships = len(SHIP_LIST)

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

        elif guess == "q":  # kilépés a játékból
            print(reveal_ships())
            break
        else:
            print("\nRossz formátum.\n")

        if found_ship_field == max_ship_field:
            print("\nSikerült megtalálni az összes hajót.\n")
            print(reveal_ships())
            break

    # tippelés vége

    if not guess_count:
        print("\nA lépések száma elfogyott.\n")

    print("Kilépés a játékból: 'q'\n")

    new_game = input("Új játék? ")
    if new_game == "q":  # kilépés a programból
        print("\nVége!\n")
        run = False