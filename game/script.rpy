# Declare characters used by this game.
define pov = DynamicCharacter("pov_name", image="player", color="#D5A7B9")
define narrator = Character(None, window_left_padding=160)
define mailman = Character('Mailman', image="player", color="#c8ffc8")

image bg logo = "logo.png"
image bg bed = "bed.jpg"
image bg stairs = "stairs.jpg"
image bg mailman = "mailman.jpg"
image bg bath = "bath.jpg"
image side playeravatar = ConditionSwitch(
                    "pov_gender == 'male'", "avatarm0.png",
                    "pov_gender == 'female'", "avatarf0.png",
                    "True", "avatar0.png")

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
    $ pov_name = ""
    $ pov_gender = ""
    
    show bg logo with Pause (1)
    scene black with dissolve
    centered " Finally Weekend! \n\n If only that stupid noise would shut up "
    play sound "sounds/bell.mp3"
    centered " Damnit.. That annoying Doorbell! \n\n Most likely the Mailman.. "
    scene bg bed with dissolve

    menu:
        "I better go open that Door":
            call mail_stairs

#       TODO: add lazier path
        "Nope! I´ll keep hugging the Pillow to Death":
            play sound "sounds/bell.mp3"
            menu:
                "Oh well..":
                    call mail_stairs
                "NOPE! Fuck off..":
                    jump end
#



    call intro_end
    call end
    return

    
    
    
label mail_stairs:
    narrator "Dressed in my Pyjamas I head downstairs"
    with vpunch
    scene bg stairs 
    with dissolve
    play sound "sounds/bell.mp3"
    narrator "YES! I´M COMING!"
    with vpunch
    call mailman
    return
    
label mailman:
    scene bg mailman with dissolve
    mailman "Hello, I´ve got some Mail for you. Just need you to sign here."
    call pov_askname
    pov playeravatar "It was quite a Challenge, but I managed to write my Name on his weird Handheld-Device"
    pov "Noone will ever have a Reason to decipher the Scribbles"
    pov "Really doesnt matter now since I´ve got my Package.."
    scene bg stairs with dissolve
    pov playeravatar "It should´ve been here yesterday, but now that I´ve got it I´m going to spend the whole Day reading the new Book in Bed"
    pov "But first things first.. Off to the Toilet"
    call toilet
    return

label toilet:
    scene bg bath with dissolve
    menu:
        "Just whip it out and aim":
            $ pov_gender = "male"
        "Sit down to pee":
            $ pov_gender = "female"
    pov playeravatar "player x"
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
    scene white
    pov playeravatar " Variables: \n\nName: [pov_name]\nGender: [pov_gender]"
    centered "  THE END  \n\n soory if it happened on an unfinished path.. this is still a work in progress \n I´m using www.renpy.org ´s engine for this creation"
    return