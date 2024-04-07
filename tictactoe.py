import numpy as np
import random 

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
             #CHANGE2 -- added inner if statement
            if block not in dictt['X']:
                dictt['X'].append(block)
        #CHANGE3 -- changed elif to if 
        if (arr[block]=='O'):
             #CHANGE2 -- added inner if statement
            if block not in dictt['O']:
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
    """
    f(np.abs(maxx)==1 or np.abs(maxx)==0): #this is in case of first move,try to randomize
        for pos in range(0,9):
            if(arr[pos]==0):
                arr[pos]='O'
                break
    """
    #CHANGE4 -- changed the entire bit above in comments to the one below
    #was done so that the first move of O does not get fixed to just position 0 of the grid.#
    #better to randomise the first move of the comp to any position 
    #also added import random statement above
    checker=0
    if(np.abs(maxx)==1 or np.abs(maxx)==0): #this is in case of first move,try to randomize
        while checker==0:  
            pos = random.randint(0,8)    
            if(arr[pos]==0): 
                arr[pos]='O'
                checker=1
            
    elif(maxx==2):
        for gstate,wt in goal.items():
            if(wt==2):
                for elem in gstate:
                    if(elem not in dictt['O']):
                        arr[elem]='O'
                        #CHANGE5 -- added a break to avoid placing O in two places
                        #not sure if the problem of double moves is because of it cause the problem still persists
                        break

    elif(maxx==-2):
        for gstate,wt in goal.items():
            if(wt==-2):
                for elem in gstate:
                    if(elem not in dictt['X']):
                        arr[elem]='O'
                        #CHANGE5 -- added a break to avoid placing O in two places
                        #not sure if the problem of double moves is because of it cause the problem still persists
                        break

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
#~ dictt = {'X': [0,0,0,0,0,0,0,0,0], 'O': [0,0,0,0,0,0,0,0,0]}  #taken positions
#CHANGE 1, changed the above to the below since it was unnecessary to have the 0s present
dictt = {'X': [], 'O': []}
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