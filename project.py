import random
import pygame


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
        show_seq(sequence)
        
        # player pick a colour
        answer = player_action(sequence) # returns wrong or right
        
        # if wrong ---> game over EXIT LOOP
        if answer == "wrong":
            break
        
        # if right, the loop continues ---> score += 1
        score += 1
        
        gameover()
        
        # --- DRAWING CODE ---
        # starting with total black
        
        screen.fill((0, 0, 0))
        
        # at the end we need updating he screen with all the drawing in this loop iteration
        pygame.display.flip()
        
    
def colour_seq(sequence):
    
    # select a random colour
    rnd_colour = random.choice(COLOURS)
    
    # append the colour to the sequence list
    sequence.append(rnd_colour)
    
    
    
def show_seq(sequence):
    
    # for loop to show the colour one by one for 1 sec
    for colour in sequence:
        print(colour)  
        time.sleep(1)
        os.system('clear')    
        
    
    
def player_choice():
    
    choice = None
    
    def release_key(key):
        
        nonlocal choice
        
        if key == Key.up:
            choice = 'up'
        elif key == Key.down:
            choice = 'down'
        elif key == Key.left:
            choice = 'left'
        elif key == Key.right:
            choice = 'right'
        
        try:
            if key.char == 'w':
                choice = 'up'
            elif key.char == 'a':
                choice = 'left'
            elif key.char == 's':
                choice = 'down'
            elif key.char == 'd':
                choice = 'right'
        except AttributeError:
            pass
    
    
    with Listener(on_release = release_key) as l:
        l.join()
        
    return choice
    
    
def player_action(sequence):
    
    # player gets asked "What's the sequence?"
    print("What's the sequence? [Use WASD or arrows]")
    
    for colour in sequence:
        if colour != player_choice():
            return "wrong"
         
         
def gameover():
    
    # We show the score and ask if the player wants to play another game
    print("Your score is", score)
    new_game = input("Do you want to play another game? Y/n").lower()
    
    # Here it could be interesting to apply restrictions about what can be replied (and apply some of the lessons we studied)
    if new_game == "y":
        main()
        
    elif new_game == "n":
        print("OK, see you next time!")
        exit()   # can we print INSIDE exit function?? can't remember
        
        

        
if __name__ == "__main__":
    main()