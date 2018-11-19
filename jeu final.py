

def gameplay(n,value_max):
    grid=init_game(n)
    print(grid_to_string(grid))
    while get_value_player(grid)<value_max:
        pos_player=get_position_player(grid)
        pos_ennemi=get_position_ennemy(grid)
        pos_objectif=get_position_objectif(grid)
        command=read_player_command()
        while move_pos_player(pos_player,command)!=move_pos_ennemi(pos_player,pos_objectif,pos_ennemi) and move_pos_player(pos_player,command)!=pos_objectif and move_pos_player(pos_player,command),move_pos_ennemi(pos_player,pos_objectif,pos_ennemi)!=pos_ennemi,pos_player:
            grid=move_player(grid,pos_player,command)
            grid=move_ennemi(grid,pos_player,pos_objectif,pos_ennemi)
            
            print(grid_to_string(grid))
            
        if move_pos_player(pos_player,command)==move_pos_ennemi(pos_player,pos_objectif,pos_ennemi) or move_pos_player(pos_player,command),move_pos_ennemi(pos_player,pos_objectif,pos_ennemi)==pos_ennemi,pos_player:
            return('game over')
            
        else:
            grid=player_sur_objectif(grid,pos_player,pos_ennemi,pos_objectif)
            print(grid)
            
    return('Gagné !')
        
        
            