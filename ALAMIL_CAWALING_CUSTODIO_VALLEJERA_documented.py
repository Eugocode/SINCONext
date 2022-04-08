#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
# Programmers: Limuelle Alamil, Dleamnor Euraze Cawaling, Adrian Miguel Custodio, Khean Marie Vallejera
#Date: 11/10/19
# Name of Program: "SINCONext"
# Description: A UPV-themed catching and dodging game made using Python language and Pygame module
# Presented to: Mrs. Christi Florence C. Cala-or
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
import pygame
import random
import time
pygame.init()
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
display_width = 800  # dimension of the window in x-axis
display_height = 600  # dimension of the window in y-axis

game_display = pygame.display.set_mode((800, 600))  # the dimensions of screen
pygame.display.set_caption("SINGKO Next")  # set the caption of the screen
clock = pygame.time.Clock()  # the time-monitoring variable of the game

# the background displayed when window open
background_intro = pygame.image.load('TITLE SCREEN.png')
# set the size of the background to the stated dimensions
background_intro = pygame.transform.scale(background_intro, (800, 600))

# the background displayed when game start
background_game = pygame.image.load('TOMAS FONACIER_2.png')
# set the size of the background to the stated dimensions
background_game = pygame.transform.scale(background_game, (800, 600))

pygame.display.set_icon(background_game)  # set the icon of the game

black = (0, 0, 0)  # colors created by adjusting the RGB
bright_yellow = (255, 255, 128)
block_color = (53, 115, 255)

character_width = 5  # dimension of the character

book_rec = pygame.Rect(-500, -50, 40, 40)  # creates a hitbox for the books
# creates a hitbox for the player
default_player = pygame.Rect(400, 380, 150, 150)
# ***hitbox: an invisible rectangle whose coordinates are checked to announce collision
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
#				DICTIONARIES containing the files used throughout the program
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
characters_move = {"lim": [pygame.image.load("LIM_HAND_UP.png"), pygame.image.load("LIM_HAND_DOWN.png")], "dleam": [pygame.image.load("EURAZE_HAND_UP.png"), pygame.image.load("EURAZE_HAND_DOWN.png")], "yanni": [pygame.image.load(
    "YANNI_HAND_UP.png"), pygame.image.load("YANNI_HAND_DOWN.png")], "khean": [pygame.image.load("KHEAN_HAND_UP.png"), pygame.image.load("KHEAN_HAND_DOWN.png")], "isko": [(pygame.image.load("PLAYER1.png")), (pygame.image.load("PLAYER2.png"))]}
#characters_down={"lim": pygame.image.load("LIM_HAND_DOWN.png"), "dleam": pygame.image.load("EURAZE_HAND_DOWN.png"), "yanni": pygame.image.load("YANNI_HAND_DOWN.png"), "khean": pygame.image.load("KHEAN_HAND_DOWN.png")}
profmoves = {1: [pygame.image.load("ANJ_REST.png"), pygame.image.load("ANJ_LEFT.png"), pygame.image.load("ANJ_BOTH.png"), pygame.image.load("ANJ_RIGHT.png")], 2: [pygame.image.load("MELOH_REST.png"), pygame.image.load(
    "MELOH_LEFT.png"), pygame.image.load("MELOH_BOTH.png"), pygame.image.load("MELOH_RIGHT.png")], 3: [pygame.image.load("NILO_REST.png"), pygame.image.load("NILO_LEFT.png"), pygame.image.load("NILO_BOTH.png"), pygame.image.load("NILO_RIGHT.png")]}

buttons_inactive = {"play": pygame.image.load("PLAY_BUTTON (1).png"), "quit": pygame.image.load("QUIT_BUTTON.png"), "help": pygame.image.load("HELP_BUTTON.png"), "back": pygame.image.load("BACK_BUTTON.png"), "menu": pygame.image.load("MENU_BUTTON.png"), "cont": pygame.image.load(
    "CONTN_BUTTON.png"), "choose": pygame.image.load("CHOOSE_BUTTON.png"), "euraze": pygame.image.load("EURAZE_BUTTON.png"), "khean": pygame.image.load("KHEAN_BUTTON.png"), "lim": pygame.image.load("LIM_BUTTON.png"), "yanni": pygame.image.load("YAN_BUTTON.png"), "about": pygame.image.load("INDO_BUTTON.png")}
