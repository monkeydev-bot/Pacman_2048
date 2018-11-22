
#Affiche la grille de manière "propre" dans la console
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