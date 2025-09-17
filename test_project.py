import pygame
from project import check_player_input, get_choice_from_key, colour_seq, COLOURS

def test_check_player_input():
    sequence = ['up', 'down', 'left']
    
    # test a correct choice
    assert check_player_input(sequence, 'up', 0) == True
    
    # test an incorrect choice
    assert check_player_input(sequence, 'right', 1) == False
    
    # test a choice that is correct but at the wrong time
    assert check_player_input(sequence, 'up', 2) == False
    
    # test an index that is out of bounds
    assert check_player_input(sequence, 'up', 3) == False
    
    
def test_get_choice_from_key():
    
    # test the primary 'WASD' keys
    assert get_choice_from_key(pygame.K_w) == 'up'
    assert get_choice_from_key(pygame.K_a) == 'left'
    assert get_choice_from_key(pygame.K_s) == 'down'
    assert get_choice_from_key(pygame.K_d) == 'right'
    
    # Test the alternate arrow keys
    assert get_choice_from_key(pygame.K_UP) == 'up'
    assert get_choice_from_key(pygame.K_LEFT) == 'left'
    assert get_choice_from_key(pygame.K_DOWN) == 'down'
    assert get_choice_from_key(pygame.K_RIGHT) == 'right'
    
    # Test a key that shouldn't return anything
    assert get_choice_from_key(pygame.K_p) is None
    
    
def test_colour_seq():
    
    # we imported the COLOURS list at the top of the file
    sequence = []
    
    # after calling the function once, the list should have 1 item
    colour_seq(sequence)
    assert len(sequence) == 1
    
    # and that item should be one of the valid colours
    assert sequence[0] in COLOURS
    
    # let's call it again to be sure
    colour_seq(sequence)
    assert len(sequence) == 2
    assert sequence[1] in COLOURS