buttons_active = {"play": pygame.image.load("PLAY_BUTTON_HOVER.png"), "quit": pygame.image.load("QUIT_BUTTON_HOVER.png"), "help": pygame.image.load("HELP_BUTTON_HOVER.png"), "back": pygame.image.load("BACK_BUTTON_HOVER.png"), "menu": pygame.image.load("MENU_BUTTON_HOVER.png"), "cont": pygame.image.load(
    "CONTN_BUTTON_HOVER.png"), "choose": pygame.image.load("CHOOSE_BUTTON_HOVER.png"), "euraze": pygame.image.load("EURAZE_BUTTON_HOVER.png"), "khean": pygame.image.load("KHEAN_BUTTON_HOVER.png"), "lim": pygame.image.load("LIM_BUTTON_HOVER.png"), "yanni": pygame.image.load("YAN_BUTTON_HOVER.png"), "about": pygame.image.load("INDO_BUTTON_HOVER.png")}

other_assets = {"help": pygame.image.load("INSTRUCTION.png"), "credits": pygame.image.load("CREDITS.png"), "victory": pygame.image.load("CONGRATS.png"), "level1": pygame.image.load("LEVEL1.png"), "level2": pygame.image.load(
    "LEVEL2.png"), "level2": pygame.image.load("LEVEL3.png"), "char_bg": pygame.image.load("CHAR_BG.png"), "pause": pygame.image.load("TITLE ONLY.PNG"), "game_over": pygame.image.load('GAME OVER.png')}
lebooks = {1: [pygame.image.load("blue_1.png"),  pygame.image.load("blue_2.png"),  pygame.image.load("blue_3.png"),  pygame.image.load("blue_4.png"),  pygame.image.load("blue_5.png")],
           2: [pygame.image.load("green_1.png"), pygame.image.load("green_2.png"), pygame.image.load("green_3.png"), pygame.image.load("green_4.png"), pygame.image.load("green_5.png")],
           3: [pygame.image.load("orange_1.png"), pygame.image.load("orange_2.png"), pygame.image.load("orange_3.png"), pygame.image.load("orange_4.png"), pygame.image.load("orange_5.png")]}

bg_music = {1: "Jump-Up-Super-Star-8-Bit-Remix-Super-Mario-Odyssey.wav",
            2: "Pokemon-BlackWhite-Gym-Leader-Last-Pokemon-Music-HQ.wav", 3: "Undertale-Megalovania.wav"}
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
#				GLOBAL VARIABLES used throughout the program
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
maxScore = 25  # the value that makes the player proceed to the next level; decremented by the falling books
finalscore = 0  # the performance of the player; just a compliment of the player's performance
hitvar = 50  # the hitpoints of the player; decremented whenever the player hit a book; the game ends when this become 0
level = 1  # the level of the player
game_exit = False  # tells whether the player is still playing or not
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
#				RANDOM BOOK GENERATOR: assigns random x and y value for the books and adds "hitbox" as an instance
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
list_uno_books = []  # contains the books in a list
for i in range(15*level):  # parameter for the number of books to be thrown
    x = random.randrange(0, 800)  # assigns a random x value for the book
    y = random.randrange(0, 600)  # assigns a random y value for the book
    # appends the book with assigned random x and y value together with a hitbox
    list_uno_books.append(pygame.Rect(x, y, 20, 20))

list_dos_books = []
for i in range(15*level):
    x = random.randrange(0, 800)
    y = random.randrange(0, 600)
    list_dos_books.append(pygame.Rect(x, y, 20, 20))

list_tres_books = []
for i in range(maxScore*level):
    x = random.randrange(0, 800)
    y = random.randrange(0, 600)
    list_tres_books.append(pygame.Rect(x, y, 20, 20))

list_kwatro_books = []
for i in range(4*level):
    x = random.randrange(0, 800)
    y = random.randrange(0, 600)
    list_kwatro_books.append(pygame.Rect(x, y, 20, 20))

list_singko_books = []
for z in range(5*level):
    x = random.randrange(0, 800)
    y = random.randrange(0, 600)
    list_singko_books.append(pygame.Rect(x, y, 20, 20))

#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
#				GAME INTRO: the first screen that the player will see in the window; contains the start and quit button together with other screen buttons
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
pause = False  # pause variable used in pausing function


