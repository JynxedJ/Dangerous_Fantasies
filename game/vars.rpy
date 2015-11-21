label askname:
# The phrase in the brackets is the text that the game will display to prompt 
# the player to enter the name they've chosen.
    $ pov_name = renpy.input("What is your name, Magical Boy?")
    $ pov_name = pov_name.strip()
    
    if pov_name == "":
        $ pov_name="Michael"

# Now the other characters in the game can greet the player.
    "It was quite a Challenge, but you managed to write on his Handheld-Device"
    "Noone will ever have a Reason to decipher the Scribbles to find out that it means '[pov_name]' \ninstead of AlkjD0voi VweidDnqle"