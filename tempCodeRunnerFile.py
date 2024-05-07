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
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
DARK_YELLOW = (204, 204, 0)
NEON_ORANGE = (255, 165, 0)

# Centering the grid 
GRID_WIDTH = 300  # Width of the grid
GRID_HEIGHT = 300  # Height of the grid
GRID_X = (WIDTH - GRID_WIDTH) // 2
GRID_Y = (HEIGHT - GRID_HEIGHT) // 2 - 50  # Shifting the entire layout 50 pixels above

# Fonts
message_font = pygame.font.SysFont("Times New Roman", 40)
symbol_font = pygame.font.SysFont("Times New Roman", 40, bold=True)

# Game variables
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
goal = {(0, 4, 8): 0, (1, 4, 7): 0, (0, 1, 2): 0, (2, 4, 6): 0, (0, 3, 6): 0, (3, 4, 5): 0, (2, 5, 8): 0, (6, 7, 8): 0}
dictt = {'X': [], 'O': []}
a = 0  # Game over flag

# Functions
def disp():
    SCREEN.fill(WHITE)

    # Draw Tic Tac Toe heading
    heading_font = pygame.font.SysFont("Times New Roman", 100)
    heading_text = heading_font.render("Tic Tac Toe", True, NEON_ORANGE)  # Neon Orange color
    heading_rect = heading_text.get_rect(center=(WIDTH // 2, GRID_Y - 100))  # Positioned above the grid
    SCREEN.blit(heading_text, heading_rect)

    for i in range(0, 9):
        cell_size = GRID_WIDTH // 3  # Calculate the size of each cell based on the grid dimensions
        row = i // 3  # Calculate the row index of the cell
        col = i % 3  # Calculate the column index of the cell
        x = GRID_X + col * cell_size  # Calculate the x-coordinate of the top-left corner of the cell
        y = GRID_Y + row * cell_size  # Calculate the y-coordinate of the top-left corner of the cell
        pygame.draw.rect(SCREEN, YELLOW, pygame.Rect(x, y, 100, 100))  # Draw grid background

        # Draw thicker grid lines
        line_width = 3
        pygame.draw.rect(SCREEN, DARK_YELLOW, pygame.Rect(x, y, 100, 100), line_width)  # Draw grid lines

        if arr[i] == 'X':
            text = symbol_font.render('X', True, RED)
            text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
            SCREEN.blit(text, text_rect)
        elif arr[i] == 'O':
            text = symbol_font.render('O', True, BLUE)
            text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
            SCREEN.blit(text, text_rect)

    # Draw thicker outer border of the grid
    border_rect = pygame.Rect(GRID_X - 2, GRID_Y - 2, GRID_WIDTH + 4, GRID_HEIGHT + 4)
    pygame.draw.rect(SCREEN, DARK_YELLOW, border_rect, line_width) 

    if a == 1:
        message = message_font.render("Game Over", True, BLACK)
        SCREEN.blit(message, (WIDTH // 2 - 90, GRID_Y + GRID_HEIGHT + 10))
    elif a == 2:
        message = message_font.render("You Win", True, BLACK)
        SCREEN.blit(message, (WIDTH // 2 - 70, GRID_Y + GRID_HEIGHT + 10))
    elif a == 3:
        message = message_font.render("Draw", True, BLACK)
        SCREEN.blit(message, (WIDTH // 2 - 40, GRID_Y + GRID_HEIGHT + 10))
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
        print("Game state updated to:", a)  # Debug statement
        return

    counterr = 0
    for i in arr:
        if i != 0:
            counterr += 1
    if counterr == 9:
        a = 3
        print("Game state updated to:", a)  # Debug statement
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
    row = pos // 3  # Calculate the row index of the cell
    col = pos % 3   # Calculate the column index of the cell
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
            # Coordinates of the cell that the user has clicked on
            x, y = pos[0] - GRID_X, pos[1] - GRID_Y
            cell_size = GRID_WIDTH // 3
            cell_x = x // cell_size
            cell_y = y // cell_size
            cell_index = cell_y * 3 + cell_x
            usinp(cell_index)
            disp()
            if a != 0:
                continue
            comp()
            disp()

pygame.quit()
