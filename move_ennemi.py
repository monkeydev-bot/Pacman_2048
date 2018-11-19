import random

def new_position_ennemi():
    ligne_ennemi, colonne_ennemi = get_position_ennemi()
    ligne_player, colonne_player = get_position_player()
    if ligne_ennemi == ligne_player :
        if colonne_player < colonne_ennemi :
            colonne_ennemi -= 1
        else:
            colonne_ennemi += 1
    elif colonne_ennemi == colonne_player:
        if ligne_player < ligne_ennemi :
            ligne_ennemi += 1
        else :
            ligne_ennemi -= 1
    else:
        if ligne_player < ligne_ennemi :
            ligne_ennemi -= 1
        else:
            ligne_ennemi += 1

    return ligne_ennemi, colonne_ennemi

def move_ennemi(grid):
    ligne_ennemi, colonne_ennemi = get_position_ennemi()
    new_ligne_ennemi, new_colonne_ennemi = new_position_ennemi()
    grid[ligne_ennemi][colonne_ennemi] = 0
    grid[new_ligne_ennemi][new_colonne_ennemi] = int(value_objectif(grid)/4)

def test_new_position_ennemi():

    assert 
