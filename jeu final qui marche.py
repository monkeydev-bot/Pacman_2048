#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gameplay(n,value_max):
    grid=init_game(n)
    print(grid_to_string(grid))
    while get_value_player(grid)<value_max:
        pos_player=get_position_player(grid)
        pos_ennemi=get_position_ennemi(grid)
        pos_objectif=get_position_objectif(grid)
        command=read_player_command()

        if move_impossible(grid,pos_player,command):
            print("Mouvement impossible")
            continue

        if move_pos_player(grid,pos_player,command)!=move_pos_ennemi(pos_player,pos_ennemi,pos_objectif) and move_pos_player(grid,pos_player,command)!=pos_objectif and (move_pos_player(grid,pos_player,command),move_pos_ennemi(pos_player,pos_ennemi,pos_objectif))!=(pos_ennemi,pos_player):
            grid=move_player(grid,pos_player,command)
            grid=move_ennemi(grid,pos_player,pos_ennemi,pos_objectif)
            print(grid_to_string(grid))
        elif move_pos_player(grid,pos_player,command)==move_pos_ennemi(pos_player,pos_ennemi,pos_objectif) or (move_pos_player(grid,pos_player,command),move_pos_ennemi(pos_player,pos_ennemi,pos_objectif))==(pos_ennemi,pos_player):
            return('game over')
        else:
            grid=player_sur_objectif(grid,pos_player,pos_ennemi,pos_objectif)
            print(grid_to_string(grid))
    return('Gagné !')



    
def player_sur_objectif(grid,pos_player,pos_ennemy,pos_objectif):
    i0,j0=pos_player
    grid[i0][j0]=0
    pos_player=pos_objectif
    i1,j1=get_new_position(grid)
    new_abs_player,new_ord_player=pos_player
    value_player=grid[new_abs_player][new_ord_player]
    grid[i1][j1]=2*value_player
    abs_ennemy,ord_ennemy=pos_ennemy
    grid[abs_ennemy][ord_ennemy]=value_player/2
    return grid


    
