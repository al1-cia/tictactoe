import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 1000, 770
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE=(0,0,255)
RED=(255,0,0)

# Fonts
FONT = pygame.font.SysFont(None, 40)

# Game variables
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
goal = {(0, 4, 8): 0, (1, 4, 7): 0, (0, 1, 2): 0, (2, 4, 6): 0, (0, 3, 6): 0, (3, 4, 5): 0, (2, 5, 8): 0, (6, 7, 8): 0}
dictt = {'X': [], 'O': []}
a = 0  # Game over flag

# Functions
def disp():
    SCREEN.fill(WHITE)

    #centering the grid 
    GRID_WIDTH = 300  # Width of the grid
    GRID_HEIGHT = 300  # Height of the grid
    GRID_X = (WIDTH - GRID_WIDTH) // 2
    GRID_Y = (HEIGHT - GRID_HEIGHT) // 2


    for i in range(0, 9):
        cell_size = GRID_WIDTH // 3  # Calculate the size of each cell based on the grid dimensions
        row = i // 3  # Calculate the row index of the cell
        col = i % 3  # Calculate the column index of the cell
        x = GRID_X + col * cell_size  # Calculate the x-coordinate of the top-left corner of the cell
        y = GRID_Y + row * cell_size  # Calculate the y-coordinate of the top-left corner of the cell
        if arr[i] == 'X':
            text = FONT.render('X', True, RED)
            text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
            SCREEN.blit(text, text_rect)
        elif arr[i] == 'O':
            text = FONT.render('O', True, BLUE)
            SCREEN.blit(text, (x + cell_size // 2 - 20, y + cell_size // 2 - 20))  # Draw the 'O' text at the center of the cell
        pygame.draw.rect(SCREEN, BLACK, pygame.Rect(x, y, 100, 100), 2)
    if a == 1:
        message = FONT.render("Game Over", True, BLACK)
        SCREEN.blit(message, (WIDTH // 2 - 60, GRID_Y + GRID_HEIGHT + 10))
    elif a == 2:
        message = FONT.render("You Win", True, BLACK)
        SCREEN.blit(message, (WIDTH // 2 - 50, GRID_Y + GRID_HEIGHT + 10))
    elif a == 3:
        message = FONT.render("Draw", True, BLACK)
        SCREEN.blit(message, (WIDTH // 2 - 30, GRID_Y + GRID_HEIGHT + 10))
    pygame.display.flip()

def maxfind():
    global arr
    maxx = 0
    for block in range(0, 9):
        if arr[block] == 'X' and block not in dictt['X']:
            dictt['X'].append(block)
        if arr[block] == 'O' and block not in dictt['O']:
            dictt['O'].append(block)

    for gstate, wt in goal.items():
        counter = 0
        for elem in gstate:
            if elem in dictt['X']:
                counter -= 1
            elif elem in dictt['O']:
                counter += 1
        goal[gstate] = counter

    for gstate, wt in goal.items():
        wtm = abs(wt)
        if wtm >= abs(maxx):
            if wtm == abs(maxx) and maxx == 2:
                continue
            maxx = wt
    return maxx

def end():
    global a
    maxx = maxfind()
    if abs(maxx) == 3:
        if maxx == 3:
            a = 1
        else:
            a = 2
        return

    counterr = 0
    for i in arr:
        if i != 0:
            counterr += 1
    if counterr == 9:
        a = 3
        return

def comp():
    maxx = maxfind()
    if abs(maxx) == 1 or abs(maxx) == 0:
        while True:
            pos = random.randint(0, 8)
            if arr[pos] == 0:
                arr[pos] = 'O'
                end()
                return
    elif maxx == 2:
        for gstate, wt in goal.items():
            if wt == 2:
                for elem in gstate:
                    if elem not in dictt['O']:
                        arr[elem] = 'O'
                        end()
                        return
    elif maxx == -2:
        for gstate, wt in goal.items():
            if wt == -2:
                for elem in gstate:
                    if elem not in dictt['X']:
                        arr[elem] = 'O'
                        end()
                        return

def usinp(pos):
    if arr[pos] == 0:
        arr[pos] = 'X'
        end()
        return
    else:
        print("Place is taken.\n")

# Game Loop
running = True
disp()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and a == 0:
            pos = pygame.mouse.get_pos()
            #coordinates of the cell that the user has clicked on
            x, y = pos[0] // 100, pos[1] // 100
            #passing index of the cell that the user has clicked on 
            usinp(y * 3 + x)
            disp()
            if a != 0:
                continue
            comp()
            disp()

pygame.quit()
