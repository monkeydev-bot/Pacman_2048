from random import randint

#Lance le jeu dans son ensemble
def gameplay(n,value_max): #n: taille de la grille, value_max : score à attendre pour gagner
    grid=init_game(n)
    print(grid_to_string(grid))
    while get_value_player(grid)<value_max:
        pos_player=get_position_player(grid)
        pos_ennemi=get_position_ennemi(grid)
        pos_objectif=get_position_objectif(grid)
        command=read_player_command()

        if move_impossible(grid,pos_player,command):
            print("Mouvement impossible")
            continue

        if move_pos_player(grid,pos_player,command)!=move_pos_ennemi(pos_player,pos_ennemi,pos_objectif) and move_pos_player(grid,pos_player,command)!=pos_objectif and (move_pos_player(grid,pos_player,command),move_pos_ennemi(pos_player,pos_ennemi,pos_objectif))!=(pos_ennemi,pos_player):
            grid=move_player(grid,pos_player,command)
            grid=move_ennemi(grid,pos_player,pos_ennemi,pos_objectif)

            print(grid_to_string(grid))

        elif move_pos_player(grid,pos_player,command)==move_pos_ennemi(pos_player,pos_ennemi,pos_objectif) or (move_pos_player(grid,pos_player,command),move_pos_ennemi(pos_player,pos_ennemi,pos_objectif))==(pos_ennemi,pos_player):
            print("Game Over")
            return ()
        else:
            grid=player_sur_objectif(grid,pos_player,pos_ennemi,pos_objectif)
            print(grid_to_string(grid))

    print("Victoire !")
    return()



