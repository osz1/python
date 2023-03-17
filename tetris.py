import pygame
import random

pygame.font.init()

blokk = 25
egyseg_szel = 10
egyseg_mag = 20
jsz = blokk * egyseg_szel # játéktér szélesség
jm = blokk * egyseg_mag # játéktér magasság
asz = jsz + 250 # ablak szélesség
am = jm # ablak magasság
bfsx = 0 # bal felső sarok x
bfsy = 0 # bal felső sarok y

# alakzatok
s = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]
z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]
i = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
o = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
j = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
l = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]
t = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

alakzatok = [s, z, i, o, j, l, t]
szinek = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 255, 255), (0, 0, 255), (255, 0, 255)]

class darab(object):
    sorok = egyseg_mag # y
    oszlopok = egyseg_szel # x
    def __init__(self, oszlop, sor, alakzat):
        self.x = oszlop
        self.y = sor
        self.alakzat = alakzat
        self.szin = szinek[alakzatok.index(alakzat)]
        self.forgatas = 0 # 0-3

def racs_letrehoz(foglalt_poziciok={}):
    racs = [[(0, 0, 0) for x in range(egyseg_szel)] for x in range(egyseg_mag)]
    for i in range(len(racs)):
        for j in range(len(racs[i])):
            if (j, i) in foglalt_poziciok:
                racs[i][j] = foglalt_poziciok[(j, i)]
    return racs

def alakzat_atalakit(alakzat):
    poziciok = []
    alak = alakzat.alakzat[alakzat.forgatas % len(alakzat.alakzat)]
    for i, vonal in enumerate(alak):
        for j, oszlop in enumerate(list(vonal)): # sor
            if oszlop == '0':
                poziciok.append((alakzat.x + j, alakzat.y + i))
    for i, poz in enumerate(poziciok):
        poziciok[i] = (poz[0] - 2, poz[1] - 4)
    return poziciok

def szabad_hely(alakzat, racs):
    szabad_poziciok = [[(j, i) for j in range(egyseg_szel) if racs[i][j] == (0, 0, 0)] for i in range(egyseg_mag)]
    szabad_poziciok = [j for al in szabad_poziciok for j in al]
    formazott = alakzat_atalakit(alakzat)
    for poz in formazott:
        if poz not in szabad_poziciok:
            if poz[1] > -1:
                return False
    return True

def vereseg_ellenorzese(poziciok):
    for poz in poziciok:
        x, y = poz
        if y < 1:
            return True
    return False

def alakzat_letrehoz():
    global alakzatok, szinek
    return darab(5, 0, random.choice(alakzatok))

def szoveg_kozepre_kiir(szoveg, meret, szin, felulet):
    betutipus = pygame.font.SysFont('bahnschrift', meret, bold=True)
    felirat = betutipus.render(szoveg, 1, szin)
    felulet.blit(felirat, (bfsx + 10, bfsy + jm / 2 - felirat.get_height() / 2))

def racs_megjelenit(felulet, sor, oszlop):
    for i in range(sor):
        pygame.draw.line(felulet, (128, 128, 128), (bfsx, bfsy + i * blokk), (bfsx + jsz, bfsy + i * blokk))  # horizontális vonalak
        for j in range(oszlop):
            pygame.draw.line(felulet, (128, 128, 128), (bfsx + j * blokk, bfsy), (bfsx + j * blokk, bfsy + jm))  # vertikális vonalak

def sorok_torlese(racs, foglalt):
    teljes = 0
    for i in range(len(racs) - 1, -1, -1):
        sor = racs[i]
        if (0, 0, 0) not in sor:
            teljes += 1
            ind = i
            for j in range(len(sor)):
                try:
                    del foglalt[(j, i)]
                except:
                    continue
    if teljes > 0:
        for kulcs in sorted(list(foglalt), key=lambda x: x[1])[::-1]:
            x, y = kulcs
            if y < ind:
                ujkulcs = (x, y + teljes)
                foglalt[ujkulcs] = foglalt.pop(kulcs)
    return teljes # pont

def kovetkezo_alakzat_megjelenit(alakzat, felulet):
    betutipus = pygame.font.SysFont('bahnschrift', 25)
    felirat = betutipus.render('Következő alakzat', 1, (255, 255, 255))
    sx = bfsx + jsz + 10
    sy = bfsy + jm - 400
    alak = alakzat.alakzat[alakzat.forgatas % len(alakzat.alakzat)]
    for i, vonal in enumerate(alak):
        for j, oszlop in enumerate(list(vonal)): # sor
            if oszlop == '0':
                pygame.draw.rect(felulet, alakzat.szin, (sx + j * blokk, sy + i * blokk, blokk, blokk), 0)
    felulet.blit(felirat, (sx + 10, sy - 30))

