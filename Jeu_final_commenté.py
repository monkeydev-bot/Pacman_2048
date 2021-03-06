from random import randint

#Lance le jeu dans son ensemble
def gameplay(n,value_max): #n: taille de la grille, value_max : score à attendre pour gagner
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
def move_ennemi(grid,pos_player,pos_ennemy,pos_objectif):
    old_abs_ennemy, old_ord_ennemy=pos_ennemy
    new_abs_ennemy, new_ord_ennemy=move_pos_ennemi(pos_player,pos_ennemy,pos_objectif) #Nouvelle position de l'ennemi
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

#Affiche la grille de manière "propre" dans la console. Testée.
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

#Retourne la nouvelle position de l'ennemi. L'ennemi suit le joueur. Testée.
def move_pos_ennemi(position_player, position_ennemi, position_objectif):
    ligne_ennemi, colonne_ennemi = position_ennemi
    ligne_player, colonne_player = position_player
    ligne_objectif, colonne_objectif = position_objectif
    if ligne_ennemi == ligne_player : #Si l'ennemi et le joueur sont sur la même ligne, l'ennemi avance vers le joueur. Si il est derrière l'objectif, il saute l'objectif en sautant de 2 places.
        if (colonne_player < colonne_ennemi) and (ligne_ennemi != ligne_objectif or colonne_ennemi != colonne_objectif + 1 ) :
            colonne_ennemi -= 1
        elif (colonne_player < colonne_ennemi) and (ligne_ennemi == ligne_objectif and colonne_ennemi == colonne_objectif + 1 ):
            colonne_ennemi -= 2
        elif (colonne_player > colonne_ennemi) and (ligne_ennemi != ligne_objectif or colonne_ennemi != colonne_objectif - 1 ):
            colonne_ennemi += 1
        else:
            colonne_ennemi += 2
    elif colonne_ennemi == colonne_player: #Si l'ennemi et le joueur sont sur la même colonne, l'ennemi avance vers le joueur. Si il est derrière l'objectif, il saute l'objectif en sautant de 2 places.
        if (ligne_player < ligne_ennemi) and (colonne_ennemi != colonne_objectif or ligne_ennemi != ligne_objectif + 1 ) :
            ligne_ennemi -= 1
        elif (ligne_player < ligne_ennemi) and (colonne_ennemi == colonne_objectif and ligne_ennemi == ligne_objectif + 1 ):
            ligne_ennemi -= 2
        elif (ligne_player > ligne_ennemi) and (colonne_ennemi != colonne_objectif or ligne_ennemi != ligne_objectif - 1 ):
            ligne_ennemi += 1
        else:
            ligne_ennemi += 2
    elif (colonne_player > colonne_ennemi) and (ligne_ennemi != ligne_objectif or colonne_ennemi!=colonne_objectif -1): #Si la colonne du joueur et celle de l'ennemi sont différentes, l'ennemi change de colonne, vers le joueur.
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

#
def test_get_value_in_grid():
    assert get_value_in_grid([[0,2,2,2],[0,0,4,0],[0,8,16,2],[0,0,0,0]])==[0, 2, 2, 2, 0, 0, 4, 0, 0, 8, 16, 2, 0, 0, 0, 0]

#
def test_get_value_objectif():
    assert get_value_objectif([[0,0,0,0],[0,0,0,0],[0,8,16,0],[4,0,0,0]])==16

#Renvoie la position de l'objectif sous forme d'un couple
def get_position_objectif(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==get_value_objectif(grid):
                return((i,j))

#
def test_get_position_objectif():
    assert get_position_objectif([[0,0,0,0],[0,0,4,0],[0,8,16,0],[0,0,0,0]])==(2,2)

#Renvoie la position de l'ennemi sous forme d'un couple
def get_position_ennemi(grid) :
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==(get_value_objectif(grid)/4): #la valeur de l'ennemi est 4 fois plus petite que celle de l'objectif
                return((i,j))

def test_get_position_ennemi():
    assert get_position_ennemi([[0,0,0,0],[0,0,4,0],[0,8,16,0],[0,0,0,0]])==(1,2)

#Renvoie la position du joueur sous forme d'un couple
def get_position_player(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==(get_value_objectif(grid)/2):
                return((i,j))
#
def test_get_position_player():
    assert get_position_player([[0,0,0,0],[0,0,4,0],[0,8,16,0],[0,0,0,0]])==(2,1)

#Testée.
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