def game_intro():  # function that will display a start menu
    music = "Wreck-It-Ralph-OST-17-One-Minute-to-Win-It.wav"  # the music for the intro
    pygame.mixer.init()  # initialize the mixer module (to let music play on the background)
    pygame.mixer.music.load(music)  # loads the audio file
    pygame.mixer.music.play()  # plays the audio file
    intro = True
    while intro:
        for event in pygame.event.get():  # for every event in the window
            if event.type == pygame.QUIT:  # if the user presses quit buton
                pygame.quit()  # the game terminates
        # Note: the buttons are not built-in in Pygame since the module doesn't support widgets :(
        #	the buttons are made by the programmers themeselves by creating a function that takes certain attributes
        #	and assigning a certain command at each one that is commence by checking if the cursor's coordinate exist
        #	within the coordinates of the button
        game_display.blit(background_intro, (0, 0))
        # function--inactive image of the button--active image of the button--x-coordinate--y-coordinate--length--width--command
        # starts the game; calls the game_loop
        button(buttons_inactive["play"], buttons_active["play"],
               142.5, 442.5, 136, 56, "START")
        # terminates the game from the inside; calls the game_quit
        button(buttons_inactive["quit"], buttons_active["quit"],
               512.5, 442.5, 136, 56, "EXIT")
        button(buttons_inactive["help"], buttons_active["help"],
               700, 50, 56, 56, "HELP")  # shows the instructions
        # shows the avatar options when the default avatar is not chosen
        button(buttons_inactive["choose"],
               buttons_active["choose"], 625, 50, 56, 56, "CHOOSE")
        # shows the name of the programmers and the credits
        button(buttons_inactive["about"],
               buttons_active["about"], 550, 50, 56, 56, "ABOUT_US")

        pygame.display.update()  # will update all the changes made
        clock.tick(15)  # will show not more than 15 frames per second

#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
#				THE AVATARS: the avatars are characters (the programmers) that the player can choose before starting the game
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#


def choose_character():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        bg = pygame.image.load("CHAR_BG.png")  # the background of the screen
        # sets the background to the desired dimensions
        bg = pygame.transform.scale(bg, (800, 600))
        game_display.blit(bg, (0, 0))  # displays the background to the screen
        # ***blit: it is like the print function in regular Python coding;
        # will bring back the player to the start menu
        button(buttons_inactive["menu"],
               buttons_active["menu"], 10, 10, 136, 56, "M_MENU")
        # displays the avatars(sprites)
        game_display.blit(characters_move["lim"][1], (120, 100))
        game_display.blit(characters_move["dleam"][1], (120, 350))
        game_display.blit(characters_move["yanni"][1], (490, 100))
        game_display.blit(characters_move["khean"][1], (490, 350))
        # displays the button that chooses the avatars
        button(buttons_inactive["lim"], buttons_active["lim"],
               125, 250, 136, 56, "LIMUELLE")
        button(buttons_inactive["euraze"],
               buttons_active["euraze"], 125, 500, 136, 56, "DLEAMNOR")
        button(buttons_inactive["yanni"],
               buttons_active["yanni"], 495, 250, 136, 56, "ADRIAN")
        button(buttons_inactive["khean"],
               buttons_active["khean"], 495, 500, 136, 56, "KHEAN")

        pygame.display.update()
        clock.tick(15)

#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
#				Other buttons in the start menu: Instructions and Credits
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#


def help_screen():  # function that will show the instructions
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        game_display.fill(bright_yellow)
        game_display.blit(other_assets["help"], (40, 0))
        button(buttons_inactive["back"],
               buttons_active["back"], 10, 10, 56, 56, "BACK")

        pygame.display.update()
        clock.tick(15)


def about_us():  # the function that will show the credits and the name of the programmers
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        game_display.fill(block_color)
        game_display.blit(other_assets["credits"], (40, 0))
        button(buttons_inactive["back"],
               buttons_active["back"], 10, 10, 56, 56, "BACK")

        pygame.display.update()
        clock.tick(15)

#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#


def game_quit():
    pygame.quit()
    quit()

#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
#				VICTORY SCREEN: will be commenced once the player wins
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#


