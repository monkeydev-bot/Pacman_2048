def move_pos_ennemi(position_player, position_ennemi, position_objectif):
    ligne_ennemi, colonne_ennemi = position_ennemi
    ligne_player, colonne_player = position_player
    ligne_objectif, colonne_objectif = position_objectif
    if ligne_ennemi == ligne_player :
        if (colonne_player < colonne_ennemi) and (ligne_ennemi != ligne_objectif or colonne_ennemi != colonne_objectif + 1 ) :
            colonne_ennemi -= 1
        elif (colonne_player < colonne_ennemi) and (ligne_ennemi == ligne_objectif and colonne_ennemi == colonne_objectif + 1 ):
            colonne_ennemi -= 2
        elif (colonne_player > colonne_ennemi) and (ligne_ennemi != ligne_objectif or colonne_ennemi != colonne_objectif - 1 ):
            colonne_ennemi += 1
        else:
            colonne_ennemi += 2
    elif colonne_ennemi == colonne_player:
        if (ligne_player < ligne_ennemi) and (colonne_ennemi != colonne_objectif or ligne_ennemi != ligne_objectif + 1 ) :
            ligne_ennemi -= 1
        elif (ligne_player < ligne_ennemi) and (colonne_ennemi == colonne_objectif and ligne_ennemi == ligne_objectif + 1 ):
            ligne_ennemi -= 2
        elif (ligne_player > ligne_ennemi) and (colonne_ennemi != colonne_objectif or ligne_ennemi != ligne_objectif - 1 ):
            ligne_ennemi += 1
        else:
            ligne_ennemi += 2
    elif (colonne_player > colonne_ennemi) and (ligne_ennemi != ligne_objectif or colonne_ennemi!=colonne_objectif -1):
        colonne_ennemi+= 1
    elif (colonne_player > colonne_ennemi) and (ligne_ennemi == ligne_objectif or colonne_ennemi==colonne_objectif -1):
        if (ligne_player > ligne_ennemi):
            ligne_ennemi+=1
        else:
            ligne_ennemi-= 1
    elif (colonne_player < colonne_ennemi) and (ligne_ennemi != ligne_objectif or colonne_ennemi!=colonne_objectif + 1):
        colonne_ennemi -= 1
    elif (colonne_player < colonne_ennemi) and (ligne_ennemi == ligne_objectif and colonne_ennemi==colonne_objectif + 1):
        if (ligne_player > ligne_ennemi):
            ligne_ennemi += 1
        else :
            ligne_ennemi -= 1

    return ligne_ennemi, colonne_ennemi


def test_move_pos_ennemi():
    assert move_pos_ennemi((1,1),(5,1),(3,4))== (4,1)
    assert move_pos_ennemi((1,1), (5,1), (4,1))== (3,1)
    assert move_pos_ennemi((2,1), (2,6), (1,5))== (2,5)
    assert move_pos_ennemi((2,1), (2,6), (2,5))== (2,4)
    assert move_pos_ennemi((1,1), (5,5), (3,3))== (5,4)
    assert move_pos_ennemi((1,1), (5,5), (5,4))== (4,5)
    assert move_pos_ennemi((7,0), (1,5), (2,4))== (1,4)
    assert move_pos_ennemi((7,0), (1,5), (1,4))== (2,5)
    assert move_pos_ennemi((2,3), (4,3), (3,3))== (2,3)

test_move_pos_ennemi()
