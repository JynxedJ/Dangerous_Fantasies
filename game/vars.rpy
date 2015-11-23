label pov_askname:
    $ pov_name = renpy.input("Recipient:")
    $ pov_name = pov_name.strip()
    if pov_name == "":
        $ pov_name="Michael"
    return
    
label pov_sissy:
    if pov_sissy <= 0:
        $ pov_gender = "male"
        $ pov_endearment = "Son"
    elif pov_sissy >= 1:
        $ pov_gender = "female"
        $ pov_endearment = "Darling"
    else:
        $ pov_gender = ""
        $ pov_endearment = ""
    return