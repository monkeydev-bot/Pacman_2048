
#Retourne la nouvelle position de l'ennemi. L'ennemi suit le joueur.
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

#Renvoie une liste contenant toutes les valeurs présente dans la grille
def get_value_in_grid(grid):
    l=[]
    for i in range(len(grid)):
        for j in range(len(grid)):
            l.append(grid[i][j])
    return(l)

#Retourne la valeur de l'objectif
def get_value_objectif(grid):
    return(max(get_value_in_grid(grid))) #l'objectif a la plus grande valeur de la grille

#Renvoie la valeur du joueur
def get_value_player(grid):
    return (get_value_objectif(grid)/2)#la valeur du joueur est la moitié de celle de l'objectif


def get_position_player(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==(get_value_objectif(grid)/2): #la valeur du joueur est la moitié de celle de l'objectif
                return((i,j))

#Renvoie la position de l'objectif sous forme d'un couple
def get_position_objectif(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==get_value_objectif(grid):
                return((i,j)

                # Renvoie la position de l'ennemi sous forme d'un couple

def get_position_ennemi(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == (get_value_objectif(
                    grid) / 4):  # la valeur de l'ennemi est 4 fois plus petite que celle de l'objectif
                return ((i, j))

