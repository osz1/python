import pygame
import random

pygame.font.init()

block = 25
unit_width = 10
unit_height = 20
play_width = block * unit_width  # játéktér szélesség
play_height = block * unit_height  # játéktér magasság
window_width = play_width + 250  # window szélesség
window_height = play_height  # window magasság
left_up_x = 0  # bal felső sarok x
left_up_y = 0  # bal felső sarok y

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

shapes = [s, z, i, o, j, l, t]
colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 255, 255), (0, 0, 255), (255, 0, 255)]

class Piece(object):
    rows = unit_height # y
    columns = unit_width # x

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = colors[shapes.index(shape)]
        self.rotation = 0 # 0-3

def create_grid(reserved_positions={}):
    grid = [[(0, 0, 0) for x in range(unit_width)] for x in range(unit_height)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in reserved_positions:
                grid[i][j] = reserved_positions[(j, i)]

    return grid

def transform_shape(shape):
    positions = []
    final_shape = shape.shape[shape.rotation % len(shape.shape)]
    for i, line in enumerate(final_shape):
        for j, column in enumerate(list(line)): # row
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions

def free_place(shape, grid):
    free_positions = [[(j, i) for j in range(unit_width) if grid[i][j] == (0, 0, 0)] for i in range(unit_height)]
    free_positions = [j for al in free_positions for j in al]

    transformed_position = transform_shape(shape)
    for pos in transformed_position:
        if pos not in free_positions:
            if pos[1] > -1:
                return False

    return True

def check_defeat(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True

    return False

def create_shape():
    global shapes, colors
    return Piece(5, 0, random.choice(shapes))

def display_text_in_middle(text, size, color, surface):
    font_type = pygame.font.SysFont('bahnschrift', size, bold=True)
    label = font_type.render(text, 1, color)
    surface.blit(label, (left_up_x + 10, left_up_y + play_height / 2 - label.get_height() / 2))

def display_grid(surface, row, column):
    for i in range(row):
        pygame.draw.line(surface, (128, 128, 128), (left_up_x, left_up_y + i * block), (left_up_x + play_width, left_up_y + i * block))  # horizontális lineak
        for j in range(column):
            pygame.draw.line(surface, (128, 128, 128), (left_up_x + j * block, left_up_y), (left_up_x + j * block, left_up_y + play_height))  # vertikális lineak

def delete_rows(grid, reserved):
    fullfilled_rows = 0
    for i in range(len(grid) - 1, -1, -1):
        row = grid[i]
        if (0, 0, 0) not in row:
            fullfilled_rows += 1
            start = i
            for j in range(len(row)):
                try:
                    del reserved[(j, i)]
                except:
                    continue

    if fullfilled_rows > 0:
        for key in sorted(list(reserved), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < start:
                new_key = (x, y + fullfilled_rows)
                reserved[new_key] = reserved.pop(key)

    return fullfilled_rows # pontozás

def display_next_shape(shape, surface):
    font_type = pygame.font.SysFont('bahnschrift', 25)
    label = font_type.render('Következő alakzat', 1, (255, 255, 255))
    sx = left_up_x + play_width + 10
    sy = left_up_y + play_height - 400
    final_shape = shape.shape[shape.rotation % len(shape.shape)]
    for i, line in enumerate(final_shape):
        for j, column in enumerate(list(line)): # row
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j * block, sy + i * block, block, block), 0)
    surface.blit(label, (sx + 10, sy - 30))

def display_window(surface, grid, score=0):
    surface.fill((0, 0, 0))
    font_type = pygame.font.SysFont('bahnschrift', 50)
    label = font_type.render('TETRIS', 1, (255, 255, 255))
    surface.blit(label, (left_up_x + play_width + 10, left_up_y))
    font_type = pygame.font.SysFont('bahnschrift', 25)
    label = font_type.render('score: ' + str(score), 1, (255, 255, 255))
    surface.blit(label, (left_up_x + play_width + 10, left_up_y + play_height - 50))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (left_up_x + j * block, left_up_y + i * block, block, block), 0)
    # rács és szegély megjelenítése
    display_grid(surface, unit_height, unit_width)
    pygame.draw.rect(surface, (0, 128, 128), (left_up_x, left_up_y, play_width, play_height), 5)

def base():
    global grid
    reserved_positions = {} # (x, y): (255, 0, 0)
    grid = create_grid(reserved_positions)

    change_piece = False
    run = True
    current_piece = create_shape()
    next_piece = create_shape()

    clock = pygame.time.Clock()
    fall_time = 0

    score = 0

    while run:
        fall_speed = 0.27

        grid = create_grid(reserved_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        # alak esés
        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if (not free_place(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not free_place(current_piece, grid):
                        current_piece.x += 1
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not free_place(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_UP:
                    # alakzat forgatása
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not free_place(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)

                if event.key == pygame.K_DOWN:
                    # alakzat (lefelé) mozgásának gyorsítása
                    current_piece.y += 1
                    if not free_place(current_piece, grid):
                        current_piece.y -= 1

        shape_pos = transform_shape(current_piece)

        # darab hozzáadása a rácshoz
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        # ha a darab leér a játéktér aljához
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                reserved_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = create_shape()
            change_piece = False

            # sorok törlése és scoreozás
            score += delete_rows(grid, reserved_positions)

        display_window(window, grid, score)
        display_next_shape(next_piece, window)
        pygame.display.update()

        if check_defeat(reserved_positions):
            run = False

    display_text_in_middle("Játék vége.", 40, (255, 255, 255), window)
    pygame.display.update()
    pygame.time.delay(2000)

def main_menu():
    run = True
    while run:
        window.fill((0, 0, 0))
        display_text_in_middle('Nyomja meg valamelyik gombot.', 30, (255, 255, 255), window)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                base()
    pygame.quit()

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Tetris')

main_menu()  # játék kezdése