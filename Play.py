#Renvoie la direction entrée par l'utilisateur
def read_player_command():
    command=input("Entrez une direction ( up,down,right or left ): ")
    return command

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

