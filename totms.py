# MiniPyAdventure
#
# A 'Choose Your Own Adventure'-style game written in Python.
#
# This game was written for Exercise 36 of 'Learn Python The Hard Way':
# http://learnpythonthehardway.org/book/ex36.html
#
#

import os
from sys import exit


def startgame(firsttime):
    if  firsttime == "yes":
        os.system('clear')
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

        """
    else:
        print "\t*****\n"
        print "\tBack again, eh?\n\n"
        raw_input("Continue...")

    print """
    \tBefore you stands the entrance to the tomb of the Mud Sorcerer,
    ancient evil from times past.  Hundreds have entered and left the tomb
    since it's discovery fourty years ago, leaving the rooms looted and
    vandalized.  Yet so little was found in the last resting place of such
    a powerful man that rumors abound of hidden entrances and fabulous wealth
    lost in the tomb.\n\n\tAnd so you stand, excited to be searching for your
    fortune at last...\n\n
    """

    print "What do you do?\n"
    print "1. Enter the Tomb"
    print "2. Look around first"
    print "3. Chicken out and go home instead..."
    print ""

    while True:
        next = raw_input("> ")

        if next == "1":
            print "\nYou decide to enter the Tomb.\n"
            raw_input("Continue...")
            main_entrance()
        elif next == "2":
            print "\nYou decide to look around first.\n"
            raw_input("Continue...")
            lazy_storyteller(startgame, 'no')
        elif next == "3":
            print "\nYou decide to Chicken out and go home instead...\n"
            raw_input("Continue...")
            chicken_out()
        else:
            print "That's not a choice."


def main_entrance():

    lazy_storyteller(startgame, 'no')


def lazy_storyteller(go_where, opt):
    os.system('clear')
    print """
    \tRight now the story teller is lazy.  (You can see him
    sleeping off to the side of the entrance, next to some bushes).
    Otherwise, he's not thought of anything for you to see yet.\n
    """

    print "\tMight as well start out at the beginning, again.\n"

    go_where(opt)


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


def dead(why):
    print why, "\tYou have died."
    print "\tThank you for playing."
    exit(0)


startgame("yes")
