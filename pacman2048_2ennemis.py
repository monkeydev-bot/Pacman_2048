from random import *

#Lance le jeu dans son ensemble
def gameplay(n,value_max): #n: taille de la grille, value_max : score à attendre pour gagner
    grid=init_game(n)
    print(grid_to_string(grid))
    while get_value_player(grid)<value_max:
        pos_player=get_position_player(grid)
        pos_ennemi=get_position_ennemi(grid)
        pos_ennemi_2 = get_position_ennemi_2(grid)
        pos_objectif=get_position_objectif(grid)

        command=read_player_command()

        if move_impossible(grid,pos_player,command):
            print("Mouvement impossible")
            continue

        if move_pos_player(grid,pos_player,command)!=move_pos_ennemi(grid,pos_player,pos_ennemi,pos_ennemi_2,pos_objectif) and move_pos_player(grid,pos_player,command)!=pos_objectif and (move_pos_player(grid,pos_player,command),move_pos_ennemi(grid, pos_player,pos_ennemi,pos_ennemi_2,pos_objectif))!=(pos_ennemi,pos_player) and move_pos_player(grid,pos_player,command)!=move_pos_ennemi_2(grid, pos_player) and (move_pos_player(grid,pos_player,command),move_pos_ennemi_2(grid, pos_player))!=(pos_ennemi_2,pos_player):
            grid=move_player(grid,pos_player,command)
            grid=move_ennemi(grid,pos_player,pos_ennemi,pos_ennemi_2,pos_objectif)
            grid=move_ennemi_2(grid, pos_player)

            print(grid_to_string(grid))

        elif move_pos_player(grid,pos_player,command)==move_pos_ennemi(grid, pos_player,pos_ennemi,pos_ennemi_2,pos_objectif) or (move_pos_player(grid,pos_player,command),move_pos_ennemi(grid, pos_player,pos_ennemi,pos_ennemi_2,pos_objectif))==(pos_ennemi,pos_player) or move_pos_player(grid,pos_player,command)==move_pos_ennemi_2(grid,pos_player) or (move_pos_player(grid,pos_player,command),move_pos_ennemi_2(grid, pos_player))==(pos_ennemi_2,pos_player):
            print("Game Over")
            return ()
        else:
            grid=player_sur_objectif(grid,pos_player,pos_ennemi,pos_objectif)
            print(grid_to_string(grid))

    print("Victoire !")
    return()

#Lorsque le joueur atteint l'objectif, celui double de valeur et change de place aléatoirement. Le joueur double de valeur.L'ennemi double de valeur.
def player_sur_objectif(grid,pos_player,pos_ennemy,pos_objectif):
    i0,j0=pos_player
    grid[i0][j0]=0 #l'ancienne case du joueur est remplacée par un 0
    pos_player=pos_objectif
    i1,j1=get_new_position(grid)  #Nouvelle position de l'objectif, choisit aléatoirement
    new_abs_player,new_ord_player=pos_player
    value_player=grid[new_abs_player][new_ord_player] # On prend la valeur du joueur
    grid[i1][j1]=2*value_player #la valeur de l'objectif est doublée par rapport au joueur
    abs_ennemy,ord_ennemy=pos_ennemy
    grid[abs_ennemy][ord_ennemy]=value_player/2 #la valeur de l'ennemi est la moitié de celle du joueur
    return grid


#Change la place du joueur sur la grille suite à une commande. Testée.
def move_player(grid,pos_player,commande):
    old_abs_player,old_ord_player=pos_player
    new_abs_player,new_ord_player=move_pos_player(grid,pos_player,commande) #Nouvelle position du joueur
    grid[new_abs_player][new_ord_player]=grid[old_abs_player][old_ord_player] #Mise à jour de la nouvelle position
    grid[old_abs_player][old_ord_player]=0 #l'ancienne position vaut 0
    return grid

#Change la place de l'ennemi sur la grille. Testée.
def move_ennemi(grid,pos_player,pos_ennemy,pos_ennemi_2,pos_objectif):
    old_abs_ennemy, old_ord_ennemy=pos_ennemy
    new_abs_ennemy, new_ord_ennemy=move_pos_ennemi(grid,pos_player,pos_ennemy,pos_ennemi_2,pos_objectif) #Nouvelle position de l'ennemi
    grid[new_abs_ennemy][new_ord_ennemy]=grid[old_abs_ennemy][old_ord_ennemy] #Mise à jour de la nouvelle position
    grid[old_abs_ennemy][old_ord_ennemy]=0 #l'ancienne position vaut 0
    return grid

#Crée une grille de taille nxn remplie de 0. Testée.
def create_grid(n):
    grid=[]
    for i in range(n):
        s=[0 for j in range(n)]
        grid.append(s)
    return grid

#Ajoute un 2**m à la position i,j de grid. Testée.
def grid_add_new_tile_at_position(grid,i,j,m):
    grid[i][j]==2**m
    return grid

