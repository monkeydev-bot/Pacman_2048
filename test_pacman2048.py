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
    assert grid(4) ==[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert grid(6) == [[0 for i in range(6)] for j in range(6)]

def test_grid_add_new_tile_at_position():
    assert grid_add_new_tile_at_position([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 1,3,4) == [[0, 0, 0, 0, 0], [0, 0, 0, 16, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

def test_get_empty_tiles_positions():
    assert get_empty_tiles_positions([[0,2],[3,7]]) == [(0,0)]
    assert get_empty_tiles_positions([[0,2],[0,0]]) == [(0,0), (1,0),(1,1)]

def test_get_new_position():
    assert get_new_position([[0,2,6],[5,0,7],[2,2,2]]) in [(0,0),(1,1)]
