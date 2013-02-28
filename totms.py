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

# Global vars that need to be set at the beginning of the game
choice_count = 0

# Start the game

def startgame(firsttime):
    if  firsttime == 0:
        os.system('clear')
        logo()
    else:
        print "\t*****\n"
        print "\tBack again, eh?\n\n"
        cont(0)

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

    dowhat()
    print "1. Enter the Tomb"
    print "2. Look around first"
    print "3. Chicken out and go home instead..."
    print ""

    while True:
        next = raw_input("> ")

        if next == "1":
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

    lazy_storyteller(startgame, 'no')


def entrance_look():
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

    dowhat()
    print "1. Enter the tomb"
    print "2. Wake up the storyteller"
    print "3. Chicken out and run away..."
    print ""

    while True:
        next = raw_input("> ")

        if next == "1":
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


def lazy_storyteller(go_where, opt):
    os.system('clear')
    print """
    \tRight now the storyteller is lazy.  (You can see him
    sleeping off to the side of the entrance, next to some bushes).
    Otherwise, he's not thought of anything for you to see yet.\n
    """

    print "\tMight as well start out at the beginning, again.\n"

    go_where(opt)


def wake_storyteller():
    os.system('clear')
    print """
    \tYou approach the storyteller.  The man is huge - easily well over
    six feet tall, and several hundred pounds.  An impressive beard graces
    his face.\n
    \tAs you reach forward with your boot, the storyteller suddenly wakes
    and screams!\n
    \tBrillian light pours from his eyes and mouth and shines from behind
    the prone figure.  A sound like none you've ever heard roars in your
    ears.\n
    \tThe storyteller slowly rises from the ground to float above you,
    arms and legs outstretched, with more of the brillian fire pouring
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
    print "Thanks for playing, though.\n"
    exit(0)


def dowhat():
    print "What do you do?\n"


def cont(i):
    if i == 0:
        raw_input("Continue...")
    elif i == 1:
        raw_input("")
    else:
        die("Error: Out of Bounds variable in function 'cont'.")


def badchoice(choice, count):
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


def die(why):
    print "Error:", why
    exit(1)

def logo():
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