#Retourne la liste des couples de position vide. Testée.
def get_empty_tiles_positions(grid):
    n=len(grid)
    pos=[]
    for i in range(n):
        for j in range(n):
            if grid[i][j]==0:
                pos.append((i,j))
    return pos

#Renvoie une position aléatoire parmis les positions non occupées. Testée.
def get_new_position(grid):
    pos=get_empty_tiles_positions(grid)
    n=len(pos)
    a=randint(0,n-1)
    return pos[a]

#Crée la grille initiale avec le joueur en bas à gauche, l'ennemi placé aléatoirement et l'objectif placé aléatoirement. Testée.
def init_game(n):
    grid=create_grid(n)
    grid[n-1][0]=2 #positionnement du joueur
    i,j=get_new_position(grid)
    grid[i][j]=4 #positionnement de l'objectif
    s,t=get_new_position(grid)
    grid[s][t]=1 #positionnement de l'ennemi
    u,v = get_new_position(grid)
    grid[u][v] = "E" #positionnement de l'ennemi 2'
    return grid

#Fonction non utilisée. Renvoie la taille de la plus grande chaine de caractères présente dans la grille. Testée.
def long_value(grid):
    m=0
    for x in grid:
        for y in x:
            if len(str(y))>m:
                m=len(str(y))
    return m

#Fonction non utilisée.
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

#Retourne la nouvelle position de l'objectif. Non testée.
def add_objectif_at_grid(grid):
    i,j=get_new_position(grid)
    return (i,j)

