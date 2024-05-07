import numpy as np
import pygame
import random

#mandatory init for the gui to work 
pygame.init()

#setting up the screen 
screen_width = 800
screen_height = 900
screen = pygame.display.set_mode((screen_width,screen_height)) 
pygame.display.set_caption("Tic Tac Toe")


#screen variables
YELLOW = (255, 255, 0)
DARK_YELLOW = (204, 204, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
cell_size = min(screen_width, screen_height - 100) // 3

## GUI FUNCTIONS::
#to draw the grid 
def draw_grid():
    pygame.draw.rect(screen, YELLOW, (200, 200, 400, 400))
    for i in range(1, 3):
        pygame.draw.line(screen, DARK_YELLOW, (200, 200 + i * cell_size), (600, 200 + i * cell_size), 3)
        pygame.draw.line(screen, DARK_YELLOW, (200 + i * cell_size, 200), (200 + i * cell_size, 600), 3)


#computer's turn
def disp():
    for i in range(0,9):
        print(arr[i],end=" ")
        if((i+1)%3==0):print("\n")
    print("-----")

def comp():
    global counter,a, arr
    #store taken positions
    for block in range(0,9):
        if (arr[block]=='X'):
            dictt['X'].append(block)
        elif (arr[block]=='O'):
            dictt['O'].append(block)

    for gstate, wt in goal.items():
        counter=0
        for elem in gstate:
            #assign weight to goal lists
            if elem in dictt['X']:
                counter-=1
            elif elem in dictt['O']:
                counter+=1
        goal[gstate]=counter

    maxx=0 #which goal state has most weight
    for gstate, wt in goal.items():
        wtm=np.abs(wt)
        if(wtm>np.abs(maxx)):
            maxx=wt
   
    #who's about to win?
    if(np.abs(maxx)==1 or np.abs(maxx)==0): #try to randomize
        for pos in range(0,9):
            if(arr[pos]==0):
                arr[pos]='O'
                break

    elif(maxx==2):
        for gstate,wt in goal.items():
            if(wt==2):
                for elem in gstate:
                    if(elem not in dictt['O']):
                        arr[elem]='O'

    elif(maxx==-2):
        for gstate,wt in goal.items():
            if(wt==-2):
                for elem in gstate:
                    if(elem not in dictt['X']):
                        arr[elem]='O'

    if(np.abs(maxx)==3):
        if(maxx==3):print("GAME OVER")
        else:print("YOU WIN")
        a=1
        return
    
    counterr=0
    for i in arr:
        if i!=0:
            counterr+1
    if (counterr==9): #draw state
        print("DRAW")
        a=1
        return
    counter=0 #reset weights of gstates
    a=0

#user turn
def usinp():
    usinput = int(input("Enter position of X:"))
    if ((arr[usinput]) == 0):
        arr[usinput] = 'X'
    else:
        print("Place is taken.\n")
        usinp()

#initialize
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
goal={(0,4,8):0,(1,4,7):0,(0,1,2):0,(2,4,6):0,(0,3,6):0,(3,4,5):0,(2,5,8):0,(6,7,8):0}
dictt = {'X': [0,0,0,0,0,0,0,0,0], 'O': [0,0,0,0,0,0,0,0,0]}  #taken positions
counter=0
a=0
disp()
while(a==0):
    usinp()
    disp()
    print("b")
    print(goal)
    comp()
    print("a")
    print(goal)
    disp()

#game loop 
running = True
while running:
    #functionality for cross button (close)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #background of screen = black
    screen.fill(BLACK)

    #DRAW grid
    draw_grid()

    #mandatory statement so that display is properly updated
    pygame.display.update()