def game_you_won():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game_display.blit(other_assets["victory"], (0, 0))  # victory screen
        # button that will terminate the program
        button(buttons_inactive["quit"],
               buttons_active["quit"], 550, 450, 136, 56, "EXIT")

        pygame.display.update()
        clock.tick(150)

#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
#		POINTS MANAGER: manages and displays the hits, points and levels of the game; called by other game-monitoring functions
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#


def things_dodged(movement, default_player):  # **FUNCTION: will show the scores**
    global maxScore
    global finalscore
    global level
    level_bg = {1: pygame.image.load("LEVEL1.png"), 2: pygame.image.load("LEVEL2.png"), 3: pygame.image.load(
        "LEVEL3.png")}  # the images shown on each level(e.g. Level 1 History)
    if maxScore == 0:  # condition for when the number books to fall in order to proceed to the next level is staisfied
        if level < 3:  # if not last level
            game_display.blit(level_bg[level], (0, 0))
            pygame.display.update()
            clock.tick(1)
            maxScore = 25  # sets a new maxScore for the next level
            level += 1  # add 1 to the level
            # calls again the game_loop but with different books and opponents
            game_loop(movement, default_player)
        else:
            game_you_won()
    font_score = pygame.font.SysFont(None, 25)
    text_score = font_score.render(
        "Your GWA: "+str(finalscore)+"%", True, black)  # the score
    # will display the score at the upperleft corner
    game_display.blit(text_score, (0, 0))


def hitpoints(movement, x1, y1):  # if collision is true
    global hitvar
    if hitvar <= 0:  # when the player loses all his/her hitpoints
        game_crash(movement, x1, y1)  # the game will end
    else:
        # will show the amount of hitpoints left
        font_score = pygame.font.SysFont(None, 25)
        text_lives = font_score.render("Your Lives: "+str(hitvar), True, black)
        game_display.blit(text_lives, (0, 100))

#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
#				Other events in the game: pause, unpause, game over
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#


def game_unpause():  # contradicts the pause function
    global pause
    pause = False


def game_paused():  # will pause the game by pressing the pause button
    # will show a pause-indicator image in the screen
    game_display.blit(other_assets["pause"], (20, 0))
    while pause:  # while True
        for event in pygame.event.get():  # for every event in the window
            if event.type == pygame.QUIT:  # if the user presses quit buton
                pygame.quit()  # the game terminates
                quit()
        # unpause the game; calls the game_unpause function
        button(buttons_inactive["cont"], buttons_active["cont"],
               150, 450, 136, 56, "CONTINUE")
        button(buttons_inactive["quit"], buttons_active["quit"],
               550, 450, 136, 56, "NOT CONTINUE")  # terminates the game
        button(buttons_inactive["menu"], buttons_active["menu"],
               10, 50, 136, 56, "M_MENU")  # go backs to the start menu

        pygame.display.update()
        clock.tick(15)


def game_crash(movement, x1, y1):
    intro = True  # will blit the text on the window
    while intro:  # while True
        for event in pygame.event.get():  # for every event in game
            if event.type == pygame.QUIT:  # if the user presses quit buton
                pygame.quit()  # the game terminates
                quit()
        over = pygame.image.load("GAME OVER.png")  # game over screen
        game_display.blit(over, (0, 0))
        button(buttons_inactive["quit"],
               buttons_active["quit"], 550, 450, 136, 56, "EXIT")
        pygame.display.update()
        clock.tick(15)

#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
#				THE MAIN LOOP/BODY OF THE GAME/THE ACTUAL GAME
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#


