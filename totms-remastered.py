# Attempting to implement Tomb of the Mud Sorcerer
# via object-oriented programming

from sys import exit
from random import randint

gameversion = "v0.2"
firsttime = 0


# The scene (room, event, etc)
class Scene(object):

    def enter(self):
        """
        A handler function to throw in for any options that are not yet
        coded into the game.  Takes the option "go_where" to specify
        where to return the player, and "opt" to pass any special options
        that the target of "go_where" might need.

        Example usage: lazy_storyteller(startgame, 1)
        """
        print """
        \tRight now the storyteller is lazy.  (If you looked, you could
        see him sleeping off to the side of the entrance, next to some
        bushes).\n\n

        He's not thought of anything for you to see here yet.\n\n

        Despite the fact that he's slumbering, he raises a hand and waves it
        dismissively at you!  There's a blinding flash of light and nausea
        like the night after your mom's two-day old tuna cassarole, and
        suddenly...!!!
        """
        return 'MainEntrance'

# The game engine
# TO DO:
# Implement:
#   Inventory: Gold, Food, Objects
#   Time: hunger, items that wear out, timelimit?


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.splash()

        while True:
            print "\n--------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):

    quips = [
        "You suck at this.",
        "My little sister is better at this than you are."
    ]

    def enter(self):
        print "You have died."
        print """
        This should be how you died, once the Storyteller figures out
        how to do it.
        """
        print Death.quips[randint(0, len(self.quips) - 1)]
        exit(0)


def dowhat(option, decision, goto):
    """
    Prompts user for what they want to do next.
    """
    print "What do you do?\n"
    i = 0
    while i <= len(option) - 1:
        print "%d -  " % (i + 1), option[i]
        i += 1
    print ""
    # Not Implemented:  print "i - Check Inventory"
    # Not Implemented:  print "q - Quit"
    # Not Implemented:  print ""
    while True:
        next = raw_input("> ")
        print decision[next - 1]
        return goto[next - 1]


class Splash(Scene):

    def enter(self):
        """
        The splash screen with the logo of the Tomb of the Mud Sorcerer
        """
        print"""
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

                                                                      %s
        """ % gameversion
        return 'Intro'


class Intro(Scene):

    def enter(self):
        """
        SCENE 001
        ---------
        Begins the game.  Chastizes you if it's not the first time through.
        """
        if firsttime == 1:
            print "\t ... \n"
            print "\t Back again, then?\n\n"
        else:
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
            "Chicken out and go home instead..."],
           ["You decide to enter the Tomb...",
            "You're going to look around some first...",
            "You decide you're not up to this, and go home..."],
           ["MainEntrance",
            "Outside",
            "ChickenOut"])


class ChickenOut(Scene):

    def enter(self):
        pass


class Outside(Scene):

    def enter(self):
        pass


class WakeStoryteller(Scene):

    def enter(self):
        pass


class MainEntrance(Scene):

    def enter(self):
        pass


class BurialChamber(Scene):

    def enter(self):
        pass


class Map(object):

    scenes = {
        'Splash': Splash(),
        'Intro': Intro(),
        'ChickenOut': ChickenOut(),
        'Outside': Outside(),
        'WakeStoryteller': WakeStoryteller(),
        'MainEntrance': MainEntrance(),
        'BurialChamber': BurialChamber(),
        'Death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('Splash')
a_game = Engine(a_map)
a_game.play()
