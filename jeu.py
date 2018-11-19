import random

def creategrid(n):
    grid=[]
    for i in range(n):
        grid.append([0]*n)
    return grid

def initjoueur(grid):
    n=len(grid)
    grid[n-1][n-1]=2

    
def get_new_spawn_position(grid):
    n=len(grid)
    x=random.randint(0,n-1)
    y=random.randint(0,n-1)
    return (x,y)
def grid_to_string_with_size(grid,n):
    
    THEMES = {
        "0": {"name": "Default", 0: " ", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256",
              512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"},
        }
   
    
    size = len(grid)
    string = """"""
    entre_lignes=" "+("="*n+" ")*size + "\n"
    string+=entre_lignes
    for i in range(size):
        string += "|"
        for j in range(size):
            ch=THEMES["0"][grid[i][j]]
            while len(ch)<n:
                ch+=" "
            string+=ch
            string+="|"
        string+="\n"
        string+=entre_lignes
    print(string)
    return(string)
