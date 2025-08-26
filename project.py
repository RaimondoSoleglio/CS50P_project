import random
import pygame

# define 4 colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# off status of colours
RED_OFF = (100, 0, 0)
GREEN_OFF = (0, 100, 0)
BLUE_OFF = (0, 0, 100)
YELLOW_OFF = (100, 100, 0)

# define rects for 4 buttons (left, top, w, h)
top = pygame.Rect(220, 40, 160, 160)
left = pygame.Rect(40, 220, 160, 160)
bottom = pygame.Rect(220, 400, 160, 160)
right = pygame.Rect(400, 220, 160, 160)

rects = {'up': top, 'left': left, 'down': bottom, 'right': right}

COLOURS = ['up', 'left', 'down', 'right']

def main():
    
    # initialising pygame
    pygame.init()
    
    # we need a screen
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    # creating the window
    pygame.display.set_caption("CS50P Simon Game - My Final Project")
    
    score = 0
    sequence = []
    
    # game states
    state = 'COMPUTER TURN'
    player_turn_index = 0
    
    # a variable to control the game loop
    running = True
    
    while running:
        
        # checking for user input (event loop)
        for event in pygame.event.get():
            # what happens when user clicks CLOSE button
            if event.type == pygame.QUIT:
                running = False
                
            if state == 'PLAYER TURN':
                
                # keyboard input
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        print("Player chose UP")
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        print("Player chose LEFT")
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        print("Player chose DOWN")
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        print("Player chose RIGHT")
                        
                # mouse input
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if top.collidepoint(event.pos):
                        print("Player chose UP")
                    elif left.collidepoint(event.pos):
                        print("Player chose LEFT")
                    elif bottom.collidepoint(event.pos):
                        print("Player chose DOWN")
                    elif right.collidepoint(event.pos):
                        print("Player chose RIGHT")
                    
                    
        # game logic - states
        if state == 'COMPUTER TURN':
            
            # computer adds a colour to the sequence        
            colour_seq(sequence)
        
            # computer shows the sequence
            show_seq(sequence, screen)
            
            # change state
            state = 'PLAYER TURN'
            
            # reset the player's progress
        
        
        

        # --- DRAWING CODE ---
        
        # starting with total black
        screen.fill((0, 0, 0))
        
        # at the end we need updating he screen with all the drawing in this loop iteration
        pygame.display.flip()
        
        
    # we are here once the 'while' loop is finished
    print("Game over! Your score was:", score)
    pygame.quit()
        
    
def colour_seq(sequence):
    
    # select a random colour
    rnd_colour = random.choice(COLOURS)
    
    # append the colour to the sequence list
    sequence.append(rnd_colour)
    
    
    
def show_seq(sequence, screen):
    
    # mapping COLOURS with rects and properties
    rect_map = {
        'up': {'rect': top, 'on': RED, 'off': RED_OFF},
        'left': {'rect': left, 'on': GREEN, 'off': GREEN_OFF},
        'down': {'rect': bottom, 'on': BLUE, 'off': BLUE_OFF},
        'right': {'rect': right, 'on': YELLOW, 'off': YELLOW_OFF},
    }    
    
    # loop needed for pygame to draw each frame of the seq
    # we hold the properties for the button to lit
    for colour in sequence:
        rect_bright = rect_map[colour]
            
        # then we cycle through all 4 buttons to make them dark, using this model:
        # pygame.draw.rect(screen, RED, top, border_radius = 30)
        for rect_dark in rect_map.values():
            pygame.draw.rect(screen, rect_dark['off'], rect_dark['rect'], border_radius = 30)
            
        # then we "draw" bright on top
        pygame.draw.rect(screen, rect_bright['on'], rect_bright['rect'], border_radius = 30)
        
        # draw the frame
        pygame.display.flip()
        pygame.time.wait(500)   # wait
        
        # light off again
        for rect_dark in rect_map.values():
            pygame.draw.rect(screen, rect_dark['off'], rect_dark['rect'], border_radius = 30)
            
        pygame.display.flip()
        pygame.time.wait(250)
    
# the following two functions are helpers to take care of player's input
    
def get_choice_from_pos(pos, rects):
    
    # position and rects dictionary - returns the clicked rect or None
    for choice, rect in rects.items():
        if rect.collidepoint(pos):
            return choice
    
    return None

def get_choice_from_key(key):
    
    # returns the choice if a button is pressed
    if key == pygame.K_w or key == pygame.K_UP:
        return 'up'
    elif key == pygame.K_a or key == pygame.K_LEFT:
        return 'left'
    elif key == pygame.K_s or key == pygame.K_DOWN:
        return 'down'
    elif key == pygame.K_d or key == pygame.K_RIGHT:
        return 'right'

        
if __name__ == "__main__":
    main()