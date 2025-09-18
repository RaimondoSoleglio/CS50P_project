import random
import pygame
import asyncio

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

# mapping COLOURS with rects and properties
rect_map = {
    'up': {'rect': top, 'on': RED, 'off': RED_OFF},
    'left': {'rect': left, 'on': GREEN, 'off': GREEN_OFF},
    'down': {'rect': bottom, 'on': BLUE, 'off': BLUE_OFF},
    'right': {'rect': right, 'on': YELLOW, 'off': YELLOW_OFF},
}

async def flash_button(choice, screen, sounds):
    # to see the button lighten up when clicked

    # First, draw all the buttons in their OFF state
    for c, button_info in rect_map.items():
        if c != choice: # if it's not the button we're flashing
            pygame.draw.rect(screen, button_info['off'], button_info['rect'], border_radius=30)


    button = rect_map[choice]
    pygame.draw.rect(screen, button['on'], button['rect'], border_radius=30)

    sounds[choice].play()
    pygame.display.flip()
    await asyncio.sleep(0.2) # the time it stays lit

    # then all off again
    for rect_dark in rect_map.values():
        pygame.draw.rect(screen, rect_dark['off'], rect_dark['rect'], border_radius=30)
    pygame.display.flip()


def colour_seq(sequence):

    # select a random colour
    rnd_colour = random.choice(COLOURS)

    # append the colour to the sequence list
    sequence.append(rnd_colour)


async def show_seq(sequence, screen, sounds):

    # loop needed for pygame to draw each frame of the seq
    # we hold the properties for the button to lit
    for colour in sequence:
        rect_bright = rect_map[colour]

        # then we cycle through all 4 buttons to make them dark, using this model:
        # pygame.draw.rect(screen, RED, top, border_radius = 30)
        for rect_dark in rect_map.values():
            pygame.draw.rect(screen, rect_dark['off'], rect_dark['rect'], border_radius = 30)

        # then we "draw" bright on top and play the sound
        pygame.draw.rect(screen, rect_bright['on'], rect_bright['rect'], border_radius = 30)
        sounds[colour].play()

        # draw the frame
        pygame.display.flip()
        await asyncio.sleep(0.5)   # wait

        # light off again
        for rect_dark in rect_map.values():
            pygame.draw.rect(screen, rect_dark['off'], rect_dark['rect'], border_radius = 30)

        pygame.display.flip()
        await asyncio.sleep(0.1)

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


def check_player_input(sequence, player_choice, turn_index):

    # returns right or wrong
    if turn_index < len(sequence):
        return sequence[turn_index] == player_choice
    return False


