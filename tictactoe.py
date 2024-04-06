import numpy as np
#computer's turn
def disp():
    for i in range(0,9):
        print(arr[i],end=" ")
        if((i+1)%3==0):print("\n")
    print("-----")

def comp():
    global countX,countO,a
    #store taken positions
    for block in range(0,9):
        if (arr[block]=='X'):
            dict['X'].append(block)
        elif (arr[block]=='O'):
            dict['O'].append(block)

    for gstate, wt in goal.items():
        for elem in gstate:
            #assign weight to goal lists
            if elem in dict['X']:
                countX-1
            elif elem in dict['O']:
                countO+1

    if(countX==-2):wt=countX
    elif(countO==2):wt=countO
    else:wt=countO

    max=0
    for gstate, wt in goal.items():
        if(np.abs(wt)>max):max=wt
   
    #who's about to win?
    if(max<=1): #try to randomize
        for pos in range(0,9):
            if(arr[pos]==0):
                arr[pos]='O'
                break

    if(max==2):
        for gstate,wt in goal.items():
            if(wt==2):
                for elem in gstate:
                    if(elem not in dict['O']):
                        arr[elem]='O'

    elif(max==-2):
        for gstate,wt in goal.items():
            if(wt==-2):
                for elem in gstate:
                    if(elem not in dict['X']):
                        arr[elem]='O'

    if(np.abs(max)==3):
        if(max==3):print("GAME OVER")
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
    countX=countO=0 #reset weights of gstates
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
dict = {'X': [0,0,0,0,0,0,0,0,0], 'O': [0,0,0,0,0,0,0,0,0]}  #taken positions
countX=countO=0
a=0
disp()
while(a==0):
    usinp()
    disp()
    comp()
    disp()