def ablak_megjelenit(felulet, racs, pont=0):
    felulet.fill((0, 0, 0))
    betutipus = pygame.font.SysFont('bahnschrift', 50)
    felirat = betutipus.render('TETRIS', 1, (255, 255, 255))
    felulet.blit(felirat, (bfsx + jsz + 10, bfsy))
    betutipus = pygame.font.SysFont('bahnschrift', 25)
    felirat = betutipus.render('Pont: ' + str(pont), 1, (255, 255, 255))
    felulet.blit(felirat, (bfsx + jsz + 10, bfsy + jm - 50))
    for i in range(len(racs)):
        for j in range(len(racs[i])):
            pygame.draw.rect(felulet, racs[i][j], (bfsx + j * blokk, bfsy + i * blokk, blokk, blokk), 0)
    # rács és szegély megjelenítése
    racs_megjelenit(felulet, egyseg_mag, egyseg_szel)
    pygame.draw.rect(felulet, (0, 128, 128), (bfsx, bfsy, jsz, jm), 5)

def alap():
    global racs
    foglalt_poziciok = {} # (x, y): (255, 0, 0)
    racs = racs_letrehoz(foglalt_poziciok)
    darab_valtas = False
    fut = True
    jelenlegi_darab = alakzat_letrehoz()
    kovetkezo_darab = alakzat_letrehoz()
    ora = pygame.time.Clock()
    eses_ido = 0
    pont = 0

    while fut:
        eses_sebesseg = 0.27

        racs = racs_letrehoz(foglalt_poziciok)
        eses_ido += ora.get_rawtime()
        ora.tick()

        # darab esés
        if eses_ido / 1000 >= eses_sebesseg:
            eses_ido = 0
            jelenlegi_darab.y += 1
            if (not szabad_hely(jelenlegi_darab, racs)) and jelenlegi_darab.y > 0:
                jelenlegi_darab.y -= 1
                darab_valtas = True

        for esemeny in pygame.event.get():
            if esemeny.type == pygame.QUIT:
                fut = False
                pygame.display.quit()
                quit()

            if esemeny.type == pygame.KEYDOWN:
                if esemeny.key == pygame.K_LEFT:
                    jelenlegi_darab.x -= 1
                    if not szabad_hely(jelenlegi_darab, racs):
                        jelenlegi_darab.x += 1
                elif esemeny.key == pygame.K_RIGHT:
                    jelenlegi_darab.x += 1
                    if not szabad_hely(jelenlegi_darab, racs):
                        jelenlegi_darab.x -= 1
                elif esemeny.key == pygame.K_UP:
                    # alakzat forgatasa
                    jelenlegi_darab.forgatas = jelenlegi_darab.forgatas + 1 % len(jelenlegi_darab.alakzat)
                    if not szabad_hely(jelenlegi_darab, racs):
                        jelenlegi_darab.forgatas = jelenlegi_darab.forgatas - 1 % len(jelenlegi_darab.alakzat)

                if esemeny.key == pygame.K_DOWN:
                    # alakzat (lefelé) mozgásának gyorsítása
                    jelenlegi_darab.y += 1
                    if not szabad_hely(jelenlegi_darab, racs):
                        jelenlegi_darab.y -= 1

        alakzat_poz = alakzat_atalakit(jelenlegi_darab)

        # darab hozzáadása a rácshoz
        for i in range(len(alakzat_poz)):
            x, y = alakzat_poz[i]
            if y > -1:
                racs[y][x] = jelenlegi_darab.szin

        # ha a darab leér a játéktér aljához
        if darab_valtas:
            for poz in alakzat_poz:
                p = (poz[0], poz[1])
                foglalt_poziciok[p] = jelenlegi_darab.szin
            jelenlegi_darab = kovetkezo_darab
            kovetkezo_darab = alakzat_letrehoz()
            darab_valtas = False

            # sorok törlése és pontozás
            pont += sorok_torlese(racs, foglalt_poziciok)

        ablak_megjelenit(ablak, racs, pont)
        kovetkezo_alakzat_megjelenit(kovetkezo_darab, ablak)
        pygame.display.update()

        if vereseg_ellenorzese(foglalt_poziciok):
            fut = False

    szoveg_kozepre_kiir("Játék vége.", 40, (255, 255, 255), ablak)
    pygame.display.update()
    pygame.time.delay(2000)

def fomenu():
    fut = True
    while fut:
        ablak.fill((0, 0, 0))
        szoveg_kozepre_kiir('Nyomja meg valamelyik gombot.', 30, (255, 255, 255), ablak)
        pygame.display.update()
        for esemeny in pygame.event.get():
            if esemeny.type == pygame.QUIT:
                fut = False

            if esemeny.type == pygame.KEYDOWN:
                alap()
    pygame.quit()

ablak = pygame.display.set_mode((asz, am))
pygame.display.set_caption('Tetris')

fomenu()  # játék kezdése