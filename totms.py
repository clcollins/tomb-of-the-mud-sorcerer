# Tomb of the Mud Sorcerer
#
# A 'Choose Your Own Adventure'-style game written in Python.
#
# This game was written for Exercise 36 of 'Learn Python The Hard Way':
# http://learnpythonthehardway.org/book/ex36.html
#
# It is a work in progress, and will keep growing.
#
# Written by: Chris Collins <christopher.collins@duke.edu>
#
#

import os
from sys import exit

### Global vars that need to be set at the beginning of the game

# Last location is not yet implemented
last = "startgame"

# Sets the "bad choice count" for use in function 'badchoice'
choice_count = 0

# Turns are not yet implemented
turns = 0

## The Player's Inventory ##
gold = 0

# Torches are not yet implemented
torches = 3

# Food is not yet implemented
food = ["4 apples",
        "some hard rolls",
        "an eighth of a wheel of moldy cheese"]

inventory = ["a rusty old shortsword",
             "a too-large horned helmet",
             "battered brown boots",
             "hand-me-down clothes",
             "extra-itchy underwear"]

# Start the game


def startgame(firsttime):
    """
    LOCATION 000
    ------------
    Begins the game, prints the logo if it's the
    first time through, and chastizes you if it's not.
    """
    if  firsttime == 0:
        os.system('clear')
        logo()
    elif firsttime == 1:
        print "\t*****\n"
        print "\tBack again, eh?\n\n"
        cont(0)
    else:
        print ""

    print """
    \tBefore you stands the entrance to the tomb of the Mud Sorcerer,
    ancient evil from times past.  Hundreds have entered and left the tomb
    since it's discovery fourty years ago, leaving the rooms looted and
    vandalized.  Yet so little was found in the last resting place of such
    a powerful man that rumors abound of hidden entrances and fabulous wealth
    lost in the tomb.\n
    \tAnd so you stand, excited to be searching for your
    fortune at last...\n
    """

    dowhat(["Enter the Tomb",
            "Look around first",
            "Chicken out and go home instead..."])

    while True:
        next = raw_input("> ")
        if next == 'I' or next == 'i':
            list_inventory()
            startgame(2)
        elif next == 'Q' or next == 'q':
            chicken_out()
        elif next == "1":
            print "\nYou decide to enter the Tomb.\n"
            cont(0)
            main_entrance()
        elif next == "2":
            print "\nYou decide to look around first.\n"
            cont(0)
            entrance_look()
        elif next == "3":
            print "\nYou decide to Chicken out and go home instead...\n"
            cont(0)
            chicken_out()
        else:
            badchoice(next, choice_count)


def main_entrance():
    """
    LOCATION 001
    ------------
    """
    os.system('clear')
    print """
    \tYou duck quickly into the small opening that marks the entrace to the
    Mud Sorcerer's tomb.  Inside is a round, smallish room, musty smelling
    and damp.  A floor of rough-cut stone pavers stretches between walls of
    small, hand-sized bricks.\n
    \tThe walls were once painted with a wash of white plaster, though much
    has fallen.  You can just make out some images on the little intact
    plaster that remains.\n
    \tAnother small door with a stone lintel exits across the room from the
    entrance.\n
    \tOther than some leaves blown into the corner, the room is empty.\n
    """

    dowhat(["Go through the door",
            "Examine the walls",
            "Check out the leaves"])

    while True:
        next = raw_input("> ")
        if next == 'I' or next == 'i':
            list_inventory()
            main_entrance()
        elif next == 'Q' or next == 'q':
            chicken_out()
        elif next == "1":
            print "\nYou go through the small door"
            cont(0)
            burial_chamber()
        elif next == "2":
            print "\nYou decide to examine the walls"
            cont(0)
            os.system('clear')
            print """
    \tYou lean in closer to the walls, holding your torch close to make out
    the details of the ancient paintings.\n
    \tCovering what is left of the crumbling plaster, ocre beings alternately
    dance and prostrate themseles before what appears to be a giant.\n
    \tIn places, painted figures are crucified on giant black wheels, and
    raised to the tops of tall poles. Hundreds stand planted on the dark
    hills in the background. Elsewhere, frenzied beings flay the skin from
    the backs of others tied to standing triangle frames.\n
    \tAbove it all, the giant stands.\n
    \tRepeated over and over along the top and bottom of the paintings are
    strange words:\n\n
    \tMAG-KASSER E KAOLAN PATRECH MAG-KASSER E KAOLAN PATRECH MAG-KASSER\n
            """
            cont(0)
            main_entrance()
        elif next == "3":
            print "\nYou walk to the corner to examin the leaves"
            cont(0)
            os.system('clear')
            print """
            Leaves!  LEAVES!  LEEEAAAAVVVVEEESSS!!!!
            """
            main_entrance()
        else:
            badchoice(next, choice_count)


