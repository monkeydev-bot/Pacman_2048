#Crée une grille de taille nxn remplie de 0
def create_grid(n):
    grid=[]
    for i in range(n):
        s=[0 for j in range(n)]
        grid.append(s)
    return grid

#Ajoute un 2**m à la position i,j de grid
def grid_add_new_tile_at_position(grid,i,j,m):
    grid[i][j]==2**m
    return grid

#Retourne la liste des couples de position vide
def get_empty_tiles_positions(grid):
    n=len(grid)
    pos=[]
    for i in range(n):
        for j in range(n):
            if grid[i][j]==0:
                pos.append((i,j))
    return pos

#Renvoie une position aléatoire parmis les positions non occupées
def get_new_position(grid):
    pos=get_empty_tiles_positions(grid)
    n=len(pos)
    a=randint(0,n-1)
    return pos[a]

#Crée la grille initiale avec le joueur en bas à gauche, l'ennemi placé aléatoirement et l'objectif placé aléatoirement
def init_game(n):
    grid=create_grid(n)
    grid[n-1][0]=2 #positionnement du joueur
    i,j=get_new_position(grid)
    grid[i][j]=4 #positionnement de l'objectif
    s,t=get_new_position(grid)
    grid[s][t]=1 #positionnement de l'ennemi
    return grid