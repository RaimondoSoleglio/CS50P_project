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
    
    # a variable to control the game loop
    running = True
    
    while running:
        
        # checking for user input
        for event in pygame.event.get():
            # what happens when user clicks CLOSE button
            if event.type == pygame.QUIT:
                running = False
                    
        # computer adds a colour to the sequence        
        colour_seq(sequence)
        
        # computer shows the sequence
        show_seq(sequence, screen)
        
        # player pick a colour
        # answer = player_action(sequence) # returns wrong or right
        
        # if wrong ---> game over EXIT LOOP
        # if answer == "wrong":
        #     break
        
        # if right, the loop continues ---> score += 1
        # score += 1
        

        # --- DRAWING CODE ---
        
        # starting with total black
        screen.fill((0, 0, 0))
        
        # rects
        pygame.draw.rect(screen, RED, top, border_radius = 30)
        pygame.draw.rect(screen, GREEN, left, border_radius = 30)
        pygame.draw.rect(screen, BLUE, bottom, border_radius = 30)
        pygame.draw.rect(screen, YELLOW, right, border_radius = 30)
        
        
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
    
    
    
def show_seq(sequence):
    
    # mapping COLOURS with rects and properties
    rect_map = {
        'up': {'rect': top, 'on': RED, 'off': RED_OFF},
        'left': {'rect': left, 'on': GREEN, 'off': GREEN_OFF},
        'down': {'rect': bottom, 'on': BLUE, 'off': BLUE_OFF},
        'right': {'rect': right, 'on': YELLOW, 'off': YELLOW_OFF},
    }        
    
    
    
# def player_choice():
    
#     choice = None
    
#     def release_key(key):
        
#         nonlocal choice
        
#         if key == Key.up:
#             choice = 'up'
#         elif key == Key.down:
#             choice = 'down'
#         elif key == Key.left:
#             choice = 'left'
#         elif key == Key.right:
#             choice = 'right'
        
#         try:
#             if key.char == 'w':
#                 choice = 'up'
#             elif key.char == 'a':
#                 choice = 'left'
#             elif key.char == 's':
#                 choice = 'down'
#             elif key.char == 'd':
#                 choice = 'right'
#         except AttributeError:
#             pass
    
        
#     return choice
    
    
# def player_action(sequence):
    
#     # player gets asked "What's the sequence?"
#     print("What's the sequence? [Use WASD or arrows]")
    
#     for colour in sequence:
#         if colour != player_choice():
#             return "wrong"
         

        
if __name__ == "__main__":
    main()