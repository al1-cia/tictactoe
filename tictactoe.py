import numpy as np
import random 

def disp():
    for i in range(0,9):
        print(arr[i],end=" ")
        if((i+1)%3==0):print("\n")
    print("-----")

def maxfind():
    global arr
    maxx=0
    #store taken positions
    for block in range(0,9):
        if (arr[block]=='X' and block not in dictt['X']):
            dictt['X'].append(block)
        if (arr[block]=='O' and block not in dictt['O']):
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

    #which goal state has most weight
    for gstate, wt in goal.items():
        wtm=np.abs(wt)
        if(wtm>np.abs(maxx)):
            maxx=wt
    return maxx
  
def end():
    global a
    maxx=maxfind()
    if(np.abs(maxx)==3):
        if(maxx==3):print("GAME OVER")
        else:print("YOU WIN")
        a=1
        return
    
    #draw state
    counterr=0
    for i in arr:
        if i!=0:
            counterr+=1
    if (counterr==9): 
        print("DRAW")
        a=1
        return
    
#computer's turn
def comp():
    #who's about to win?
    maxx=maxfind()
    #randomizing first move
    if(np.abs(maxx)==1 or np.abs(maxx)==0): 
        while True:  
            pos = random.randint(0,8)    
            if(arr[pos]==0): 
                arr[pos]='O'
                end()
                return
            
    elif(maxx==2):
        for gstate,wt in goal.items():
            if(wt==2):
                for elem in gstate:
                    if(elem not in dictt['O']):
                        arr[elem]='O'
                        end()
                        return

    elif(maxx==-2):
        for gstate,wt in goal.items():
            if(wt==-2):
                for elem in gstate:
                    if(elem not in dictt['X']):
                        arr[elem]='O'
                        end()
                        return

    a=0

#user turn
def usinp():
    usinput = int(input("Enter position of X:"))
    if ((arr[usinput]) == 0):
        arr[usinput] = 'X'
        end()
        return
    else:
        print("Place is taken.\n")
        usinp()

#initialize
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
goal={(0,4,8):0,(1,4,7):0,(0,1,2):0,(2,4,6):0,(0,3,6):0,(3,4,5):0,(2,5,8):0,(6,7,8):0}
dictt = {'X': [], 'O': []}
counter=0
a=0
disp()
while(a==0):
    usinp()
    disp()
    if(a==1):continue
    comp()
    disp()