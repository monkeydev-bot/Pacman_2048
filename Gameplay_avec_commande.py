from random import randint
import pygame
from pygame.locals import *

pygame.init()

#Lance le jeu dans son ensemble
def gameplay(n,value_max): #n: taille de la grille, value_max : score a attendre pour gagner
    """
    Play a game.
    """
    grid=init_game(n)
    print(grid_to_string(grid))
    continuer = True
    while continuer:

        for event in pygame.event.get():  # On parcours la liste de tous les evenements recus

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    command = 'up'

                if event.key == K_DOWN:
                    command = 'down'

                if event.key == K_RIGHT:
                    command = 'right'
                if event.key == K_LEFT:
                    command = 'left'
                pos_player=get_position_player(grid)
                pos_ennemi=get_position_ennemi(grid)
                pos_objectif=get_position_objectif(grid)
                if move_impossible(grid,pos_player,command):
                    print("Mouvement impossible")
                    continue

                if move_pos_player(grid,pos_player,command)!=move_pos_ennemi(pos_player,pos_ennemi,pos_objectif) and move_pos_player(grid,pos_player,command)!=pos_objectif and (move_pos_player(grid,pos_player,command),move_pos_ennemi(pos_player,pos_ennemi,pos_objectif))!=(pos_ennemi,pos_player):
                    grid=move_player(grid,pos_player,command)
                    grid=move_ennemi(grid,pos_player,pos_ennemi,pos_objectif)
                    print(grid_to_string(grid))

                elif move_pos_player(grid,pos_player,command)==move_pos_ennemi(pos_player,pos_ennemi,pos_objectif) or (move_pos_player(grid,pos_player,command),move_pos_ennemi(pos_player,pos_ennemi,pos_objectif))==(pos_ennemi,pos_player):
                    print('game over')
                    continuer=False

                else:
                    grid=player_sur_objectif(grid,pos_player,pos_ennemi,pos_objectif)
                    print(grid_to_string(grid))

    return('Gagne !')

liste_commandes=['up','down','left','right','q','z','s','d']

#Lorsque le joueur atteint l'objectif, celui double de valeur et change de place aleatoirement. Le joueur double de valeur.L'ennemi double de valeur.
def player_sur_objectif(grid,pos_player,pos_ennemy,pos_objectif):
    """
    Calculate a list.
    """
    i0,j0=pos_player
    grid[i0][j0]=0 #l'ancienne case du joueur est remplacee par un 0
    pos_player=pos_objectif
    i1,j1=get_new_position(grid)  #Nouvelle position de l'objectif, choisit aleatoirement
    new_abs_player,new_ord_player=pos_player
    value_player=grid[new_abs_player][new_ord_player] # On prend la valeur du joueur
    grid[i1][j1]=2*value_player #la valeur de l'objectif est doublee par rapport au joueur
    abs_ennemy,ord_ennemy=pos_ennemy
    grid[abs_ennemy][ord_ennemy]=value_player/2 #la valeur de l'ennemi est la moitie de celle du joueur
    return grid

#Change la place du joueur sur la grille suite a une commande
def move_player(grid,pos_player,commande):
    """
    Move a player to a player.
    """
    old_abs_player,old_ord_player=pos_player
    new_abs_player,new_ord_player=move_pos_player(grid,pos_player,commande) #Nouvelle position du joueur
    grid[new_abs_player][new_ord_player]=grid[old_abs_player][old_ord_player] #Mise a jour de la nouvelle position
    grid[old_abs_player][old_ord_player]=0 #l'ancienne position vaut 0
    return grid

