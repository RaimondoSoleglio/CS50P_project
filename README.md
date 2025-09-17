# CS50P Final Project - Simon Game

### by Roberto Sommella

A documentation of my final project development process for Harvard's CS50P Introduction to Programming with Python course.

### VIDEO LINK:

#### Description:

The Simon Game is a memory skill game where players must repeat a sequence of colours/sounds that gets progressively longer and more complex. The game starts with a intro title and a **START** button. There a small I in the top left corner to read instructions and credits. 

The game starts with the computer lightening up one of four colour, with a sound. Like in a “Simon says” game, the player needs to imitate the sequence by choosing that same colour. It’s then Computer’s turn. A new colour will be added to the sequence, and again the player will have to imitate the sequence by choosing the colours in the same order. The game progresses until the player makes a mistake.

### Project Goals

- Create a Python implementation/clone of the classic Simon game
- Implement a user-friendly interface using appropriate Python libraries (Pygame)
- Practice and demonstrate Python programming concepts learned in CS50P
- Build a more complex app with the help of Gemini Assistant. I believe that today it is even more complicated to try and avoid AI’s assistance rather than embrace it. For this reason, I have deactivated all direct suggestions in the code and used the assistant as a guide to build “on the blank page” or to help identify errors

## Development Log, challenges & solutions

- Start with an initial state
- Build a main *while* loop where we can define COMPUTER TURN (showing the sequence of colours) and PLAYER TURN (make a choice)
- Write function helpers to handle the main processes: colours sequence build and show, player choosing with a mouse or with a keyboard
- Up to this point, in place of “colours” I had used text placeholders (up, left, down, right). Now we start to add graphics, with four coloured rectangles
- *Here I encounter many difficulties in grasping the concept of pygame having to draw every time all the screen. Eventually I find a way to have only one rectangle turning on and then off again. In the end most of the problem came out of a typo, where an underscore was missing smh (the art of debugging, I guess, is the ultimate goal)*
- Adjust timing of colour sequence and general pacing of the game
- When player makes a choice we need to see the button pressed lighten up. Build a function flash_button()
- Created some sounds in Firefly and modified them in Audition for the button sounds
- I noticed another small bug that it would be nice to fix: if a player is hitting keys while the computer is showing the sequence the program still "accepts" it and memorise it. We need to wait until the sequence is shown before the program can listen to any player input
- Collect the (free) font for the intro, info and game over screen: Public Pixel - https://ggbot.itch.io/public-pixel-font
- Then I need an intro and a game over/score/restart screen. In the beginning Gemini proposed the option to change most of the code structure, but at this stage I prefer to keep building on my own by trying to integrate all on one screen, just changing the states of the game
- Idea for an Info pop-up in the style of a lightbox. *Solution: not a lightbox, but it works through game states*
- Encountered a problem with refreshing of screen - the info screen does not disappear. Or another problem: when clicking on button, the rest of the gfx disappears. Also the dynamics for wrong answers are now broken. *fixed: screen drawing issue and a typo*
- Final tests

### Project Structure

```
project/
├── README.md
├── requirements.txt
├── project.py       # Main code
├── sounds/          # Game audio files
├── font.ttf         # Game audio files
└── test_project.py  # Unit tests

```

## Implementation Details

### Core Features

- Random sequence generation
- Visual and audio through pygame
- Score tracking
- Increasing difficulty through longer sequences
- Game states check

### Python Concepts Applied

- Functions and control flow
- Object-oriented programming
- Player’s input and interactivity
- Libraries and modules
- Testing

### Functions/helpers inside main()

- colour_seq(): selects a random colour and adds it to the sequence
- show_seq(): shows the sequence on screen
- get_choice_from_pos(): collects the data of a player’s choice made with a mouse
- get_choice_from_key(): collects the data of a player’s choice made with a keyboard
- flash_button(): the button pressed by the player flashes up with colour
- check_player_input(): checks if a player’s choice is correct or wrong

### Functions tested with pytest

- test_check_player_input(): tests a correct choice, an incorrect choice, a correct choice at a wrong time, an index that is out of bounds
- test_get_choice_from_key(): tests WASD, arrow keys, and a key that returns nothing
- test_colour_seq(): tests the presence of a colour in a sequence and its validity

## Future Improvements

Increase the speed of the sequence of colours being shown as we are progressing

Introduce a database to store high scores

Add a music score to the intro and/or the game
