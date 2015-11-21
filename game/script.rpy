# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define pov = DynamicCharacter("pov_name", image="pov", color="#D373CA")
define mailman = Character('Mailman', image="player", color="#c8ffc8")

image bg logo = "logo.png"
image bg bed = "bed.jpg"
image bg stairs = "stairs.jpg"

image bg mailman = "mailman.jpg"

image side pov default = "avatar0.png"

init:
    image black = Solid((0, 0, 0, 255))
    image white = Solid((255, 255, 255, 255))
    image grey = Solid((128, 128, 128, 255))

# This is the splash screen. Should show my logo, and then the 
# instructions for playing on the Ouya.
label splashscreen:
    show bg logo
    with dissolve
    with Pause(5)
    return    

# The game starts here.
label start:
    $ pov_name = "You"
    $ pov_gender = "male"
    show bg logo with Pause (1)
    scene black with dissolve
    " Finally Weekend! \n\n If only that stupid noise would shut up "
    play sound "sounds/bell.mp3"
    " Damnit.. Its the Doorbell! \n\n Most likely the Mailman.. \n\n Time to get up "
    scene bg bed with dissolve

    menu:
        "I better go open that Door":
            scene bg stairs with dissolve
            play sound "sounds/bell.mp3"
            "YES! I´M COMING!"
            menu:
                pov "What the..."
                "Hide the Morning-Wood":
                    "still male"
                "Fingercomb your Bedhair":
                    $ pov_gender = "female"
            call mailman

#        "Nope! I´ll keep hugging the Pillow to Death":
#            jump end

    "Dressed in my Pyjamas I head downstairs"


    call end
    return

    
    
    
    
    
    
label mailman:
    scene bg mailman
    mailman "Hello, I´ve got some Mail for you. Just need you to sign here."
    call pov_askname
    "It was quite a Challenge, but I managed to write my Name on his weird Handheld-Device"
    "Noone will ever have a Reason to decipher the Scribbles to find out that it means '[pov_name]' \ninstead of AlkjD0voi VweidDnqle"
    "Doesnt matter now anyway since I´ve got my Package.. Just got to hunt down some Scissors to open it"
    return

label end:
    "Congratz.. youve reached the end.. soory if it happened on an unfinished path.. this is still a work in progress"
    return