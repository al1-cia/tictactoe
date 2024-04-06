def check():
    global countX,countO,a
    #store taken positions
    for block in range(0,9):
        if (arr[block]=='X'):
            dict['X'].append(block)
        elif (arr[block]=='O'):
            dict['O'].append(block)

    for lst in goal:
        for elem in lst:
            #assign weight to goal lists
            if elem in dict['X']:
                countX+1
            elif elem in dict['O']:
                countO+1
        if(countX==2):lst.extend([-countX])
        elif(countO==2):lst.extend([countO])
        else:lst.extend([countO])

    max=0
    for lst in goal:
        if(lst[3]>max):max=lst[3]
    
    #who's about to win?
    if(max==1):
        for pos in range(0,9):
            if(arr[pos]!=0):
                arr[pos]='O'

    if(max==2):
        for elem in lst:
            if(elem not in dict['X']):
                arr[elem]='O'
    elif(max==-2):
        for elem in lst:
            if(elem not in dict['O']):
                arr[elem]='O'
    if(max==3 or max==-3):
        print(arr)
        if(max==3):print("GAME OVER")
        else:print("YOU WIN")
        a=1
        return
    countX=countO=0 #reset weight of list
    a= 0
    print(arr)

#user turn
def usinp():
    usinput = int(input("Enter position of X:"))
    if ((arr[usinput]) == 0):
        arr[usinput] = 'X'
        print(arr)
    else:
        print("Place is taken.\n")
        usinp()
#computer turn
def comp():
    check()

#initialize
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
goal=[[0,4,8],[1,4,7],[0,1,2],[2,4,6],[0,3,6],[3,4,5],[2,5,8],[6,7,8]]
dict = {'X': [0,0,0,0,0,0,0,0,0], 'O': [0,0,0,0,0,0,0,0,0]}  # taken positions
countX=countO=0
a=0
print(arr)
while(a==0):
    usinp()
    comp()
