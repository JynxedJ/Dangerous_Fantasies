# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define player = Character('Protagonist', image="player", color="#c8ffc8")
define player2 = Character('Protagonist', image="player", color="#000000")

image logo = "logo.png"

image side player avatar = "playeravatar.png"

init:
    image black = Solid((0, 0, 0, 255))
    image white = Solid((255, 255, 255, 255))
    image grey = Solid((128, 128, 128, 255))

# This is the splash screen. Should show my logo, and then the 
# instructions for playing on the Ouya.
label splashscreen:
    show logo
    with dissolve
    with Pause(3)
    return    

# The game starts here.
label start:
    show logo with Pause (0.5)
    scene black with dissolve
    show text " Finally Weekend! \n\n Unfortunately u can't sleep anymore \n\n Time to get up " with Pause(4.5)
    scene black with dissolve

    menu:
        "Scratch between the legs":
            jump malestart
        "untangle hair":
            jump femalestart
    return

label malestart:
    player avatar "You've created a new Ren'Py game."

    player "Once you add a story, pictures, and music, you can release it to the world!"

    return

label femalestart:
    "girly boy huh"
    jump askname
    return
    
    
label askname:
# The phrase in the brackets is the text that the game will display to prompt 
# the player to enter the name they've chosen.

    $ player_name = renpy.input("What is your name, Magical Boy?")

    $ player_name = player_name.strip()
# The .strip() instruction removes any extra spaces the player 
# may have typed by accident.

#  If the player can't be bothered to choose a name, then we
#  choose a suitable one for them:
    if player_name == "":
        $ player_name="Michael"

# And get a nostalgic sigh from Seasons of Sakura fans!
    
# Now the other characters in the game can greet the player.
  
    player2 "Pleased to meet you, %(player_name)s!"
    return

    
    
    
    
label answerdoor:
    menu:
        "open the door":
            jump answerpostman
        "ignore it":
            jump sleepyhead
    return