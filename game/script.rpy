# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define pov = DynamicCharacter("pov_name", image="pov", color="#D373CA")
define postman = Character('Protagonist', image="player", color="#c8ffc8")

image logo = "logo.png"

image side pov avatar0 = "avatar0.png"

init:
    image black = Solid((0, 0, 0, 255))
    image white = Solid((255, 255, 255, 255))
    image grey = Solid((128, 128, 128, 255))

# This is the splash screen. Should show my logo, and then the 
# instructions for playing on the Ouya.
label splashscreen:
    show logo
    with dissolve
    with Pause(5)
    return    

# The game starts here.
label start:
    show logo with Pause (1.5)
    scene black with dissolve
    show text " Finally Weekend! \n\n Unfortunately u can't sleep anymore \n\n Time to get up " with Pause(4.5)
    scene black with dissolve
    jump askname
    return

label answerdoor:
    menu:
        "open the door":
            jump answerpostman
        "ignore it":
            jump sleepyhead
    return
    
label askname:
# The phrase in the brackets is the text that the game will display to prompt 
# the player to enter the name they've chosen.
    $ pov_name = renpy.input("What is your name, Magical Boy?")
    $ pov_name = pov_name.strip()
    
    if pov_name == "":
        $ pov_name="Michael"

# Now the other characters in the game can greet the player.
    pov avatar0 "test"
    postman "Pleased to meet you, [pov_name]!"

label getpackage:
    show logo
    pov "something something"
    pov avatar0 "now the avatar0 should show up"
    postman "well"
    pov "test"