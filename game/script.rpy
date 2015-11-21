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
 #   $ pov_name="temp"
    show logo with Pause (1.5)
    scene black with dissolve
    show text " Finally Weekend! \n\n Unfortunately u can't sleep anymore \n\n Time to get up " with Pause(4.5)
    call leavebed
    call stairs
    call answerdoor
    return

label leavebed:
    return
   
label stairs:
    return

label answerdoor:
    menu:
        "open the door":
            call getpackage
        "ignore it":
            call soory
    return

label getpackage:
    postman "Hello, here´s your Mail. Sign this please."
    call askname
    return
    
label sorry:
    "soory, this path isnt finished yet"
    return