# Adding a Website Link to the main menu
#
#
# this has to be added to "screen main_menu:" in your screens.rpy
# textbutton _("Website") action Jump("openwebsite")

init:
    $ import webbrowser

label openwebsite:
    $ webbrowser.open("https://github.com/JynxedJ/Dangerous_Fantasies")
    call screen main_menu
    return