#
def test_move_player():
    """
    Make player move move.
    """
    assert move_player([[0, 4, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [2, 0, 0, 0]],(3,0),'up')==[[0, 4, 0, 0], [0, 0, 1, 0], [2, 0, 0, 0], [0, 0, 0, 0]]

#Change la place de l'ennemi sur la grille
def move_ennemi(grid,pos_player,pos_ennemy,pos_objectif):
    """
    Moves the player.
    """
    old_abs_ennemy, old_ord_ennemy=pos_ennemy
    new_abs_ennemy, new_ord_ennemy=move_pos_ennemi(pos_player,pos_ennemy,pos_objectif) #Nouvelle position de l'ennemi
    grid[new_abs_ennemy][new_ord_ennemy]=grid[old_abs_ennemy][old_ord_ennemy] #Mise a jour de la nouvelle position
    grid[old_abs_ennemy][old_ord_ennemy]=0 #l'ancienne position vaut 0
    return grid

#Cree une grille de taille nxn remplie de 0
def create_grid(n):
    """
    Create a list of n - dimensional sequences
    """
    grid=[]
    for i in range(n):
        s=[0 for j in range(n)]
        grid.append(s)
    return grid

#Ajoute un 2**m a la position i,j de grid
def grid_add_new_tile_at_position(grid,i,j,m):
    """
    Returns a new grid at a given position
    """
    grid[i][j]==2**m
    return grid

#Retourne la liste des couples de position vide
def get_empty_tiles_positions(grid):
    """
    Return a list of positions that are empty.
    """
    n=len(grid)
    pos=[]
    for i in range(n):
        for j in range(n):
            if grid[i][j]==0:
                pos.append((i,j))
    return pos

#Renvoie une position aleatoire parmis les positions non occupees
def get_new_position(grid):
    """
    Return a list of a grid positions.
    """
    pos=get_empty_tiles_positions(grid)
    n=len(pos)
    a=randint(0,n-1)
    return pos[a]

#Cree la grille initiale avec le joueur en bas a gauche, l'ennemi place aleatoirement et l'objectif place aleatoirement
def init_game(n):
    """
    Create a game instance.
    """
    grid=create_grid(n)
    grid[n-1][0]=2 #positionnement du joueur
    i,j=get_new_position(grid)
    grid[i][j]=4 #positionnement de l'objectif
    s,t=get_new_position(grid)
    grid[s][t]=1 #positionnement de l'ennemi
    return grid

#Fonction non utilisee. Renvoie la taille de la plus grande chaine de caracteres presente dans la grille.
def long_value(grid):
    """
    Convert longitude to longitude.
    """
    m=0
    for x in grid:
        for y in x:
            if len(str(y))>m:
                m=len(str(y))
    return m

#Fonction non utilisee.
def grid_to_string_with_size(grid,n):
    """
    Convert a string to a string.
    """
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

#Retourne la nouvelle position de l'objectif.
def add_objectif_at_grid(grid):
    """
    Return a new position to the grid.
    """
    i,j=get_new_position(grid)
    return (i,j)

#Affiche la grille de maniere "propre" dans la console
def grid_to_string(grid):
    """
    Convert grid to string.
    """

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

#Retourne la nouvelle position de l'ennemi. L'ennemi suit le joueur.
def move_pos_ennemi(position_player, position_ennemi, position_objectif):
    """
    Move the player position.
    """
    ligne_ennemi, colonne_ennemi = position_ennemi
    ligne_player, colonne_player = position_player
    ligne_objectif, colonne_objectif = position_objectif
    if ligne_ennemi == ligne_player : #Si l'ennemi et le joueur sont sur la meme ligne, l'ennemi avance vers le joueur. Si il est derriere l'objectif, il saute l'objectif en sautant de 2 places.
        if (colonne_player < colonne_ennemi) and (ligne_ennemi != ligne_objectif or colonne_ennemi != colonne_objectif + 1 ) :
            colonne_ennemi -= 1
        elif (colonne_player < colonne_ennemi) and (ligne_ennemi == ligne_objectif and colonne_ennemi == colonne_objectif + 1 ):
            colonne_ennemi -= 2
        elif (colonne_player > colonne_ennemi) and (ligne_ennemi != ligne_objectif or colonne_ennemi != colonne_objectif - 1 ):
            colonne_ennemi += 1
        else:
            colonne_ennemi += 2
    elif colonne_ennemi == colonne_player: #Si l'ennemi et le joueur sont sur la meme colonne, l'ennemi avance vers le joueur. Si il est derriere l'objectif, il saute l'objectif en sautant de 2 places.
        if (ligne_player < ligne_ennemi) and (colonne_ennemi != colonne_objectif or ligne_ennemi != ligne_objectif + 1 ) :
            ligne_ennemi -= 1
        elif (ligne_player < ligne_ennemi) and (colonne_ennemi == colonne_objectif and ligne_ennemi == ligne_objectif + 1 ):
            ligne_ennemi -= 2
        elif (ligne_player > ligne_ennemi) and (colonne_ennemi != colonne_objectif or ligne_ennemi != ligne_objectif - 1 ):
            ligne_ennemi += 1
        else:
            ligne_ennemi += 2
    elif (colonne_player > colonne_ennemi) and (ligne_ennemi != ligne_objectif or colonne_ennemi!=colonne_objectif -1): #Si la colonne du joueur et celle de l'ennemi sont differentes, l'ennemi change de colonne, vers le joueur.
        colonne_ennemi+= 1
    elif (colonne_player > colonne_ennemi) and (ligne_ennemi == ligne_objectif or colonne_ennemi==colonne_objectif -1):#Si il y a l'objectif, l'ennemi change de ligne, en allant vers le joueur
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

#
def test_move_pos_ennemi():
    """
    Test if the position of the position positions.
    """
    assert move_pos_ennemi((1,1),(5,1),(3,4))== (4,1)
    assert move_pos_ennemi((1,1), (5,1), (4,1))== (3,1)
    assert move_pos_ennemi((2,1), (2,6), (1,5))== (2,5)
    assert move_pos_ennemi((2,1), (2,6), (2,5))== (2,4)
    assert move_pos_ennemi((1,1), (5,5), (3,3))== (5,4)
    assert move_pos_ennemi((1,1), (5,5), (5,4))== (4,5)
    assert move_pos_ennemi((7,0), (1,5), (2,4))== (1,4)
    assert move_pos_ennemi((7,0), (1,5), (1,4))== (2,5)
    assert move_pos_ennemi((2,3), (4,3), (3,3))== (2,3)

#Retourne la position du joueur, sous forme d'un couple
def get_position_player(grid):
    """
    Return the position of the player.
    """
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==(get_value_objectif(grid)/2): #la valeur du joueur est la moitie de celle de l'objectif
                return((i,j))

#Retourne la valeur de l'objectif
def get_value_objectif(grid):
    """
    Returns the value of a grid
    """
    return(max(get_value_in_grid(grid))) #l'objectif a la plus grande valeur de la grille

#Renvoie une liste contenant toutes les valeurs presente dans la grille
def get_value_in_grid(grid):
    """
    Return a list of grid numbers
    """
    l=[]
    for i in range(len(grid)):
        for j in range(len(grid)):
            l.append(grid[i][j])
    return(l)

#Renvoie la valeur du joueur
def get_value_player(grid):
    """
    Get the value of a player.
    """
    return (get_value_objectif(grid)/2)#la valeur du joueur est la moitie de celle de l'objectif

#Renvoie la direction entree par l'utilisateur
def read_player_command():
    """
    Reads a command.
    """
    command=raw_input("Entrez une direction ( up,down,right or left ): ")
    return command


#Renvoie la nouvelle position du joueur en finction de la commande entree par l'utilisateur
def move_pos_player(grid,pos_player,command):
    """
    Move the player to a player.
    """
    n=len(grid)
    if command=='up' or command=='z':
        return (pos_player[0]-1,pos_player[1])
    if command=='down' or command=='s':
        return (pos_player[0]+1,pos_player[1])
    if command=='right' or command=='d':
        return (pos_player[0], pos_player[1]+1)
    if command=='left' or command=='q':
        return (pos_player[0], pos_player[1]-1)

def move_pos_player_sans_murs(grid,pos_player,command):
    """
    Move a player to the player.
    """
    n=len(grid)
    if command=='up':
        if pos_player[0]==0:
            return (n-1,pos_player[1])
        return (pos_player[0]-1,pos_player[1])
    if command=='down':
        if pos_player[0]==n-1:
            return (0,pos_player[1])
        return (pos_player[0]+1,pos_player[1])
    if command=='right':
        if pos_player[1]==n-1:
            return(pos_player[0],0)
        return (pos_player[0], pos_player[1]+1)
    if command=='left':
        if pos_player[1]==0:
            return (pos_player[0], n-1)
        return(pos_player[0],pos_player[1]-1)


#
def test_get_value_in_grid():
    """
    Test if the value in x y x y w h w h w h w h w h w h w h w h w h w h w
    """
    assert get_value_in_grid([[0,2,2,2],[0,0,4,0],[0,8,16,2],[0,0,0,0]])==[0, 2, 2, 2, 0, 0, 4, 0, 0, 8, 16, 2, 0, 0, 0, 0]

#
def test_get_value_objectif():
    """
    Test if value is a 8 - bit value.
    """
    assert get_value_objectif([[0,0,0,0],[0,0,0,0],[0,8,16,0],[4,0,0,0]])==16

#Renvoie la position de l'objectif sous forme d'un couple
def get_position_objectif(grid):
    """
    Returns the position of the position of a grid
    """
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==get_value_objectif(grid):
                return((i,j))

#
def test_get_position_objectif():
    """
    Decode a bson object.
    """
    assert get_position_objectif([[0,0,0,0],[0,0,4,0],[0,8,16,0],[0,0,0,0]])==(2,2)

#Renvoie la position de l'ennemi sous forme d'un couple
def get_position_ennemi(grid) :
    """
    Return the position of the position of the grid.
    """
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==(get_value_objectif(grid)/4): #la valeur de l'ennemi est 4 fois plus petite que celle de l'objectif
                return((i,j))

def test_get_position_ennemi():
    """
    Test if the position of the dipoleemi.
    """
    assert get_position_ennemi([[0,0,0,0],[0,0,4,0],[0,8,16,0],[0,0,0,0]])==(1,2)

#Renvoie la position du joueur sous forme d'un couple
def get_position_player(grid):
    """
    Return the position of the player.
    """
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==(get_value_objectif(grid)/2):
                return((i,j))
#
def test_get_position_player():
    """
    !
    """
    assert get_position_player([[0,0,0,0],[0,0,4,0],[0,8,16,0],[0,0,0,0]])==(2,1)

def move_impossible(grid,pos_player,command):
    """
    Determine whether the player.
    """
    n=len(grid)
    if (command=='up' or command=='z') and pos_player[0]==0 :
        return True
    if (command=='down' or command=='s') and pos_player[0]==n-1 :
        return True
    if (command=='right' or command=='d') and pos_player[1]==n-1 :
        return True
    if (command=='left' or command=='q') and pos_player[1]==0 :
        return True

gameplay(8,512) 

