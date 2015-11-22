# Declare characters used by this game.
define pov = DynamicCharacter("pov_name", image="pov", color="#D5A7B9")
define narrator = Character(None, window_left_padding=160)
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

# This is the splash screen. Should show my logo
label splashscreen:
    show bg logo
    with dissolve
    with Pause(5)
    return    

# The game starts here.
label start:
    $ pov_name = "You"
    show bg logo with Pause (1)
    scene black with dissolve
    centered " Finally Weekend! \n\n If only that stupid noise would shut up "
    play sound "sounds/bell.mp3"
    centered " Damnit.. That annoying Doorbell! \n\n Most likely the Mailman.. \n\n Got to get up "
    scene bg bed with dissolve

    menu:
        "I better go open that Door":
            scene bg stairs with dissolve
            play sound "sounds/bell.mp3"
            pov "YES! I´M COMING!"
            menu:
                pov "Ouch! What the..."
                "Reposition my Morning-Wood":
                    $ pov_gender = "male"
                "Fingercomb that knot in my Bedhair":
                    $ pov_gender = "female"
            call mailman

#       TODO: add lazier path
#        "Nope! I´ll keep hugging the Pillow to Death":
#            jump end

    "Dressed in my Pyjamas I head downstairs"


    call end
    return

    
    
    
    
    
    
label mailman:
    scene bg mailman with dissolve
    mailman "Hello, I´ve got some Mail for you. Just need you to sign here."
    call pov_askname
    "It was quite a Challenge, but I managed to write my Name on his weird Handheld-Device"
    "Noone will ever have a Reason to decipher the Scribbles to find out that it means '[pov_name]' \ninstead of AlkjD0voi VweidDnqle"
    "Doesnt matter now anyway since I´ve got my Package.. Just got to hunt down some Scissors to open it"
    return

label intro_end:
    menu:
        "End of the Intro. Would you like to save the Character?"
        "Yes.":
              $ renpy.game_menu("save_screen")
        "No.":
              pass
    return

label end:
    scene black with dissolve
    centered "Congratz.. youve reached the end.. \n\n soory if it happened on an unfinished path.. this is still a work in progress \n\n\n If you like u can follow the Development on \n https://github.com/JynxedJ/Dangerous_Fantasies \n\n I´m using www.renpy.org ´s engine for this creation"

    menu:
        "open website":
            call openwebsite
        "dont":
            "done"
    
    return