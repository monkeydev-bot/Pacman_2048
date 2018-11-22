
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




#Change la place du joueur sur la grille suite à une commande
def move_player(grid,pos_player,commande):
    old_abs_player,old_ord_player=pos_player
    new_abs_player,new_ord_player=move_pos_player(grid,pos_player,commande) #Nouvelle position du joueur
    grid[new_abs_player][new_ord_player]=grid[old_abs_player][old_ord_player] #Mise à jour de la nouvelle position
    grid[old_abs_player][old_ord_player]=0 #l'ancienne position vaut 0
    return grid

#Change la place de l'ennemi sur la grille
def move_ennemi(grid,pos_player,pos_ennemy,pos_objectif):
    old_abs_ennemy, old_ord_ennemy=pos_ennemy
    new_abs_ennemy, new_ord_ennemy=move_pos_ennemi(pos_player,pos_ennemy,pos_objectif) #Nouvelle position de l'ennemi
    grid[new_abs_ennemy][new_ord_ennemy]=grid[old_abs_ennemy][old_ord_ennemy] #Mise à jour de la nouvelle position
    grid[old_abs_ennemy][old_ord_ennemy]=0 #l'ancienne position vaut 0
    return grid