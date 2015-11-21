# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define player = Character('Protagonist', image="player", color="#c8ffc8")

image bg logo = "bg logo.png"

image side player avatar = "playeravatar.png"

init:
    image black = Solid((0, 0, 0, 255))
    image white = Solid((255, 255, 255, 255))
    image grey = Solid((128, 128, 128, 255))

# This is the splash screen. Should show my logo, and then the 
# instructions for playing on the Ouya.
label splashscreen:
#    show bg black
    $ renpy.pause(0)
    show bg logo
 #   with dissolve
#    with Pause (1.5)
    
#    show bg main_menu
    with dissolve
    with Pause(3)
    
    return    

# The game starts here.
label start:
    show bg logo with Pause (0.5)
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