def game_loop(movement, default_player):
    global level
    music = bg_music[level]
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()
    global pause
    global hit
    global finalscore
    x = 400  # the initial x coordinate of the player
    y = 440  # the initial y coordinate of the player

    hit = False
    left = False
    right = False

    x_change = 0  # movement of the character in the x-axis
    hit = 0  # the number of collisions

    # professor position
    profX = 305
    profY = 90
    profx_change = 4*level

    # means that the user is quitting the game or not (not in this case)
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():  # event handling loop
            # if the user presses quit button (X)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()  # the game terminates
            if event.type == pygame.KEYDOWN:  # if user holds the key
                if event.key == pygame.K_LEFT:  # if user press left arrow key
                    x_change -= 10  # character will move to the left
                    left = True
                    right = False
                if event.key == pygame.K_RIGHT:  # if user press right arrow key
                    x_change += 10  # character will move to the right
                    left = False
                    right = True
                if event.key == pygame.K_SPACE:  # if user press space button
                    pause = True
                    game_paused()  # will pause the game
            if event.type == pygame.KEYUP:  # if user let go of the key
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0  # character will not move anymore
                    left = False
                    right = False

                    # the character will move from current position+change based on the presses
        rect = background_game.get_rect()
        game_display.blit(background_game, rect)
        # Player Movement: Controlled by the player
        # character animation: the program displays a particular image at a particular time and coordinate consecutively to make the illusion of movement
        if left:
            # cycles through the images(frames) to show "movement"
            game_display.blit(movement[x_change//-8], (x, y))
            # move hitbox along with the image
            default_player = pygame.Rect(x, y, 150, 150)
        elif right:
            game_display.blit(movement[x_change // 8], (x, y))
            default_player = pygame.Rect(x, y, 150, 150)
        else:
            game_display.blit(movement[0], (x, y))

        x += x_change  # changes x position

        # program set a border so player couldn't escape the screen
        if x <= 0:
            x = 0
        elif x >= 630:
            x = 630

        # Prof Movement: Running throughout the game, uncontrolled by the player
        profX += profx_change  # moves through the x-axis
        # limits the prof's movement
        if profX <= 70:  # increases once reached
            profx_change += 1
        elif profX >= 540:  # decreases once reached
            profx_change -= 1

        # prof animation
        if profX > 70 or profX < 540:
            # cycles through the prof's frames depending on the level para intense
            game_display.blit((profmoves[level])[
                              profx_change//4], (profX, profY))

        # calls functions
        # displays scores; will manage next levels and other conditions stated in the comments of the actual function
        things_dodged(movement, default_player)
        hitpoints(movement, x, y)  # checks and the amount of hitpoints left
        falling_books()  # will make the books fall down
        draw_books()  # will show the falling books on the screen
        # checks for collision(when the player touches books)
        collision_check(movement, default_player)

        pygame.display.update()
        clock.tick(100)  # the program will show at most 120 frames per second

#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
#				MAKE THE BOOKS FALL: will let the books look like falling in the screen
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#


def falling_books():
    global level
    global maxScore
    # Process each uno books in the list
    for u in range(len(list_uno_books)):
        # Draw the blue book(UNO) inside the default_player
        game_display.blit(lebooks[level][0], book_rec)
        #  Make book fall.
        list_uno_books[u][1] += 2*level  # y-axis
        # If the book leaves screen
        if list_uno_books[u][1] > 600:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            list_uno_books[u][1] = y
        # Give it a new x position
            x = random.randrange(0, 800)
            list_uno_books[u][0] = x
    # Process dos books
    for d in range(len(list_dos_books)):
        # Draw the blue book(DOS) inside the default_player
        game_display.blit(lebooks[level][1], book_rec)
        #  Make book fall.
        list_dos_books[d][1] += 2*level
        # If the book leaves screen
        if list_dos_books[d][1] > 600:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            list_dos_books[d][1] = y
        # Give it a new x position
            x = random.randrange(0, 800)
            list_dos_books[d][0] = x
        # Proces tres books
    for t in range(len(list_tres_books)):
        # Draw the blue book(TRES) inside the default_player
        game_display.blit(lebooks[level][2], book_rec)
        #  Make book fall.
        list_tres_books[t][1] += 2*level
        #     # If the book leaves screen
        if list_tres_books[t][1] > 800:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            list_tres_books[t][1] = y
        # Give it a new x position
            x = random.randrange(0, 800)
            list_tres_books[t][0] = x
        # Proces tres books
    for f in range(len(list_kwatro_books)):
        # Draw the blue book(TRES) inside the default_player
        game_display.blit(lebooks[level][3], book_rec)
        #  Make book fall.
        list_kwatro_books[f][1] += 2*level
        # If the book leaves screen
        if list_kwatro_books[f][1] > 600:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            list_kwatro_books[f][1] = y
        # Give it a new x position
            x = random.randrange(0, 800)
            list_kwatro_books[f][0] = x
            maxScore -= 1  # Process each book in the list
    for s in range(len(list_singko_books)):
        game_display.blit(lebooks[level][4], book_rec)
        # Make book fall.
        list_singko_books[s][1] += 3*level
        # If the coal leaves screen
        if list_singko_books[s][1] > 600:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            list_singko_books[s][1] = y
        # Give it a new x position
            x = random.randrange(0, 800)
            list_singko_books[s][0] = x
            maxScore -= 1
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
#		COLLISION: checks if the player touches a book
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#


def collision_check(movement, default_player):
    global maxScore
    global finalscore
    global hitvar
    # Check whether the player has intersected with any books
    # Note: Collision is an event that is True when two surfaces(e.g. image, shape) happen to have atleast one same coordinate
    #		Atleast one coordinate of one surface overlapped with any of the coordinates of the other surface
    #		This is possible by putting a hitbox (pygame.Rect()) to the surfaces
    #		The hitboxes contains the coordinates that will be checked by the "colliderect" a built-in function in Pygame
    for book in list_uno_books[:]:  # traverses the list containing the books
        if default_player.colliderect(book):  # if there is collision
            # the book that collides will be removed to the list to make it look like it pop out of the game
            list_uno_books.remove(book)
            maxScore -= 1  # decreases playing time/maxScore
            finalscore += 3  # adds to overall score of the player
    for book in list_dos_books[:]:
        if default_player.colliderect(book):
            list_dos_books.remove(book)
            maxScore -= 1
            finalscore += 2

    for book in list_tres_books[:]:
        if default_player.colliderect(book):
            list_tres_books.remove(book)
            maxScore -= 1
            finalscore += 1

    for books in list_kwatro_books[:]:
        if default_player.colliderect(books):
            list_kwatro_books.remove(books)
            maxScore -= 1
            finalscore -= 1  # deducts to overall score of the player
            hitvar -= 5  # deducts to the hitpoints of the player

    for books in list_singko_books[:]:
        if default_player.colliderect(books):
            list_singko_books.remove(books)
            maxScore -= 1
            finalscore -= 2
            hitvar -= 10

#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
#				Will display the books on the screen
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#


def draw_books():
    # Draw the uno book
    for book in list_uno_books:
        game_display.blit(lebooks[level][0], book)
        # Draw dos book
    for book in list_dos_books:
        game_display.blit(lebooks[level][1], book)
    # Draw tres book
    for book in list_tres_books:
        game_display.blit(lebooks[level][2], book)
    # Draw kwatro book
    for book in list_kwatro_books:
        game_display.blit(lebooks[level][3], book)
        # Draw singko book
    for book in list_singko_books:
        game_display.blit(lebooks[level][4], book)

    pygame.display.update()
    clock.tick(60)

#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#
#				BUTTONS: The button function made to act as button widgets in the game
#================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================#


def button(button1, button2, x, y, w, h, action=None):  # **FUNCTION**: will create the button
    mouse = pygame.mouse.get_pos()  # will track the position of the mouse (0, 0, 0)
    # will show what button of the mouse was clicked [(1, 0, 0) means you left-clicked]
    click = pygame.mouse.get_pressed()
    # print(click)	#'uncomment' to see how (1, 0, 0) works
    # if the cursor is inside the area of the "button"
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        # the "button" will change into active form (bright)
        game_display.blit(button2, (x, y))
        if click[0] == 1 and action != None:  # the user left-clicked the mouse
            # the commands to be executed when the buttons are pressed
            if action == "START":
                level = 1
                game_loop(characters_move["isko"], (default_player))
            elif action == "EXIT":
                game_quit()
            elif action == "CHOOSE":
                choose_character()
            elif action == "HELP":
                help_screen()
            elif action == "ABOUT_US":
                about_us()
            elif action == "M_MENU":
                game_exit = True
                game_intro()
            elif action == "BACK":
                game_intro()
            elif action == "CONTINUE":
                game_unpause()
            elif action == "NOT CONTINUE":
                game_quit()
            elif action == "LIMUELLE":
                game_loop(characters_move["lim"], (default_player))
            elif action == "DLEAMNOR":
                game_loop(characters_move["dleam"], (default_player))
            elif action == "ADRIAN":
                game_loop(characters_move["yanni"], (default_player))
            elif action == "KHEAN":
                game_loop(characters_move["khean"], (default_player))
    # if the cursor is outside the area of the "button"(or the default_player)
    else:
        # the "button" will change into inactive form (dull)
        game_display.blit(button1, (x, y))


game_intro()
game_loop()
pygame.quit()
quit()
