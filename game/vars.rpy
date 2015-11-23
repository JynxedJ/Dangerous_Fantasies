label pov_askname:
# The phrase in the brackets is the text that the game will display to prompt 
# the player to enter the name they've chosen.
    $ pov_name = renpy.input("Recipient:")
    $ pov_name = pov_name.strip()
    
    if pov_name == "":
        $ pov_name="Michael"

# Now the other characters in the game can greet the player.
#   "example-> hello [pov_name]"
    return
    
label pov_sissy:
    if pov_sissy <= -1:
        $ pov_gender = "male"
        $ pov_endearment = "Son"
    elif pov_sissy >= 1:
        $ pov_gender = "female"
        $ pov_endearment = "Darling"
    else:
        $ pov_gender = ""
        $ pov_endearment = ""
    return