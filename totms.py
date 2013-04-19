from sys import exit
#from random import randint

choice_count = 0


def dowhat(list):
    """
    Prompts the user for what they want to do next
    """
    print "What do you want to do?"
    i = 0
    while i <= len(list) - 1:
        print "%d - " % (i + 1), list[i]
        i += 1


def cont(prompt):
    """
    Prompt user to continue.
    If passed 0 (True),  then display the prompt
    If passed 1 (False), then don't display a prompt
    but still require input to continue.
    """
    if prompt == 0:
        raw_input("Continue...")
    elif prompt == 1:
        raw_input("")
    else:
        exit(1)
        #("Error: Out of Bounds variable in function 'cont'.")


def dummy(action, go, count):
    """
    Chastizes the user for not picking a valid choice
    """
    choices = [
        "Perhaps you should try reading for a change.",
        "Look - see the numbers there?  Just pick one.",
        "What is wrong with you?  Do you have a head injury?",
        "You're just screwing with me now, aren't you?",
        "Come on, don't be a jerk."
        "Fine, screw you too."]

    my_choice = choices[count]

    global choice_count

    print "'%r' is not a choice." % action

    if choice_count <= 3:
        print my_choice
        choice_count += 1
    else:
        return 'death'


class Scene(object):

    def enter(self):
        print """
        The storyteller is to lazy to have imagined this room yet.  He's
        probably outside asleep in the bushes somewhere.  Maybe you should
        go look for him and give him a swift kick in the butt.
        """
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):

    def enter(self, my_choice):
        print "You chose to %r" % my_choice
        print "It doesn't work out for you..."
        print "You have died."
        exit(1)


class Logo(Scene):

    def enter(self):
        """
        The Logo of the Tomb of the Mud Sorcerer
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

        cont(1)
        return 'outside'


class Outside(Scene):

    def enter(self):
        """
        LOCATION 001
        ------------
        """

        print """
        Before you stands the entrance to the tomb of the Mud Sorcerer, ancient
        evil from times past.  Hundreds have entered and dozens left the tomb
        since it's discovery fourty years ago, leaving room looted and
        vandalized.  Yet so little was found in the last resting place of such
        a powerful man that rumors abound of hidden rooms and fabulous wealth
        lost in the tomb.

        And so you stand, nervous and excited, before the tomb,
        ready to seek your fortune at last.
        """

        dowhat(["Enter the Tomb",
                "Look around outside",
                "Chicken out and go home instead..."])

        action = raw_input("> ")

        if action == "1":
            return 'narthex'
        elif action == "2":
            return 'bushes'
        elif action == "3":
            return 'chicken_out'
        else:
            dummy(action, 'outside', choice_count)


class Narthex(Scene):

    def enter(self):
        print "Not implemented"


class RightAlcove(Scene):

    def enter(self):
        pass


class LeftAlcove(Scene):

    def enter(self):
        pass


class Nave(Scene):

    def enter(self):
        pass


class Apse(Scene):

    def enter(self):
        pass


class ChickenOut(Scene):

    def enter(self):
        pass


class Map(object):

    scenes = {
        'logo': Logo(),
        'outside': Outside(),
        'narthex': Narthex(),
        'right_alcove': RightAlcove(),
        'left_alcove': LeftAlcove(),
        'nave': Nave(),
        'apse': Apse(),
        'chicken_out': ChickenOut(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('logo')
a_game = Engine(a_map)
a_game.play()
