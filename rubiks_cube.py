# 3x3 kocka
# y z
# |/
# +-x
class Cube:
    def __init__(self, position):
    
        self.position = position
        self.CUBE_NUM_ROWS = len(position)
        self.CUBE_NUM_COLUMNS = len(position[0])
        self.CUBE_END_POSITION = self._generate_end_position()

    def __str__(self):
    
        cube_string = ''
        for i in range(self.CUBE_NUM_ROWS):
            for j in range(self.CUBE_NUM_COLUMNS):
                cube_string += str(self.position[i][j])
            cube_string += '\n'

        return cube_string

    # a végső állapot definiálása
    def _generate_end_position(self):
                                        # y
        # end_position = [[" ", " ", " ", "n", "n", "n", " ", " ", " ", " ", " ", " "],
        #                 [" ", " ", " ", "n", "n", "n", " ", " ", " ", " ", " ", " "],
        #                 [" ", " ", " ", "n", "n", "n", " ", " ", " ", " ", " ", " "],
        #                 ["z", "z", "z", "f", "f", "f", "s", "s", "s", "k", "k", "k"],
        #                 ["z", "z", "z", "f", "f", "f", "s", "s", "s", "k", "k", "k"],
        #                 ["z", "z", "z", "f", "f", "f", "s", "s", "s", "k", "k", "k"], # x
        #                 [" ", " ", " ", "p", "p", "p", " ", " ", " ", " ", " ", " "],
        #                 [" ", " ", " ", "p", "p", "p", " ", " ", " ", " ", " ", " "],
        #                 [" ", " ", " ", "p", "p", "p", " ", " ", " ", " ", " ", " "]]

                                        # y
        end_position = [[" ", " ", " ", "f", "f", "f", " ", " ", " ", " ", " ", " "],
                        [" ", " ", " ", "f", "f", "f", " ", " ", " ", " ", " ", " "],
                        [" ", " ", " ", "f", "f", "f", " ", " ", " ", " ", " ", " "],
                        ["n", "n", "n", "k", "k", "k", "p", "p", "p", "z", "z", "z"],
                        ["n", "n", "n", "k", "k", "k", "p", "p", "p", "z", "z", "z"],
                        ["n", "n", "n", "k", "k", "k", "p", "p", "p", "z", "z", "z"], # x
                        [" ", " ", " ", "s", "s", "s", " ", " ", " ", " ", " ", " "],
                        [" ", " ", " ", "s", "s", "s", " ", " ", " ", " ", " ", " "],
                        [" ", " ", " ", "s", "s", "s", " ", " ", " ", " ", " ", " "]]
        
        return end_position

    # tekerés
    def _rot_x1(self, cw):
        
        cc = [list(row) for row in self.position]
        f1, f2, f3 = cc[0][3], cc[1][3], cc[2][3]
        k1, k2, k3 = cc[3][3], cc[4][3], cc[5][3]
        s1, s2, s3 = cc[6][3], cc[7][3], cc[8][3]
        z1, z2, z3 = cc[3][11], cc[4][11], cc[5][11]
        n1, n2, n3 = cc[3][0], cc[4][0], cc[5][0]
        n4, n5 = cc[3][1], cc[5][1]
        n6, n7, n8 = cc[3][2], cc[4][2], cc[5][2]

        cc[0][3], cc[1][3], cc[2][3] = ((k1, k2, k3) if cw else (z3, z2, z1))
        cc[3][3], cc[4][3], cc[5][3] = ((s1, s2, s3) if cw else (f1, f2, f3))
        cc[6][3], cc[7][3], cc[8][3] = ((z3, z2, z1) if cw else (k1, k2, k3))
        cc[3][11], cc[4][11], cc[5][11] = ((f3, f2, f1) if cw else (s3, s2, s1))
        cc[3][0], cc[4][0], cc[5][0] = ((n6, n4, n1) if cw else (n3, n5, n8))
        cc[3][1], cc[5][1] = ((n7, n2) if cw else (n2, n7))
        cc[3][2], cc[4][2], cc[5][2] = ((n8, n5, n3) if cw else (n1, n4, n8))

        return cc

    def _rot_x2(self, cw):
        
        cc = [list(row) for row in self.position]
        f1, f2, f3 = cc[0][4], cc[1][4], cc[2][4]
        k1, k2, k3 = cc[3][4], cc[4][4], cc[5][4]
        s1, s2, s3 = cc[6][4], cc[7][4], cc[8][4]
        z1, z2, z3 = cc[3][10], cc[4][10], cc[5][10]

        cc[0][4], cc[1][4], cc[2][4] = ((k1, k2, k3) if cw else (z3, z2, z1))
        cc[3][4], cc[4][4], cc[5][4] = ((s1, s2, s3) if cw else (f1, f2, f3))
        cc[6][4], cc[7][4], cc[8][4] = ((z3, z2, z1) if cw else (k1, k2, k3))
        cc[3][10], cc[4][10], cc[5][10] = ((f3, f2, f1) if cw else (s3, s2, s1))

        return cc

    def _rot_x3(self, cw):
        
        cc = [list(row) for row in self.position]
        f1, f2, f3 = cc[0][5], cc[1][5], cc[2][5]
        k1, k2, k3 = cc[3][5], cc[4][5], cc[5][5]
        s1, s2, s3 = cc[6][5], cc[7][5], cc[8][5]
        z1, z2, z3 = cc[3][9], cc[4][9], cc[5][9]
        p1, p2, p3 = cc[3][6], cc[4][6], cc[5][6]
        p4, p5 = cc[3][7], cc[5][7]
        p6, p7, p8 = cc[3][8], cc[4][8], cc[5][8]

        cc[0][5], cc[1][5], cc[2][5] = ((k1, k2, k3) if cw else (z3, z2, z1))
        cc[3][5], cc[4][5], cc[5][5] = ((s1, s2, s3) if cw else (f1, f2, f3))
        cc[6][5], cc[7][5], cc[8][5] = ((z3, z2, z1) if cw else (k1, k2, k3))
        cc[3][9], cc[4][9], cc[5][9] = ((f3, f2, f1) if cw else (s3, s2, s1))
        cc[3][6], cc[4][6], cc[5][6] = ((p3, p5, p8) if cw else (p6, p4, p1))
        cc[3][7], cc[5][7] = ((p2, p7) if cw else (p7, p2))
        cc[3][8], cc[4][8], cc[5][8] = ((p1, p4, p8) if cw else (p8, p5, p3))

        return cc

    def _rot_y1(self, cw):
        
        cc = [list(row) for row in self.position]
        n1, n2, n3 = cc[5][0], cc[5][1], cc[5][2]
        k1, k2, k3 = cc[5][3], cc[5][4], cc[5][5]
        p1, p2, p3 = cc[5][6], cc[5][7], cc[5][8]
        z1, z2, z3 = cc[5][9], cc[5][10], cc[5][11]
        s1, s2, s3 = cc[6][3], cc[7][3], cc[8][3]
        s4, s5 = cc[6][4], cc[8][4]
        s6, s7, s8 = cc[6][5], cc[7][5], cc[8][5]

        cc[5][0], cc[5][1], cc[5][2] = ((k1, k2, k3) if cw else (z1, z2, z3))
        cc[5][3], cc[5][4], cc[5][5] = ((p1, p2, p3) if cw else (n1, n2, n3))
        cc[5][6], cc[5][7], cc[5][8] = ((z1, z2, z3) if cw else (k1, k2, k3))
        cc[5][9], cc[5][10], cc[5][11] = ((n1, n2, n3) if cw else (p1, p2, p3))
        cc[6][3], cc[7][3], cc[8][3] = ((s6, s4, s1) if cw else (s3, s5, s8))
        cc[6][4], cc[8][4] = ((s7, s2) if cw else (s2, s7))
        cc[6][5], cc[7][5], cc[8][5] = ((s8, s5, s3) if cw else (s1, s4, s8))

        return cc

    def _rot_y2(self, cw):
        
        cc = [list(row) for row in self.position]
        n1, n2, n3 = cc[4][0], cc[4][1], cc[4][2]
        k1, k2, k3 = cc[4][3], cc[4][4], cc[4][5]
        p1, p2, p3 = cc[4][6], cc[4][7], cc[4][8]
        z1, z2, z3 = cc[4][9], cc[4][10], cc[4][11]

        cc[4][0], cc[4][1], cc[4][2] = ((k1, k2, k3) if cw else (z1, z2, z3))
        cc[4][3], cc[4][4], cc[4][5] = ((p1, p2, p3) if cw else (n1, n2, n3))
        cc[4][6], cc[4][7], cc[4][8] = ((z1, z2, z3) if cw else (k1, k2, k3))
        cc[4][9], cc[4][10], cc[4][11] = ((n1, n2, n3) if cw else (p1, p2, p3))

        return cc

    def _rot_y3(self, cw):
        
        cc = [list(row) for row in self.position]
        n1, n2, n3 = cc[3][0], cc[3][1], cc[3][2]
        k1, k2, k3 = cc[3][3], cc[3][4], cc[3][5]
        p1, p2, p3 = cc[3][6], cc[3][7], cc[3][8]
        z1, z2, z3 = cc[3][9], cc[3][10], cc[3][11]
        f1, f2, f3 = cc[0][3], cc[1][3], cc[2][3]
        f4, f5 = cc[0][4], cc[2][4]
        f6, f7, f8 = cc[0][5], cc[1][5], cc[2][5]

        cc[3][0], cc[3][1], cc[3][2] = ((k1, k2, k3) if cw else (z1, z2, z3))
        cc[3][3], cc[3][4], cc[3][5] = ((p1, p2, p3) if cw else (n1, n2, n3))
        cc[3][6], cc[3][7], cc[3][8] = ((z1, z2, z3) if cw else (k1, k2, k3))
        cc[3][9], cc[3][10], cc[3][11] = ((n1, n2, n3) if cw else (p1, p2, p3))
        cc[0][3], cc[1][3], cc[2][3] = ((f3, f5, f8) if cw else (f6, f4, f1))
        cc[0][4], cc[2][4] = ((f2, f7) if cw else (f7, f2))
        cc[0][5], cc[1][5], cc[2][5] = ((f1, f4, f8) if cw else (f8, f5, f3))

        return cc

    def _rot_z1(self, cw):
        
        cc = [list(row) for row in self.position]
        n1, n2, n3 = cc[3][2], cc[4][2], cc[5][2]
        f1, f2, f3 = cc[2][3], cc[2][4], cc[2][5]
        p1, p2, p3 = cc[3][6], cc[4][6], cc[5][6]
        s1, s2, s3 = cc[6][3], cc[6][4], cc[6][5]
        k1, k2, k3 = cc[3][3], cc[4][3], cc[5][3]
        k4, k5 = cc[3][4], cc[5][4]
        k6, k7, k8 = cc[3][5], cc[4][5], cc[5][5]

        cc[3][2], cc[4][2], cc[5][2] = ((s1, s2, s3) if cw else (f3, f2, f1))
        cc[2][3], cc[2][4], cc[2][5] = ((n3, n2, n1) if cw else (p1, p2, p3))
        cc[3][6], cc[4][6], cc[5][6] = ((f1, f2, f3) if cw else (s3, s2, s1))
        cc[6][3], cc[6][4], cc[6][5] = ((p3, p2, p1) if cw else (n1, n2, n3))
        cc[3][3], cc[4][3], cc[5][3] = ((k3, k5, k8) if cw else (k6, k4, k1))
        cc[3][4], cc[5][4] = ((k2, k7) if cw else (k7, k2))
        cc[3][5], cc[4][5], cc[5][5] = ((k1, k4, k8) if cw else (k8, k5, k3))

        return cc

    def _rot_z2(self, cw):
        
        cc = [list(row) for row in self.position]
        n1, n2, n3 = cc[3][1], cc[4][1], cc[5][1]
        f1, f2, f3 = cc[1][3], cc[1][4], cc[1][5]
        p1, p2, p3 = cc[3][7], cc[4][7], cc[5][7]
        s1, s2, s3 = cc[7][3], cc[7][4], cc[7][5]

        cc[3][1], cc[4][1], cc[5][1] = ((s1, s2, s3) if cw else (f3, f2, f1))
        cc[1][3], cc[1][4], cc[1][5] = ((n3, n2, n1) if cw else (p1, p2, p3))
        cc[3][7], cc[4][7], cc[5][7] = ((f1, f2, f3) if cw else (s3, s2, s1))
        cc[7][3], cc[7][4], cc[7][5] = ((p3, p2, p1) if cw else (n1, n2, n3))

        return cc

    def _rot_z3(self, cw):
        
        cc = [list(row) for row in self.position]
        n1, n2, n3 = cc[3][0], cc[4][0], cc[5][0]
        f1, f2, f3 = cc[0][3], cc[0][4], cc[0][5]
        p1, p2, p3 = cc[3][8], cc[4][8], cc[5][8]
        s1, s2, s3 = cc[8][3], cc[8][4], cc[8][5]
        z1, z2, z3 = cc[3][9], cc[4][9], cc[5][9]
        z4, z5 = cc[3][10], cc[5][10]
        z6, z7, z8 = cc[3][11], cc[4][11], cc[5][11]

        cc[3][0], cc[4][0], cc[5][0] = ((s1, s2, s3) if cw else (f3, f2, f1))
        cc[0][3], cc[0][4], cc[0][5] = ((n3, n2, n1) if cw else (p1, p2, p3))
        cc[3][8], cc[4][8], cc[5][8] = ((f1, f2, f3) if cw else (s3, s2, s1))
        cc[8][3], cc[8][4], cc[8][5] = ((p3, p2, p1) if cw else (n1, n2, n3))
        cc[3][9], cc[4][9], cc[5][9] = ((z6, z4, z1) if cw else (z3, z5, z8))
        cc[3][10], cc[5][10] = ((z7, z2) if cw else (z2, z7))
        cc[3][11], cc[4][11], cc[5][11] = ((z8, z5, z3) if cw else (z1, z4, z8))

        return cc

    def get_moves(self):
    
        moves = []
        moves.append(Cube(self._rot_x1(True)))
        moves.append(Cube(self._rot_x1(False)))
        moves.append(Cube(self._rot_x2(True)))
        moves.append(Cube(self._rot_x2(False)))
        moves.append(Cube(self._rot_x3(True)))
        moves.append(Cube(self._rot_x3(False)))
        moves.append(Cube(self._rot_y1(True)))
        moves.append(Cube(self._rot_y1(False)))
        moves.append(Cube(self._rot_y2(True)))
        moves.append(Cube(self._rot_y2(False)))
        moves.append(Cube(self._rot_y3(True)))
        moves.append(Cube(self._rot_y3(False)))
        moves.append(Cube(self._rot_z1(True)))
        moves.append(Cube(self._rot_z1(False)))
        moves.append(Cube(self._rot_z2(True)))
        moves.append(Cube(self._rot_z2(False)))
        moves.append(Cube(self._rot_z3(True)))
        moves.append(Cube(self._rot_z3(False)))

        return moves

