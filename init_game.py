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

