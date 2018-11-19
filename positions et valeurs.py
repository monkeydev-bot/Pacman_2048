def get_value_in_grid(grid):
    l=[]
    for i in range(len(grid)):
        for j in range(len(grid)):
            l.append(grid[i][j])
    return(l)
    
    
def test_get_value_in_grid():
    assert get_value_in_grid([[0,2,2,2],[0,0,4,0],[0,8,16,2],[0,0,0,0]])==[0, 2, 2, 2, 0, 0, 4, 0, 0, 8, 16, 2, 0, 0, 0, 0]
    

def get_value_objectif(grid):
    return(max(get_value_in_grid(grid)))
    
    
def test_get_value_objectif():
    assert get_value_objectif([[0,0,0,0],[0,0,0,0],[0,8,16,0],[4,0,0,0]])==16
    
def get_position_objectif(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==get_value_objectif(grid):
                return((i,j))
            
def test_get_position_objectif():
    assert get_position_objectif([[0,0,0,0],[0,0,4,0],[0,8,16,0],[0,0,0,0]])==(2,2)
    
def get_position_ennemy(grid) :
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==(get_value_objectif(grid)/4):
                return((i,j))
       
def test_get_position_ennemy():
    assert get_position_ennemy([[0,0,0,0],[0,0,4,0],[0,8,16,0],[0,0,0,0]])==(1,2)   

def get_position_player(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==(get_value_objectif(grid)/2):
                return((i,j))
                
def test_get_position_player():
    assert get_position_player([[0,0,0,0],[0,0,4,0],[0,8,16,0],[0,0,0,0]])==(2,1)
    