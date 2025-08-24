import random
import time
import os


COLOURS = ['up', 'right', 'down', 'left']

def main():
    
    score = 0
    sequence = []
    
    
    while True:
        
        # computer adds a colour to the sequence        
        colour_seq(sequence)
        
        # computer shows the sequence
        show_seq(sequence)
        
        # player pick a colour
        answer = player_action() # returns wrong or right
        
        # if wrong ---> game over EXIT LOOP
        if answer == wrong:
            break
        
        # if right, the loop continues ---> score += 1
        score += 1
        
    gameover()
        
    
def colour_seq(sequence):
    
    # select a random colour
    rnd_colour = random.choice(COLOURS)
    
    # append the colour to the sequence list
    sequence.append(rnd_colour)
    
    
    
def show_seq(sequence):
    
    # for loop to show the colour one by one for 0.5 secs at 1 sec interval
    for colour in sequence:
        print(colour)  
        time.sleep(1)
        os.system('clear')    
    
    
def player_action():
    
    # player gets asked "What's the sequence?"
    print("What's the sequence? [Use WASD or arrows]")
    
    
    # for loop ? to cycle through sequence elements and at each one we wait for input from player
    # if answer is right loop moves on
    # if answer is wrong we return "wrong"
    # if loop ends we return right
         
         
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