import pygame
pygame.init()
pygame.font.init()
from main import solve_board, check_valid_board
from pygame.locals import (
    K_r,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    K_RETURN,
    K_0,
    K_1,
    K_2,
    K_3,
    K_4,
    K_5,
    K_6,
    K_7,
    K_8,
    K_9,
)
# Fonts
font_number = pygame.font.SysFont("comicsans", 40)
# Colours to be used
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLUE = (0, 255, 255)
LEFT = 1
# Window size
SIDE_WINDOW = 500
SIDE_GAME = 486
SPACING = (SIDE_WINDOW - SIDE_GAME) / 2

# Title and Icon
pygame.display.set_caption("Sudoku Solver")
img = pygame.image.load('icon.png')
pygame.display.set_icon(img)

SPACE_BETWEEN_BOX = SIDE_GAME / 9
LEFT_CLICK_PRESS = (1, 0, 0)

# Total window
screen = pygame.display.set_mode([SIDE_WINDOW, SIDE_WINDOW])
screen.fill(WHITE)
selection_box = pygame.Surface([int(SPACE_BETWEEN_BOX), int(SPACE_BETWEEN_BOX)])
selection_box.fill(BLUE)
empty_box = pygame.Surface([int(SPACE_BETWEEN_BOX), int(SPACE_BETWEEN_BOX)])
empty_box.fill(WHITE)

sudoku_board = [[0 for x in range(9)] for y in range(9)]


def draw_grid():
    # Making column lines
    for i in range(0, 10):
        if i % 3 != 0:
            pygame.draw.line(screen, BLACK, ((i * SPACE_BETWEEN_BOX) + SPACING, SPACING), ((i * SPACE_BETWEEN_BOX) +
                                                                                           SPACING, SIDE_GAME +
                                                                                           SPACING))
        else:
            pygame.draw.line(screen, BLACK, ((i * SPACE_BETWEEN_BOX) + SPACING, SPACING), ((i * SPACE_BETWEEN_BOX) +
                                                                                           SPACING, SIDE_GAME +
                                                                                           SPACING), 3)
    # Making row lines
    for j in range(0, 10):
        if j % 3 != 0:
            pygame.draw.line(screen, BLACK, (SPACING, (j * SPACE_BETWEEN_BOX) + SPACING), (SPACING + SIDE_GAME,
                                                                                           (j * SPACE_BETWEEN_BOX) +
                                                                                           SPACING))
        else:
            pygame.draw.line(screen, BLACK, (SPACING, (j * SPACE_BETWEEN_BOX) + SPACING), (SPACING + SIDE_GAME,
                                                                                           (j * SPACE_BETWEEN_BOX) +
                                                                                           SPACING), 3)


def put_all_num():
    for i in range(9):
        for j in range(9):
            text = font_number.render(str(sudoku_board[i][j]), False, BLACK)
            x_ordinate = (j * SPACE_BETWEEN_BOX) + SPACING + (SPACE_BETWEEN_BOX / 2) - 8
            y_ordinate = (i * SPACE_BETWEEN_BOX) + SPACING + (SPACE_BETWEEN_BOX / 2) - 10
            screen.blit(text, (x_ordinate, y_ordinate))


def enter_space(x_ordinate, y_ordinate):
    x_point = ((x_ordinate // SPACE_BETWEEN_BOX) * SPACE_BETWEEN_BOX) + SPACING
    y_point = ((y_ordinate // SPACE_BETWEEN_BOX) * SPACE_BETWEEN_BOX) + SPACING
    reset_screen_board()
    put_all_num()
    screen.blit(selection_box, (x_point, y_point))


def reset_screen_board():
    screen = pygame.display.set_mode([SIDE_WINDOW, SIDE_WINDOW])
    screen.fill(WHITE)


def get_number(number):
    if number == K_0:
        return 0
    if number == K_1:
        return 1
    if number == K_2:
        return 2
    if number == K_3:
        return 3
    if number == K_4:
        return 4
    if number == K_5:
        return 5
    if number == K_6:
        return 6
    if number == K_7:
        return 7
    if number == K_8:
        return 8
    if number == K_9:
        return 9


def put_num_in_board(num, x_ordinate, y_ordinate):
    text = font_number.render(str(get_number(num)), False, BLACK)
    x_point = ((x_ordinate // SPACE_BETWEEN_BOX) * SPACE_BETWEEN_BOX) + SPACING + (SPACE_BETWEEN_BOX / 2) - 8
    y_point = ((y_ordinate // SPACE_BETWEEN_BOX) * SPACE_BETWEEN_BOX) + SPACING + (SPACE_BETWEEN_BOX / 2) - 10
    x_box = ((x_ordinate // SPACE_BETWEEN_BOX) * SPACE_BETWEEN_BOX) + SPACING
    y_box = ((y_ordinate // SPACE_BETWEEN_BOX) * SPACE_BETWEEN_BOX) + SPACING
    screen.blit(selection_box, (x_box, y_box))
    screen.blit(text, (x_point, y_point))
    y_coord = ((x_point - SPACING) / SPACE_BETWEEN_BOX)
    x_coord = ((y_point - SPACING) / SPACE_BETWEEN_BOX)
    sudoku_board[int(x_coord)][int(y_coord)] = get_number(num)


# -----------------------------------Main loop----------------------------------- #
# Variable to keep the main loop running
running = True
x = 0
y = 0
while running:
    # Look at every event in the queue
    put_all_num()
    for event in pygame.event.get():
        # Did the user press the mouse?
        if event.type == MOUSEBUTTONDOWN and event.button == LEFT:
            (x, y) = pygame.mouse.get_pos()
            reset_screen_board()
            enter_space(x + SPACING, y + SPACING)
            put_all_num()
        if event.type == KEYDOWN and (K_0 <= event.key <= K_9):
            put_num_in_board(event.key, x + SPACING, y + SPACING)
        if event.type == KEYDOWN and event.key == K_r:
            reset_screen_board()
        if event.type == KEYDOWN and event.key == K_RETURN:
            solve_board(sudoku_board)
            reset_screen_board()
            put_all_num()
            running = False
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
    draw_grid()
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()
