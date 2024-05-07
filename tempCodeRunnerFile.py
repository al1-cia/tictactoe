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
    for i in range(0, 9):
        x = (i % 3) * 100
        y = (i // 3) * 100
        if arr[i] == 'X':
            text = FONT.render('X', True, RED)
            SCREEN.blit(text, (x + 40, y + 40))
        elif arr[i] == 'O':
            text = FONT.render('O', True, BLUE)
            SCREEN.blit(text, (x + 40, y + 40))
        pygame.draw.rect(SCREEN, BLACK, pygame.Rect(x, y, 100, 100), 2)
    if a == 1:
        message = FONT.render("Game Over", True, BLACK)
        SCREEN.blit(message, (50, 310))
    elif a == 2:
        message = FONT.render("You Win", True, BLACK)
        SCREEN.blit(message, (70, 310))
    elif a == 3:
        message = FONT.render("Draw", True, BLACK)
        SCREEN.blit(message, (90, 310))
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
            x, y = pos[0] // 100, pos[1] // 100
            usinp(y * 3 + x)
            disp()
            if a != 0:
                continue
            comp()
            disp()

pygame.quit()