#Affiche la grille de manière "propre" dans la console. Non testée.
def grid_to_string(grid):

    THEMES = {
        "0": {"name": "Default", 1: "1" ,0: " ", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256",
              512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192", "E": "E"},
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

#Retourne la nouvelle position de l'ennemi. L'ennemi suit le joueur. Testée.
def move_pos_ennemi(grid, position_player, position_ennemi,position_ennemi_2, position_objectif):
    ligne_ennemi, colonne_ennemi = position_ennemi
    ligne_ennemi_2, colonne_ennemi_2 = position_ennemi_2
    ligne_player, colonne_player = position_player
    ligne_objectif, colonne_objectif = position_objectif
    if ligne_ennemi == ligne_player : #Si l'ennemi et le joueur sont sur la même ligne, l'ennemi avance vers le joueur. Si il est derrière l'objectif, il saute l'objectif en sautant de 2 places.
        if (colonne_player < colonne_ennemi) and (ligne_ennemi != ligne_objectif or colonne_ennemi != colonne_objectif + 1 ) and (ligne_ennemi != ligne_ennemi_2 or colonne_ennemi != colonne_ennemi_2 + 1)  :
            colonne_ennemi -= 1
        elif (colonne_player < colonne_ennemi) and ((ligne_ennemi == ligne_objectif and colonne_ennemi == colonne_objectif + 1 ) or (ligne_ennemi == ligne_ennemi_2 and colonne_ennemi == colonne_ennemi_2 + 1 )) :
            colonne_ennemi -= 2
        elif (colonne_player > colonne_ennemi) and (ligne_ennemi != ligne_objectif or colonne_ennemi != colonne_objectif - 1 ) and (ligne_ennemi != ligne_ennemi_2 or colonne_ennemi != colonne_ennemi_2 - 1 ):
            colonne_ennemi += 1
        else:
            colonne_ennemi += 2
    elif colonne_ennemi == colonne_player: #Si l'ennemi et le joueur sont sur la même colonne, l'ennemi avance vers le joueur. Si il est derrière l'objectif, il saute l'objectif en sautant de 2 places.
        if (ligne_player < ligne_ennemi) and (colonne_ennemi != colonne_objectif or ligne_ennemi != ligne_objectif + 1 ) and (colonne_ennemi != colonne_ennemi_2 or ligne_ennemi != ligne_ennemi_2 + 1 ) :
            ligne_ennemi -= 1
        elif (ligne_player < ligne_ennemi) and ((colonne_ennemi == colonne_objectif and ligne_ennemi == ligne_objectif + 1 ) or (colonne_ennemi == colonne_ennemi_2 and ligne_ennemi == ligne_ennemi_2 + 1 )):
            ligne_ennemi -= 2
        elif (ligne_player > ligne_ennemi) and (colonne_ennemi != colonne_objectif or ligne_ennemi != ligne_objectif - 1 ) and (colonne_ennemi != colonne_ennemi_2 or ligne_ennemi != ligne_ennemi_2 - 1 ):
            ligne_ennemi += 1
        else:
            ligne_ennemi += 2
    elif colonne_ennemi != colonne_player :
        ligne_ennemi, colonne_ennemi = move_possible_ennemi(grid, position_player)

    return ligne_ennemi, colonne_ennemi

#Retourne la position du joueur, sous forme d'un couple.Testée.
def get_position_player(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==(get_value_objectif(grid)/2): #la valeur du joueur est la moitié de celle de l'objectif
                return((i,j))

#Retourne la valeur de l'objectif
def get_value_objectif(grid):
    return(max(get_value_in_grid(grid))) #l'objectif a la plus grande valeur de la grille

#Renvoie une liste contenant toutes les valeurs présente dans la grille
def get_value_in_grid(grid):
    l=[]
    for i in range(len(grid)):
        for j in range(len(grid)):
            l.append(grid[i][j])
    l.remove("E")
    return(l)

#Renvoie la valeur du joueur
def get_value_player(grid):
    return (get_value_objectif(grid)/2)#la valeur du joueur est la moitié de celle de l'objectif

#Renvoie la direction entrée par l'utilisateur
def read_player_command():
    command=input('Entrez une direction ( up,down,right or left ): ')
    return command

#Renvoie la nouvelle position du joueur en finction de la commande entrée par l'utilisateur
def move_pos_player(grid,pos_player,command):
    n=len(grid)
    if command=='up' or command=='z':
        return (pos_player[0]-1,pos_player[1])
    if command=='down' or command=='s':
        return (pos_player[0]+1,pos_player[1])
    if command=='right' or command=='d':
        return (pos_player[0], pos_player[1]+1)
    if command=='left' or command=='q':
        return (pos_player[0], pos_player[1]-1)

#Renvoie la position de l'objectif sous forme d'un couple
def get_position_objectif(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==get_value_objectif(grid):
                return((i,j))


#Renvoie la position de l'ennemi sous forme d'un couple
def get_position_ennemi(grid) :
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==(get_value_objectif(grid)/4): #la valeur de l'ennemi est 4 fois plus petite que celle de l'objectif
                return((i,j))

#Vérifie quand le joueur sort de la grille
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

#Renvoie la position de l'ennemi 2 sous forme d'un couple
def get_position_ennemi_2(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "E":
                return (i,j)

#Renvoie la nouvelle position de l'ennemi 2
def move_pos_ennemi_2(grid,pos_player):
    move_ennemi_2 =[]
    empty_tiles = get_empty_tiles_positions(grid)
    empty_tiles.append(pos_player)
    ligne_ennemi_2, colonne_ennemi_2 = get_position_ennemi_2(grid)
    if (ligne_ennemi_2,colonne_ennemi_2+1) in empty_tiles:
        move_ennemi_2.append((ligne_ennemi_2,colonne_ennemi_2 + 1))
    if (ligne_ennemi_2,colonne_ennemi_2 -1) in empty_tiles:
        move_ennemi_2.append((ligne_ennemi_2,colonne_ennemi_2 - 1))
    if (ligne_ennemi_2 + 1,colonne_ennemi_2+1) in empty_tiles:
        move_ennemi_2.append((ligne_ennemi_2 + 1,colonne_ennemi_2))
    if (ligne_ennemi_2 - 1,colonne_ennemi_2) in empty_tiles:
        move_ennemi_2.append((ligne_ennemi_2 - 1,colonne_ennemi_2))
    new_position = randint(0, len(move_ennemi_2)-1)
    return move_ennemi_2[new_position]

#Met à jour la grille de jeu après le mouvement de l'ennemi 2
def move_ennemi_2(grid, pos_player):
    ligne_ennemi_2, colonne_ennemi_2 = get_position_ennemi_2(grid)
    new_ligne_ennemi_2, new_colonne_ennemi_2 = move_pos_ennemi_2(grid, pos_player)
    grid[ligne_ennemi_2][colonne_ennemi_2] = 0
    grid[new_ligne_ennemi_2][new_colonne_ennemi_2] = "E"
    return grid

#Renvoie la liste des couples de positions possible des ennemis
def move_possible_ennemi(grid, pos_player):
    move_ennemi =[]
    empty_tiles = get_empty_tiles_positions(grid)
    empty_tiles.append(pos_player)
    ligne_ennemi, colonne_ennemi = get_position_ennemi(grid)
    if (ligne_ennemi,colonne_ennemi+1) in empty_tiles:
        move_ennemi.append((ligne_ennemi,colonne_ennemi + 1))
    if (ligne_ennemi,colonne_ennemi -1) in empty_tiles:
        move_ennemi.append((ligne_ennemi,colonne_ennemi - 1))
    if (ligne_ennemi + 1,colonne_ennemi+1) in empty_tiles:
        move_ennemi.append((ligne_ennemi + 1,colonne_ennemi))
    if (ligne_ennemi - 1,colonne_ennemi) in empty_tiles:
        move_ennemi.append((ligne_ennemi - 1,colonne_ennemi))
    new_position = randint(0, len(move_ennemi)-1)
    return move_ennemi[new_position]

gameplay(6,2048)