async def main():

    # initialising pygame
    pygame.init()
    pygame.mixer.init()

    # mapping SOUNDS
    sounds = {
        'up': pygame.mixer.Sound("sounds/Button1.wav"),
        'left': pygame.mixer.Sound("sounds/Button2.wav"),
        'down': pygame.mixer.Sound("sounds/Button3.wav"),
        'right': pygame.mixer.Sound("sounds/Button4.wav")
    }

    # fonts
    title_font = pygame.font.Font("font.ttf", 40)
    button_font = pygame.font.Font("font.ttf", 28)

    # buttons
    start_button = pygame.Rect(200, 250, 200, 50)
    again_button = pygame.Rect(200, 320, 200, 50)
    exit_button = pygame.Rect(200, 380, 200, 50)

    # Info button
    info_button = pygame.Rect(10, 10, 30, 30)
    info_font = pygame.font.Font("font.ttf", 15) # a smaller font for the 'i'
    instruction_font = pygame.font.Font("font.ttf", 16)

    # we need a screen
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # creating the window
    pygame.display.set_caption("CS50P Simon Game - My Final Project")

    # game states
    game_state = 'START_SCREEN'
    play_state = 'COMPUTER TURN'
    previous_game_state = ''

    score = 0
    sequence = []
    player_turn_index = 0

    # a variable to control the game loop
    running = True

    pygame.event.clear()
    while running:

        player_choice = None

        # starting with total black
        screen.fill((0, 0, 0))

        # start screen - waiting for player to hit start
        if game_state == 'START_SCREEN':

            # info button
            pygame.draw.circle(screen, (200, 200, 200), info_button.center, 15)
            info_text = info_font.render("i", True, (0, 0, 0))
            screen.blit(info_text, (info_button.centerx - info_text.get_width() // 2, info_button.centery - info_text.get_height() // 2))

            # title and start button
            title_text = title_font.render("Simon Game", True, (255, 255, 255))
            screen.blit(title_text, (600 // 2 - title_text.get_width() // 2, 150))

            pygame.draw.rect(screen, (0, 150, 0), start_button, border_radius=10)
            start_text = button_font.render("START", True, (255, 255, 255))
            screen.blit(start_text, (start_button.centerx - start_text.get_width() // 2, start_button.centery - start_text.get_height() // 2))


            # checking for user input (event loop)
            for event in pygame.event.get():

                # what happens when user clicks CLOSE button
                if event.type == pygame.QUIT:
                    running = False

                # if the click START button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(event.pos):
                        game_state = 'PLAYING'

                # if they press Spacebar or T
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_state = 'PLAYING'

                # if info
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if info_button.collidepoint(event.pos):
                        previous_game_state = game_state
                        game_state = 'INFO_SCREEN'

                # if info
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_i:
                        previous_game_state = game_state
                        game_state = 'INFO_SCREEN'

        elif game_state == 'PLAYING':

            # game logic
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if play_state == 'PLAYER TURN':

                    # keyboard input
                    if event.type == pygame.KEYDOWN:
                        player_choice = get_choice_from_key(event.key)

                    # mouse input
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        player_choice = get_choice_from_pos(event.pos, rects)


            # game logic - states
            if play_state == 'COMPUTER TURN':

                await asyncio.sleep(0.5)

                # computer adds a colour to the sequence
                colour_seq(sequence)

                # computer shows the sequence
                await show_seq(sequence, screen, sounds)

                # this line to clear the event queue
                # it will help with problem of players choosing during the sequence show
                pygame.event.clear()

                # change state
                play_state = 'PLAYER TURN'

                # reset the player's progress
                player_turn_index = 0

            elif play_state == 'PLAYER TURN':

                # if the player has made a choice we check with the func
                if player_choice is not None:
                    await flash_button(player_choice, screen, sounds)
                    is_correct = check_player_input(sequence, player_choice, player_turn_index)

                    if is_correct:
                        player_turn_index += 1

                        if player_turn_index == len(sequence):
                            score += 1
                            await asyncio.sleep(0.5)
                            play_state = 'COMPUTER TURN'

                    else:   # wrong answer
                        game_state = 'GAME_OVER'


            # --- DRAWING CODE ---

            # dark colours at start
            pygame.draw.rect(screen, RED_OFF, top, border_radius=30)
            pygame.draw.rect(screen, GREEN_OFF, left, border_radius=30)
            pygame.draw.rect(screen, BLUE_OFF, bottom, border_radius=30)
            pygame.draw.rect(screen, YELLOW_OFF, right, border_radius=30)


        elif game_state == 'GAME_OVER':

            # info button
            pygame.draw.circle(screen, (200, 200, 200), info_button.center, 15)
            info_text = info_font.render("i", True, (0, 0, 0))
            screen.blit(info_text, (info_button.centerx - info_text.get_width() // 2, info_button.centery - info_text.get_height() // 2))

            game_over_text = title_font.render("Game Over", True, (255, 255, 255))
            score_text = button_font.render(f"Your Score: {score}", True, (255, 255, 255))
            screen.blit(game_over_text, (600 // 2 - game_over_text.get_width() // 2, 150))
            screen.blit(score_text, (600 // 2 - score_text.get_width() // 2, 250))

            pygame.draw.rect(screen, (0, 150, 0), again_button, border_radius=10)
            again_text = button_font.render("AGAIN?", True, (255, 255, 255))
            screen.blit(again_text, (again_button.centerx - again_text.get_width() // 2, again_button.centery - again_text.get_height() // 2))

            pygame.draw.rect(screen, (150, 0, 0), exit_button, border_radius=10)
            exit_text = button_font.render("EXIT", True, (255, 255, 255))
            screen.blit(exit_text, (exit_button.centerx - exit_text.get_width() // 2, exit_button.centery - exit_text.get_height() // 2))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # handes mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if again_button.collidepoint(event.pos):
                        # --- Reset the game variables ---
                        score = 0
                        sequence = []
                        play_state = 'COMPUTER TURN'
                        player_turn_index = 0
                        game_state = 'PLAYING' # Go back to playing
                    elif exit_button.collidepoint(event.pos):
                        running = False

                # handle key presses
                if event.type == pygame.KEYDOWN:
                    # Pressing SPACE starts a new game
                    if event.key == pygame.K_SPACE:
                        # --- Reset the game variables ---
                        score = 0
                        sequence = []
                        play_state = 'COMPUTER TURN'
                        player_turn_index = 0
                        game_state = 'PLAYING'
                    # Pressing ESC quits the game
                    elif event.key == pygame.K_ESCAPE:
                        running = False

                # if info
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if info_button.collidepoint(event.pos):
                        previous_game_state = game_state
                        game_state = 'INFO_SCREEN'

                # if info
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_i:
                        previous_game_state = game_state
                        game_state = 'INFO_SCREEN'


        elif game_state == 'INFO_SCREEN':

            info_title_surf = title_font.render("How to play", True, (255, 255, 255))
            screen.blit(info_title_surf, (600 // 2 - info_title_surf.get_width() // 2, 50))

            instructions = [
                "SIMON GAME - by Roberto Sommella",
                "A CS50P Final Project",
                "",
                "Repeat the sequence of colours.",
                "",
                "Use the mouse to click the buttons",
                "or WASD / Arrow Keys.",
                "",
                "On the menu screens:",
                "SPACE or Click to Play Again.",
                "ESC or Click to Exit.",
            ]

            line_y = 150

            for line in instructions:
                line_surf = instruction_font.render(line, True, (200, 200, 200))
                screen.blit(line_surf, (600 // 2 - line_surf.get_width() // 2, line_y))
                line_y += 30 # move down for the next line

            # --- Event handling to close the info screen ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Pressing ESC or clicking the mouse closes the info screen
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_state = previous_game_state # go back!
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_state = previous_game_state # go back!


        # at the end we need updating he screen with all the drawing in this loop iteration
        pygame.display.flip()
        await asyncio.sleep(0)


    # we are here once the 'while' loop is finished
    pygame.quit()


if __name__ == "__main__":
    asyncio.run(main())