from Pacman2048.Jeu_final_commenté import *



def test_move_player():
    assert move_player([[0, 0, 0, 0, 0], [0, 0, 0, 8, 0], [0, 4, 0, 0, 0], [0, 0, 0, 2, 0], [0, 0, 0, 0, 0]], (2,1), "up") == [[0, 0, 0, 0, 0], [0, 4, 0, 8, 0], [0, 0, 0, 0, 0], [0, 0, 0, 2, 0], [0, 0, 0, 0, 0]]
    assert move_player([[0, 0, 0, 0, 0], [0, 0, 0, 8, 0], [0, 4, 0, 0, 0], [0, 0, 0, 2, 0], [0, 0, 0, 0, 0]], (2,1), "down") == [[0, 0, 0, 0, 0], [0, 0, 0, 8, 0], [0, 0, 0, 0, 0], [0, 4, 0, 2, 0], [0, 0, 0, 0, 0]]
    assert move_player([[0, 0, 0, 0, 0], [0, 0, 0, 8, 0], [0, 4, 0, 0, 0], [0, 0, 0, 2, 0], [0, 0, 0, 0, 0]], (2,1), "right") == [[0, 0, 0, 0, 0], [0, 0, 0, 8, 0], [0, 0, 4, 0, 0], [0, 0, 0, 2, 0], [0, 0, 0, 0, 0]]
    assert move_player([[0, 0, 0, 0, 0], [0, 0, 0, 8, 0], [0, 4, 0, 0, 0], [0, 0, 0, 2, 0], [0, 0, 0, 0, 0]], (2,1), "left") == [[0, 0, 0, 0, 0], [0, 0, 0, 8, 0], [4, 0, 0, 0, 0], [0, 0, 0, 2, 0], [0, 0, 0, 0, 0]]

def test_move_ennemi():
    assert move_ennemi([[0, 0, 0, 0, 0], [0, 0, 0, 8, 0], [0, 4, 0, 0, 0], [0, 0, 0, 2, 0], [0, 0, 0, 0, 0]],(2,1),(3,3), (1,3)) == [[0, 0, 0, 0, 0], [0, 0, 0, 8, 0], [0, 4, 0, 0, 0], [0, 0, 2, 0, 0], [0, 0, 0, 0, 0]]
    assert move_ennemi([[0, 0, 0, 0, 0], [0, 0, 0, 8, 0], [0, 0, 0, 0, 0], [0, 4, 0, 2, 0], [0, 0, 0, 0, 0]],(3,1), (3,3),(1,3)) == [[0, 0, 0, 0, 0], [0, 0, 0, 8, 0], [0, 0, 0, 0, 0], [0, 4, 2, 0, 0], [0, 0, 0, 0, 0]]

def test_create_grid():
    assert create_grid(4) ==[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert create_grid(6) == [[0 for i in range(6)] for j in range(6)]

def test_grid_add_new_tile_at_position():
    assert grid_add_new_tile_at_position([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 1,3,4) == [[0, 0, 0, 0, 0], [0, 0, 0, 16, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

def test_get_empty_tiles_positions():
    assert get_empty_tiles_positions([[0,2],[3,7]]) == [(0,0)]
    assert get_empty_tiles_positions([[0,2],[0,0]]) == [(0,0), (1,0),(1,1)]

def test_get_new_position():
    assert get_new_position([[0,2,6],[5,0,7],[2,2,2]]) in [(0,0),(1,1)]

def test_init_game():
    assert init_game(4)[3][0] == 2
    assert len(init_game(10))== 10

def test_long_value():
    assert long_value([[2,56],[4,2067]])== 4
    assert long_value([[3,45],[2,0]]) == 2

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

def test_get_position_player():
    assert get_position_player([[0, 2, 0, 0, 0], [0, 0, 4, 0, 0], [0, 0, 0, 8, 0], [0, 0, 0, 0, 0]]) == (1,2)