_list = []

class RunCubeSolver:
    def __init__(self, initial_cube):

        self._initial_cube = initial_cube

    def print_solution(self):
        print('A megoldás lépései:\n')
        for s in self._initial_cube.solution:
            _list.append(s)
            print(s)

    def run(self):
        self._initial_cube.do_algorithm()

class CubeSolver():
    def __init__(self, initial_cube):
        
        self.start = initial_cube

    def do_algorithm(self):
        queue = [[self.start]]
        expanded = []
        num_expanded_nodes = 0
        path = None

        while queue:
            path = queue[0]
            queue.pop(0)
            end_node = path[-1]

            if end_node.position in expanded:
                continue

            for move in end_node.get_moves():
                if move.position in expanded:
                    continue
                queue.append(path + [move])

            expanded.append(end_node.position)
            num_expanded_nodes += 1

            if end_node.position == end_node.CUBE_END_POSITION:
                break

        self.num_expanded_nodes = num_expanded_nodes
        self.solution = path

if __name__ == '__main__':
    # cube = Cube([[" ", " ", " ", "z", "s", "f", " ", " ", " ", " ", " ", " "],
    #                 [" ", " ", " ", "f", "n", "s", " ", " ", " ", " ", " ", " "],
    #                 [" ", " ", " ", "p", "k", "f", " ", " ", " ", " ", " ", " "],
    #                 ["p", "z", "k", "s", "p", "z", "p", "f", "p", "s", "p", "k"],
    #                 ["k", "z", "n", "z", "f", "z", "p", "s", "n", "k", "k", "z"],
    #                 ["n", "s", "n", "f", "p", "s", "n", "f", "s", "f", "s", "k"],
    #                 [" ", " ", " ", "z", "f", "k", " ", " ", " ", " ", " ", " "],
    #                 [" ", " ", " ", "n", "p", "n", " ", " ", " ", " ", " ", " "],
    #                 [" ", " ", " ", "z", "k", "n", " ", " ", " ", " ", " ", " "]])

    cube = Cube([[" ", " ", " ", "f", "f", "f", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", "f", "f", "f", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", "f", "f", "f", " ", " ", " ", " ", " ", " "],
                    ["z", "z", "z", "n", "n", "n", "k", "k", "k", "p", "p", "p"],
                    ["p", "p", "p", "z", "z", "z", "n", "n", "n", "k", "k", "k"],
                    ["n", "n", "n", "k", "k", "k", "p", "p", "p", "z", "z", "z"],
                    [" ", " ", " ", "s", "s", "s", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", "s", "s", "s", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", "s", "s", "s", " ", " ", " ", " ", " ", " "]])
    p = RunCubeSolver(CubeSolver(cube))
    p.run()
    p.print_solution()

