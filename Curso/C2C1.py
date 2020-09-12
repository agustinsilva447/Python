import numpy as np

def imprimir_table(table):
    print("/|0|1|2|")
    for i in range(3):
        print(i, end="")
        for j in range(3):
            print("|", end="")
            if table[i,j]==0 :
                print("_", end="")
            if table[i,j]==1 :
                print("X", end="")
            if table[i,j]==2 :
                print("O", end="")        
        print("|")

def is_done(table):
    for i in range(3):
        for j in range(1,3):
            if (table[i,0]==j and table[i,1]==j and table[i,2]==j) :
                return 0,j
            if (table[0,i]==j and table[1,i]==j and table[2,i]==j) :
                return 0,j
            if (table[0,0]==j and table[1,1]==j and table[2,2]==j) :
                return 0,j
            if (table[0,2]==j and table[1,1]==j and table[2,0]==j) :
                return 0,j     
    if np.all(table!=0):
        return 0,0
    return 1,0

tablero = np.zeros([3, 3])

print("Choose X or O:")
simbol = input()
print("Xs begin...")
done = 1
win = 0
pieza = 1

while done:
    imprimir_table(tablero)
    
    print("Set coordinates (X,Y) from 0 to 2:")
    coord_x = int(input())
    coord_y = int(input())
    
    if tablero[coord_x, coord_y] == 0:
        tablero[coord_x, coord_y] = pieza   
        if pieza == 1:
            pieza = 2
        elif pieza == 2:
            pieza = 1
    else:
        print("That spot is occupied!")

    done, win = is_done(tablero)

imprimir_table(tablero)

if win == 0:
    print("Nobody won!")
if win == 1:
    print("Congratulations, Xs won!")
if win == 2:
    print("Congratulations, Os won!")