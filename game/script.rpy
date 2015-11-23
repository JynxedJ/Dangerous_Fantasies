# Declare characters used by this game.
define pov = DynamicCharacter("pov_name", image="player", color="#6c4382")
define narrator = Character(None, window_left_padding=155)
define mailman = Character('Mailman', image="player", color="#aabcc4")
define mom = Character('Mom', image="player", color="#FF1000")

image bg logo = "logo.png"
image bg bed = "bed.jpg"
image bg stairs = "stairs.jpg"
image bg mailman = "mailman.jpg"
image bg bath = "bath.jpg"
image bg kitchen = "kitchen.jpg"
image bg livingroom = "livingroom.jpg"
image bg frontdoor = "frontdoor.jpg"
image phone = "phone.png"
image package = "package.png"
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
    $ pov_msgs = 1
    $ pov_endearment = ""
    $ pov_sissy = 0
    $ mom_msgs = 0

    show bg logo with Pause (1)

#   TODO: comment out this menu before compiling a release
    menu:
        "start game":
            jump intro
        "test":
            jump test
    return

    
label intro:
    scene black with dissolve
    centered " Finally Weekend! \n\n If only that stupid noise would shut up "
    play sound "sounds/bell.mp3"
    centered " Damnit.. That annoying Doorbell! \n\n Most likely the Mailman.. "
    scene bg bed with dissolve

    menu:
        "I better go open that Door":
            call mail_stairs
            call mailman
            call toilet
            call unpack
            call kitchen

        "Nope! I´ll keep hugging the Pillow to Death":
            play sound "sounds/bell.mp3"
            menu:
                "Oh well..":
                    call mail_stairs
                    call mailman
                    call toilet
                    call unpack
                    call kitchen
                "NOPE! Fuck off..":
                    call gnight
                    call gmorning
                    call stairs
                    call toilet
                    call nomailman
                    call unpack
                    call kitchen
    call intro_end
    call end
    return
    
label gnight:
    scene black with dissolve
    call pov_sissy
    pov playeravatar "ZzZzZzZzZzZz..."
    return
    
label gmorning:
    scene bg bed with dissolve
    call pov_sissy
    pov playeravatar "Damn you Light.. and Blatter.."
    return
    
label mail_stairs:
    narrator "Dressed in my Pyjamas I head downstairs"
    call stairs
    play sound "sounds/bell.mp3"
    narrator "YES! I´M COMING!"
    return
    
label stairs:
    scene bg stairs with dissolve
    with Pause(1)
    with vpunch
    return
    
label mailman:
    scene bg mailman with dissolve
    mailman "Hello, I´ve got some Mail for you. Just need you to sign here."
    call pov_askname
    call pov_sissy
    pov playeravatar "It was quite a Challenge, but I managed to write my Name on his weird Handheld-Device"
    pov "Noone will ever have a Reason to decipher the Scribbles"
    pov "Really doesnt matter now since I´ve got my Package.."
    scene bg stairs with dissolve
    pov playeravatar "It should´ve been here yesterday, but now that I´ve got it I´m going to spend the whole Day reading the new Book in Bed"
    pov "But first things first.. Off to the Toilet"
    return

label nomailman:
    scene bg frontdoor with dissolve
    call pov_sissy
    pov playeravatar "Finally it´s here. The Package should´ve arrived yesterday."
    return
    
label toilet:
    scene bg bath with dissolve
    menu:
        "Just whip it out and aim":
            $ pov_sissy -= 2
            call pov_sissy
        "Sit down and check the Phone":
            $ pov_sissy += 1
            call phone
    return
    
label unpack:
    call pov_sissy
    pov playeravatar "Time to unpack my new Book"
    scene bg livingroom with dissolve
    show package at right with dissolve
    if pov_name == "":
        "Looks a little big, but here it says that it´s for me."
        call pov_askname
    menu:
        "Just rip it open...":
            $ pov_sissy -= 2
        "No need to make a mess. Use Scissors.":
            $ pov_sissy += 2
    return
    
label kitchen:
    scene bg kitchen with dissolve
    call pov_sissy
    pov playeravatar "Hmm.. Breakfast.. or just Snack?"
    menu:
        "Chips" if pov_sissy <=0:
            $ pov_sissy -= 3
        "Eggs and Bacon":
            $ pov_sissy -= 2
        " Make a Sandwich":
            $ pov_sissy -= 2
        "Smoothie" if pov_sissy >= 0:
            $ pov_sissy += 5
        "Jogurt":
            $ pov_sissy += 3
        "Some random Fruit":
            $ pov_sissy += 2
        "Something Sweet":
            $ pov_sissy += 2
    return

label intro_end:
    menu:
        "End of the Intro. Would you like to save the Character?"
        "Yes.":
              $ renpy.game_menu("save_screen")
        "No.":
              pass
    return

label phone:
    show phone with dissolve
    if pov_msgs == 0:
        "No News or Messages.. Boring"
    else:
        menu:
            "New Messages: [pov_msgs]":
                if mom_msgs == 0:
                    mom "G´Morning [pov_endearment]\nwhen are you coming over for Dinner tommorow?"
                    $ pov_msgs -= 1
                    $ mom_msgs += 1
                    menu:
                        "As ussual":
                            $ pov_sissy -= 2
                        "Sorry, I´m busy, I´ll have to skip it.":
                            $ pov_sissy -= 2
                        "Sorry, I´m busy, really miss you tho! Love you":
                            $ pov_sissy += 3
                        "I´ll be early, alright?\nWant to chat a little, but dont worry.\nNothing serious is going on.":
                            $ pov_sissy += 4
                    call pov_sissy
            # TODO:
            #"Social Media":
            #"Google":
            #"make selfie to check look" pov_sissy +++
    return
    
label end:
    scene white
    pov playeravatar " Variables: \n\nName: [pov_name]\nSissy-Score: [pov_sissy]"
    scene black
    centered "  THE END  \n\n soory if it happened on an unfinished path.. this is still a work in progress \n I´m using www.renpy.org ´s engine for this creation"
    return