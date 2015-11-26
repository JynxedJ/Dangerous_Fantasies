label pov_askname:
    $ pov_name = renpy.input("Recipient:")
    $ pov_name = pov_name.strip()
    if pov_name == "":
        $ pov_name="Mika"
    return
    
label pov_sissy:
    if pov_sissy <= -1:
        $ pov_gender = "Male"
        $ pov_endearment = "Son"
    elif pov_sissy >= 1:
        $ pov_gender = "Female"
        $ pov_endearment = "Darling"
    else:
        $ pov_gender = ""
        $ pov_endearment = ""
    return

label pov_gender:
    if pov_gender == "":
        $ pov_gender = "Male"
    elif pov_gender == "Male":
        $ pov_gender = "Female"
    elif pov_gender == "Female":
        $ pov_gender = "Male"
    else:
        $ pov_gender = "Error"