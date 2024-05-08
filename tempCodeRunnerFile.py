import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 900, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DARK_YELLOW = (204, 204, 0)
NEON_ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
GREEN = (0, 128, 0)
DARK_BLUE = (0, 0, 128)

# Centering the grid
GRID_WIDTH = 300
GRID_HEIGHT = 300
GRID_X = (WIDTH - GRID_WIDTH) // 2
GRID_Y = (HEIGHT - GRID_HEIGHT) // 2 - 50

# Fonts
message_font = pygame.font.SysFont("Times New Roman", 40)
symbol_font = pygame.font.SysFont("Times New Roman", 40, bold=True)

# Game variables
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
goal = {(0, 4, 8): 0, (1, 4, 7): 0, (0, 1, 2): 0, (2, 4, 6): 0, (0, 3, 6): 0, (3, 4, 5): 0, (2, 5, 8): 0, (6, 7, 8): 0}
dictt = {'X': [], 'O': []}
a = 0  # Game over flag
player_score = 0
computer_score = 0

# Define button dimensions and spacing
BUTTON_WIDTH = 180
BUTTON_HEIGHT = 80
BUTTON_SPACE_TO_EDGE = 50
BUTTON_SPACING = 26

def disp():
    global score_button, play_again_button, restart_game_button, quit_button

    SCREEN.fill(WHITE)

    # Draw Tic Tac Toe heading
    heading_font = pygame.font.SysFont("Times New Roman", 100)
    heading_text = heading_font.render("Tic Tac Toe", True, NEON_ORANGE)
    heading_rect = heading_text.get_rect(center=(WIDTH // 2, GRID_Y - 100))
    SCREEN.blit(heading_text, heading_rect)

    for i in range(0, 9):
        cell_size = GRID_WIDTH // 3
        row = i // 3
        col = i % 3
        x = GRID_X + col * cell_size
        y = GRID_Y + row * cell_size
        pygame.draw.rect(SCREEN, YELLOW, pygame.Rect(x, y, 100, 100))

        # Draw grid lines
        line_width = 3
        pygame.draw.rect(SCREEN, DARK_YELLOW, pygame.Rect(x, y, 100, 100), line_width)

        if arr[i] == 'X':
            text = symbol_font.render('X', True, RED)
            text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
            SCREEN.blit(text, text_rect)
        elif arr[i] == 'O':
            text = symbol_font.render('O', True, BLUE)
            text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
            SCREEN.blit(text, text_rect)

    # Draw  outer border of the grid
    border_rect = pygame.Rect(GRID_X - 2, GRID_Y - 2, GRID_WIDTH + 4, GRID_HEIGHT + 4)
    pygame.draw.rect(SCREEN, DARK_YELLOW, border_rect, line_width)

    # Draw message
    if a == 1:
        message = message_font.render("Game Over", True, BLACK)
        SCREEN.blit(message, (WIDTH // 2 - 90, GRID_Y + GRID_HEIGHT + 10))
    elif a == 2:
        message = message_font.render("You Win", True, BLACK)
        SCREEN.blit(message, (WIDTH // 2 - 70, GRID_Y + GRID_HEIGHT + 10))
    elif a == 3:
        message = message_font.render("Draw", True, BLACK)
        SCREEN.blit(message, (WIDTH // 2 - 40, GRID_Y + GRID_HEIGHT + 10))

    # Draw score button
    score_button = pygame.Rect(BUTTON_SPACE_TO_EDGE, HEIGHT - BUTTON_HEIGHT - BUTTON_SPACE_TO_EDGE, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(SCREEN, GREEN, score_button, border_radius=10)
    score_text_line1 = message_font.render("X: " + str(player_score), True, WHITE)
    score_text_line2 = message_font.render("O: " + str(computer_score), True, WHITE)
    score_text_rect_line1 = score_text_line1.get_rect(center=(score_button.center[0], score_button.center[1] - 20))
    score_text_rect_line2 = score_text_line2.get_rect(center=(score_button.center[0], score_button.center[1] + 20))
    SCREEN.blit(score_text_line1, score_text_rect_line1)
    SCREEN.blit(score_text_line2, score_text_rect_line2)

    # Draw play again button
    play_again_button = pygame.Rect(BUTTON_SPACE_TO_EDGE + BUTTON_WIDTH + BUTTON_SPACING, HEIGHT - BUTTON_HEIGHT - BUTTON_SPACE_TO_EDGE, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(SCREEN, RED, play_again_button, border_radius=10)
    play_again_text_line1 = message_font.render("Play", True, WHITE)
    play_again_text_line2 = message_font.render("Again", True, WHITE)
    play_again_text_rect1 = play_again_text_line1.get_rect(center=(play_again_button.center[0], play_again_button.center[1] - 20))
    play_again_text_rect2 = play_again_text_line2.get_rect(center=(play_again_button.center[0], play_again_button.center[1] + 20))
    SCREEN.blit(play_again_text_line1, play_again_text_rect1)
    SCREEN.blit(play_again_text_line2, play_again_text_rect2)

    # Draw restart game button
    restart_game_button = pygame.Rect(BUTTON_SPACE_TO_EDGE + 2 * (BUTTON_WIDTH + BUTTON_SPACING), HEIGHT - BUTTON_HEIGHT - BUTTON_SPACE_TO_EDGE, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(SCREEN, DARK_BLUE, restart_game_button, border_radius=10)
    restart_game_text_line1 = message_font.render("Restart", True, WHITE)
    restart_game_text_line2 = message_font.render("Game", True, WHITE)
    restart_game_text_rect1 = restart_game_text_line1.get_rect(center=(restart_game_button.center[0], restart_game_button.center[1] - 20))
    restart_game_text_rect2 = restart_game_text_line2.get_rect(center=(restart_game_button.center[0], restart_game_button.center[1] + 20))
    SCREEN.blit(restart_game_text_line1, restart_game_text_rect1)
    SCREEN.blit(restart_game_text_line2, restart_game_text_rect2)

    # Draw quit button
    quit_button = pygame.Rect(WIDTH - BUTTON_SPACE_TO_EDGE - BUTTON_WIDTH, HEIGHT - BUTTON_HEIGHT - BUTTON_SPACE_TO_EDGE, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(SCREEN, PURPLE, quit_button, border_radius=10)
    quit_text = message_font.render("Quit", True, WHITE)
    quit_text_rect = quit_text.get_rect(center=quit_button.center)
    SCREEN.blit(quit_text, quit_text_rect)

    pygame.display.flip()


def reset_game():
    global arr, a, dictt
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    dictt = {'X': [], 'O': []}
    a = 0

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
    global a, player_score, computer_score
    maxx = maxfind()
    if abs(maxx) == 3:
        if maxx == 3:
            a = 1
            computer_score += 1
        else:
            a = 2
            player_score += 1
        print("Game state updated to:", a)
        return

    counterr = 0
    for i in arr:
        if i != 0:
            counterr += 1
    if counterr == 9:
        a = 3
        print("Game state updated to:", a)
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
    if 0 <= pos <= 8:
        row = pos // 3
        col = pos % 3
        if arr[pos] == 0:
            arr[pos] = 'X'
            end()
            return

# Game Loop
running = True
disp()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and a == 0:
            pos = pygame.mouse.get_pos()
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
            disp()# Inside the game loop
        elif event.type == pygame.MOUSEBUTTONDOWN and a != 0:
            if quit_button.collidepoint(event.pos):
                running = False  # Set running to False to exit the game loop
            elif play_again_button.collidepoint(event.pos):
                reset_game()
                disp()
            elif restart_game_button.collidepoint(event.pos):
                reset_game()
                player_score = 0
                computer_score = 0
                disp()
pygame.quit()