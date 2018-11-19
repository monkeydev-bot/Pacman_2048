def get_position_player(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==(get_value_objectif(grid)/2):
                return((i,j))

def get_value_objectif(grid):
    return(max(get_value_in_grid(grid)))
    
def get_value_in_grid(grid):
    l=[]
    for i in range(len(grid)):
        for j in range(len(grid)):
            l.append(grid[i][j])
    return(l)
    
    
def get_value_player(grid):
    return (get_value_objectif(grid)/2)
    

def read_player_command():
    command=input('Entrez une direction ( up,down,right or left ): ')
    return command


def move_pos_player(grid,command):
    n=len(grid)
    pos=get_position_player(grid)
    
    if command=='up':
        if pos[0]==0:
            return ('Mouvement impossible' )
        else:
            
            return (pos[0]-1,pos[1])
    elif command=='down':
        if pos[0]==n-1:
            return ('Mouvement impossible' )
        else:
            
            return (pos[0]+1,pos[1])
    elif command=='right':
        if pos[1]==n-1:
            return ('Mouvement impossible' )
        else:
            return (pos[0], pos[1]+1)
    elif command=='left':
        if pos[1]==0:
            return ('Mouvement impossible' )
        else:
             return (pos[0], pos[1]-1)

def test_move_pos_player():
    assert move_pos_player([[0,0,0,0],[0,2,0,0],[0,0,1,0],[0,0,4,0]],'up')==(0,1)
    assert move_pos_player([[0,0,0,0],[0,0,0,0],[0,4,1,0],[0,0,2,0]], 'down')=='Mouvement impossible'
    
           

        
        
            
        
    