import pygame
import random

pygame.font.init()

block = 40
unit_w = 12
unit_h = 9
gw = block * unit_w # rács szélesség
gh = block * unit_h # rács magasság
win_w = gw # ablak szélesség
win_h = gh # ablak magasság
tlx = 0 # bal felső sarok x
tly = 0 # bal felső sarok y

def grid_draw(surface, row, column):
    for i in range(row):
        pygame.draw.line(surface, (0, 0, 0), (tlx, tly + i * block), (tlx + gw, tly + i * block))  # horizontális vonalak
        for j in range(column):
            pygame.draw.line(surface, (0, 0, 0), (tlx + j * block, tly), (tlx + j * block, tly + gh))  # vertikális vonalak

def window_draw(surface, grid):
    colors = {' ': (0, 0, 0), 'f': (255, 255, 255), 'n': (255, 128, 0), 'k': (0, 0, 255),
            'p': (255, 0, 0), 'z': (0, 255, 0), 's': (255, 255, 0)}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, colors[grid[i][j]], (tlx + j * block, tly + i * block, block, block), 0)
    # rács és szegély megjelenítése
    grid_draw(surface, unit_h, unit_w)
    pygame.draw.rect(surface, (0, 0, 0), (tlx, tly, gw, gh), 5)

window = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption('Rubik kocka megoldása')

global grid
grid = _list
run = True
i = 0

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.display.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                i -= 1
                if i < 0:
                    i = 0
            elif event.key == pygame.K_RIGHT:
                i += 1
                if i >= len(grid):
                    i = len(grid) - 1

    window_draw(window, grid[i].position)
    pygame.display.update()