def entrance_look():
    """
    LOCATION 002
    ------------
    """
    os.system('clear')
    print """
    \tThe entrance to the Tomb of the Mud Sorcerer is unassuming for one who
    once ruled the better part of the kingdom with an iron fist of terror.\n
    \tDug into the hillside is a small entrance - an opening a head shorter
    than you stand. A rough-cut stone lintel supports the weight of the hill
    above. Nearby lies a broken stone disk that once covered the entrance.
    A few low shrubs and bushes struggle to live in the poor soil.\n
    \tThe moon waxes large through the thin clouds that smear the sky.
    It's cold light is enough for you to make out details of the
    scene.\n
    To one side, a slumbering lazy storyteller reclines under the branches
    of one of the larger bushes.\n
    """

    dowhat(["Enter the tomb",
            "Wake up the storyteller",
            "Chicken out and run away..."])

    while True:
        next = raw_input("> ")
        if next == 'I' or next == 'i':
            list_inventory()
            entrance_look()
        elif next == 'Q' or next == 'q':
            chicken_out()
        elif next == "1":
            print "\nYou enter the Tomb.\n"
            cont(0)
            main_entrance()
        elif next == "2":
            print "\nYou decide to prod the storyteller with your boot.\n"
            cont(0)
            wake_storyteller()
        elif next == "3":
            print "\nYou decide to run away like a scared little girl...\n"
            cont(0)
            chicken_out()
        else:
            print "That's not a choice."


def burial_chamber():
    """
    LOCATION 003
    -----------
    """
    lazy_storyteller(startgame, 1)

#########################
### ENDGAME functions ###
#########################


def wake_storyteller():
    """
    LOCATION 003
    ------------
    """
    os.system('clear')
    print """
    \tYou approach the storyteller.  The man is huge - easily well over
    six feet tall, and several hundred pounds.  An impressive beard graces
    his face.\n
    \tAs you reach forward with your boot, the storyteller suddenly wakes
    and screams!\n
    \tDazzling light pours from his eyes and mouth and shines from behind
    the prone figure.  A sound like none you've ever heard roars in your
    ears.\n
    \tThe storyteller slowly rises from the ground to float above you,
    arms and legs outstretched, with more of the brilliant fire pouring
    from palms and soles.  Around you stones pull free from the earth and
    rise into the air.  The ground cracks and splinters and the struggling
    local flora ignites in flame.\n
    \tThe noise grows - louder and louder until you feel you can no longer
    deal with the pain.\n
    \tThe floating figure gazes upon you, and slowly raises one hand
    to point directly at you.  The world is suddenly filled with
    the light of a thousand suns and then...\n
    """

    cont(0)
    dead("The storyteller vaporizes you for your arrogance.")


def chicken_out():
    os.system('clear')
    print """
    \tThe fear of the unknown is too much for you, and
    you turn around, head hung low, and return to your comfortable,
    safe, and above all, boring life on the farm.  So ends the
    non-career of an ordinary, unremarkable loser.\n
    """
    print "\tThanks for playing, though.\n"
    exit(0)


