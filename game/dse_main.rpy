# This is the main program. This can be changed quite a bit to
# customize it for your program... But remember what you do, so you
# can integrate with a new version of DSE when it comes out.

# Set up a default schedule.
init python:
    register_stat("Strength", "strength", 0, 100)
    register_stat("Endurance", "endurance", 0, 100)
    register_stat("Charisma", "charisma", 0, 100)
    register_stat("Intelligence", "intelligence", 0, 100)
    register_stat("Agility", "agility", 0, 100)
    register_stat("Luck", "luck", 0, 100)

    dp_period("Morning", "morning_act")
    dp_choice("Attend Class", "class")
    dp_choice("Cut Class", "cut")
    
    # This is an example of an event that should only show up under special circumstances
    dp_choice("Fly to the Moon", "fly", show="strength >= 100 and intelligence >= 100")

    dp_period("Afternoon", "afternoon_act")
    dp_choice("Study", "study")
    dp_choice("Hang Out", "hang")

    dp_period("Evening", "evening_act")
    dp_choice("Exercise", "exercise")
    dp_choice("Play Games", "play")

    
# This is the entry point into the game.
label start1:

    # Initialize the default values of some of the variables used in
    # the game.
    $ day      = 4
    $ daynames = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Show a default background.
    scene black

    # The script here is run before any event.

    "In case you're just tuning in, here's the story of my life to
     date."

    "I'm a guy in the second year of high school."

    "I'm not good at sports or school or even something as simple as
     remembering peoples names."

    "In short, I am your usual random loser guy."

    "And this is my story..."


    # We jump to day to start the first day.
    jump day


# This is the label that is jumped to at the start of a day.
label day:

    # Increment the day it is.
    $ day += 1
    $ todays =  daynames[(day%7)]
    "It is day [day]. Today is [todays]."
    
    # Here, we want to set up some of the default values for the
    # day planner. In a more complicated game, we would probably
    # want to add and remove choices from the dp_ variables
    # (especially dp_period_acts) to reflect the choices the
    # user has available.

    $ morning_act = None
    $ afternoon_act = None
    $ evening_act = None
    $ narrator("What should I do today?", interact=False)

    # Now, we call the day planner, which may set the act variables
    # to new values. We call it with a list of periods that we want
    # to compute the values for.
    call screen day_planner(["Morning", "Afternoon", "Evening"])

    
    # We process each of the three periods of the day, in turn.
label morning:

    # Tell the user what period it is.
    centered "Morning"

    # Set these variables to appropriate values, so they can be
    # picked up by the expression in the various events defined below. 
    $ period = "morning"
    $ act = morning_act
    
    # Execute the events for the morning.
    call events_run_period

    # That's it for the morning, so we fall through to the
    # afternoon.

label afternoon:

    # It's possible that we will be skipping the afternoon, if one
    # of the events in the morning jumped to skip_next_period. If
    # so, we should skip the afternoon.
    if check_skip_period():
        jump evening

    # The rest of this is the same as for the morning.

    centered "Afternoon"

    $ period = "afternoon"
    $ act = afternoon_act

    call events_run_period


label evening:
    
    # The evening is the same as the afternoon.
    if check_skip_period():
        jump night

    centered "Evening"

    $ period = "evening"
    $ act = evening_act
    
    call events_run_period


label night:

    # This is now the end of the day, and not a period in which
    # events can be run. We put some boilerplate end-of-day text
    # in here.

    centered "Night"

    "It's getting late, so I decide to go to sleep."

    # We call events_end_day to let it know that the day is done.
    call events_end_day

    # And we jump back to day to start the next day. This goes
    # on forever, until an event ends the game.
    jump day
         

# This is a callback that is called by the day planner. 
label dp_callback:

    # Add in a line of dialogue asking the question that's on
    # everybody's mind.
    $ narrator("What should I do today?", interact=False)
    
    return