def test_move_player():
    assert move_player([[0, 4, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [2, 0, 0, 0]],(3,0),'up')==[[0, 4, 0, 0], [0, 0, 1, 0], [2, 0, 0, 0], [0, 0, 0, 0]]
    

def move_ennemi(grid,pos_player,pos_ennemy,pos_objectif):
    old_abs_ennemy, old_ord_ennemy=pos_ennemy
    new_abs_ennemy, new_ord_ennemy=move_pos_ennemi(pos_player,pos_ennemy,pos_objectif)
    grid[new_abs_ennemy][new_ord_ennemy]=grid[old_abs_ennemy][old_ord_ennemy]
    grid[old_abs_ennemy][old_ord_ennemy]=0
    return grid
    
def create_grid(n):
    grid=[]
    for i in range(n):
        s=[0 for j in range(n)]
        grid.append(s)
    return grid

def grid_add_new_tile_at_position(grid,i,j,m):
    grid[i][j]==2**m
    return grid

def get_empty_tiles_positions(grid):
    n=len(grid)
    m=len(grid[0])
    pos=[]
    for i in range(n):
        for j in range(m):
            if grid[i][j]==0:
                pos.append((i,j))
    return pos

from random import randint

def get_new_position(grid):
    pos=get_empty_tiles_positions(grid)
    n=len(pos)
    a=randint(0,n-1)
    return pos[a]

def init_game(n):
    grid=create_grid(n)
    grid[n-1][0]=2
    i,j=get_new_position(grid)
    grid[i][j]=4
    s,t=get_new_position(grid)
    grid[s][t]=1
    return grid

def grid_to_string(grid,n):
    a=""""""
    for i in range(n):
        a=a+n*"="+ ' \n'
        for j in range(n):
            value=str(grid[i][j])
            a+='| '+value+' '
    a=a+n*"="+ ' \n'
    return a

def long_value(grid):
    m=0
    for x in grid:
        for y in x:
            if len(str(y))>m:
                m=len(str(y))
    return m

def grid_to_string_with_size(grid,n):
    longvalue=long_value(grid)
    a=""""""
    for i in range(n):
        a+=n*(longvalue*"=")+ ' \n'
        for j in range(n):
            value=str(grid[i][j])
            l=len(value)
            a+='|'+value+(longvalue-l)*' '
    a+=n*(longvalue*"=")+ ' \n'
    return a

def add_objectif_at_grid(grid):
    i,j=get_new_position(grid)
    return (i,j)
    
def creategrid(n):
    grid=[]
    for i in range(n):
        grid.append([0]*n)
    return grid


def grid_to_string(grid):
    
    THEMES = {
        "0": {"name": "Default", 1: "1" ,0: " ", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256",
              512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"},
        }
   
    
    size = len(grid)
    string = """"""
    entre_lignes=" "+("="*4+" ")*size + "\n"
    string+=entre_lignes
    for i in range(size):
        string += "|"
        for j in range(size):
            ch=THEMES["0"][grid[i][j]]
            while len(ch)<4:
                ch+=" "
            string+=ch
            string+="|"
        string+="\n"
        string+=entre_lignes
    
    return(string)
    
def create_grid(n):
    grid=[]
    for i in range(n):
        s=[0 for j in range(n)]
        grid.append(s)
    return grid

def grid_add_new_tile_at_position(grid,i,j,m):
    grid[i][j]==2**m
    return grid

def get_empty_tiles_positions(grid):
    n=len(grid)
    m=len(grid[0])
    pos=[]
    for i in range(n):
        for j in range(m):
            if grid[i][j]==0:
                pos.append((i,j))
    return pos

from random import randint

def get_new_position(grid):
    pos=get_empty_tiles_positions(grid)
    n=len(pos)
    a=randint(0,n-1)
    return pos[a]

def init_game(n):
    grid=create_grid(n)
    grid[n-1][0]=2
    i,j=get_new_position(grid)
    grid[i][j]=4
    s,t=get_new_position(grid)
    grid[s][t]=1
    return grid
    
def move_pos_ennemi(position_player, position_ennemi, position_objectif):
    ligne_ennemi, colonne_ennemi = position_ennemi
    ligne_player, colonne_player = position_player
    ligne_objectif, colonne_objectif = position_objectif
    if ligne_ennemi == ligne_player :
        if (colonne_player < colonne_ennemi) and (ligne_ennemi != ligne_objectif or colonne_ennemi != colonne_objectif + 1 ) :
            colonne_ennemi -= 1
        elif (colonne_player < colonne_ennemi) and (ligne_ennemi == ligne_objectif and colonne_ennemi == colonne_objectif + 1 ):
            colonne_ennemi -= 2
        elif (colonne_player > colonne_ennemi) and (ligne_ennemi != ligne_objectif or colonne_ennemi != colonne_objectif - 1 ):
            colonne_ennemi += 1
        else:
            colonne_ennemi += 2
    elif colonne_ennemi == colonne_player:
        if (ligne_player < ligne_ennemi) and (colonne_ennemi != colonne_objectif or ligne_ennemi != ligne_objectif + 1 ) :
            ligne_ennemi -= 1
        elif (ligne_player < ligne_ennemi) and (colonne_ennemi == colonne_objectif and ligne_ennemi == ligne_objectif + 1 ):
            ligne_ennemi -= 2
        elif (ligne_player > ligne_ennemi) and (colonne_ennemi != colonne_objectif or ligne_ennemi != ligne_objectif - 1 ):
            ligne_ennemi += 1
        else:
            ligne_ennemi += 2
    elif (colonne_player > colonne_ennemi) and (ligne_ennemi != ligne_objectif or colonne_ennemi!=colonne_objectif -1):
        colonne_ennemi+= 1
    elif (colonne_player > colonne_ennemi) and (ligne_ennemi == ligne_objectif or colonne_ennemi==colonne_objectif -1):
        if (ligne_player > ligne_ennemi):
            ligne_ennemi+=1
        else:
            ligne_ennemi-= 1
    elif (colonne_player < colonne_ennemi) and (ligne_ennemi != ligne_objectif or colonne_ennemi!=colonne_objectif + 1):
        colonne_ennemi -= 1
    elif (colonne_player < colonne_ennemi) and (ligne_ennemi == ligne_objectif and colonne_ennemi==colonne_objectif + 1):
        if (ligne_player > ligne_ennemi):
            ligne_ennemi += 1
        else :
            ligne_ennemi -= 1

    return ligne_ennemi, colonne_ennemi


def test_move_pos_ennemi():
    assert move_pos_ennemi((1,1),(5,1),(3,4))== (4,1)
    assert move_pos_ennemi((1,1), (5,1), (4,1))== (3,1)
    assert move_pos_ennemi((2,1), (2,6), (1,5))== (2,5)
    assert move_pos_ennemi((2,1), (2,6), (2,5))== (2,4)
    assert move_pos_ennemi((1,1), (5,5), (3,3))== (5,4)
    assert move_pos_ennemi((1,1), (5,5), (5,4))== (4,5)
    assert move_pos_ennemi((7,0), (1,5), (2,4))== (1,4)
    assert move_pos_ennemi((7,0), (1,5), (1,4))== (2,5)
    assert move_pos_ennemi((2,3), (4,3), (3,3))== (2,3)

def get_position_player(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==(get_value_objectif(grid)/2):
                return((i,j))

def get_value_objectif(grid):
    return(max(get_value_in_grid(grid)))
    
def get_value_in_grid(grid):
    l=[]
    for i in range(len(grid)):
        for j in range(len(grid)):
            l.append(grid[i][j])
    return(l)
    
    
def get_value_player(grid):
    return (get_value_objectif(grid)/2)
    

def read_player_command():
    command=raw_input('Entrez une direction ( up,down,right or left ): ')
    return command


def move_pos_player(grid,pos_player,command):
    
    n=len(grid)
    
    if command=='up' or command=='z':
        if pos_player[0]==0:
            return ('Mouvement impossible' )
        else:
            
            return (pos_player[0]-1,pos_player[1])
    elif command=='down' or command=='s':
        if pos_player[0]==n-1:
            return ('Mouvement impossible' )
        else:
            
            return (pos_player[0]+1,pos_player[1])
    elif command=='right' or command=='d':
        if pos_player[1]==n-1:
            return ('Mouvement impossible' )
        else:
            return (pos_player[0], pos_player[1]+1)
    elif command=='left' or command=='q':
        if pos_player[1]==0:
            return ('Mouvement impossible' )
        else:
             return (pos_player[0], pos_player[1]-1)


    
def get_value_in_grid(grid):
    l=[]
    for i in range(len(grid)):
        for j in range(len(grid)):
            l.append(grid[i][j])
    return(l)
    
    
def test_get_value_in_grid():
    assert get_value_in_grid([[0,2,2,2],[0,0,4,0],[0,8,16,2],[0,0,0,0]])==[0, 2, 2, 2, 0, 0, 4, 0, 0, 8, 16, 2, 0, 0, 0, 0]
    

def get_value_objectif(grid):
    return(max(get_value_in_grid(grid)))
    
    
def test_get_value_objectif():
    assert get_value_objectif([[0,0,0,0],[0,0,0,0],[0,8,16,0],[4,0,0,0]])==16
    
def get_position_objectif(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==get_value_objectif(grid):
                return((i,j))
            
def test_get_position_objectif():
    assert get_position_objectif([[0,0,0,0],[0,0,4,0],[0,8,16,0],[0,0,0,0]])==(2,2)
    
def get_position_ennemi(grid) :
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==(get_value_objectif(grid)/4):
                return((i,j))
       
def test_get_position_ennemi():
    assert get_position_ennemi([[0,0,0,0],[0,0,4,0],[0,8,16,0],[0,0,0,0]])==(1,2)   

def get_position_player(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==(get_value_objectif(grid)/2):
                return((i,j))
                
def test_get_position_player():
    assert get_position_player([[0,0,0,0],[0,0,4,0],[0,8,16,0],[0,0,0,0]])==(2,1)


def move_player(grid,pos_player,commande):
    old_abs_player,old_ord_player=pos_player
    new_abs_player,new_ord_player=move_pos_player(grid,pos_player,commande)
    grid[new_abs_player][new_ord_player]=grid[old_abs_player][old_ord_player]
    grid[old_abs_player][old_ord_player]=0
    return grid


def move_impossible(grid,pos_player,command):
    n=len(grid)
    if (command=='up' or command=='z') and pos_player[0]==0 :
        return True
    if (command=='down' or command=='s') and pos_player[0]==n-1 :
        return True
    if (command=='right' or command=='d') and pos_player[1]==n-1 :
        return True
    if (command=='left' or command=='q') and pos_player[1]==0 :
        return True



gameplay(5,2048)