def dead(why):
    os.system('clear')
    print ""
    print "\t", why, "You are dead.\n"
    print "\tOH NOES!\n"
    cont(1)
    os.system('clear')
    print ""
    print "Thank you for playing:\n"
    logo()
    exit(0)

####################################################################
### Below here are meta-game functions - those that don't belong ###
### to a particular room or situation (ie. functional stuff).    ###
####################################################################


def dowhat(list):
    """
    Prompts user for what they want to do next.
    """
    print "What do you do?\n"
    i = 0
    while i <= len(list) - 1:
        print "%d -  " % (i + 1), list[i]
        i += 1
    print ""
    print "i - Check Inventory"
    print "q - Quit"
    print ""


def cont(i):
    """
    Prompt user to continue.
    If passed 0 (True),  then display the prompt
    If passed 1 (False), then don't display a prompt
    but still require input to continue.
    """
    if i == 0:
        raw_input("Continue...")
    elif i == 1:
        raw_input("")
    else:
        die("Error: Out of Bounds variable in function 'cont'.")


def list_inventory():
    print "\tGold:", gold, "\tTorches:", torches, "\n"
    print "\n\tFood:"
    i = 0
    while i <= len(food) - 1:
        print "\t*", food[i]
        i += 1
    n = 0
    print "\n\tStuff:"
    while n <= len(inventory) - 1:
        print "\t*", inventory[n]
        n += 1
    print ""
    cont(0)


def lazy_storyteller(go_where, opt):
    """
    A handler function to throw in for any options that are not yet
    coded into the game.  Takes the option "go_where" to specify
    where to return the player, and "opt" to pass any special options
    that the target of "go_where" might need.

    Example usage: lazy_storyteller(startgame, 1)
    """
    os.system('clear')
    print """
    \tRight now the storyteller is lazy.  (You can see him
    sleeping off to the side of the entrance, next to some bushes).
    Otherwise, he's not thought of anything for you to see yet.\n
    """

    print "\tMight as well start out at the beginning, again.\n"

    go_where(opt)


def badchoice(choice, count):
    """
    Error handling for bad input.  End game if user can't figure
    it out after 5 tries.
    """
    print "\t%r is not a choice.\n" % choice
    choices = [
        "\tPerhaps you should try reading for a change.\n",
        "\tLook - see the numbers?  Pick one, genius.\n",
        "\tYou're just screwing with me now, aren't you?\n",
        "\tCome on, don't be a jerk.\n",
        "Fine, screw  you too."]

    my_choice = choices[count]

    global choice_count

    if choice_count <= 3:
        print my_choice
        choice_count += 1
    else:
        cont(0)
        dead(my_choice)


def die(why):
    """
    Simple Error handler with exit 1 and error message
    Message is passed when function is called
    """
    print "Error:", why
    exit(1)


def logo():
    """
    The logo of the tomb of the Mud Sorcerer
    """
    print """
                  ______ __         ______              __
                 /_  __// /  ___   /_  __/___   __ _   / /
                  / /  / _ \/ -_)   / /  / _ \ /  ' \ / _ \\
                 /_/  /_//_/\__/   /_/   \___//_/_/_//_.__/

  *****************************  of the  ************************************
 __  __  _   _  ____    ____    ___   ____    ____  _____  ____   _____  ____
|  \/  || | | ||  _ \  / ___|  / _ \ |  _ \  / ___|| ____||  _ \ | ____||  _ \\
| |\/| || | | || | | | \___ \ | | | || |_) || |    |  _|  | |_) ||  _|  | |_) |
| |  | || |_| || |_| |  ___) || |_| ||  _ < | |___ | |___ |  _ < | |___ |  _ <
|_|  |_| \___/ |____/  |____/  \___/ |_| \_\ \____||_____||_| \_\|_____||_| \_\\

                                                                      v0.1
   """

startgame(0)
