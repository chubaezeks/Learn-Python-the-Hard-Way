from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement "
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play (self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_map(next_scene_name)

            #be sure to print out the last scene
            current_scene.enter()

class Death(Scene):


    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons of Planet percal #25 have invaded your ship and destroyed"
        print "your entire crew. You are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapon Amory,"
        print "put it in the bridge, and blow the ship up after getting into an"
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Amory when "
        print "a Gothon jumps out, red scaly skin, dark grimy teerh, and evil clown co"
        print "stume"
        print "flowing around his hate filled body. He's blocking the door to the"
        print "Amory and about to pull a weapon to blast you."

        action = raw_input(">")

        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at ease"
            print "His clown costume is flowing and moving around his body"
            print "Off your aim. Your laser hits his costume but misses him"
            print "completely ruin his brand new costume his mother bought and"
            print "make him fly into an insane rage and blast you repeatedly till"
            print "you're dead. Then he eats you."
            return 'death'

        elif action == "dodge!":
        print "Like a world class boxer you dodge, weave, slip and slide right"
        print "as the Gothon's blaster cranks a laser past your head."
        print "In the middle of your artful dodge your foot slips and you"
        print "band your head on the metal wall and pass out."
        print "You wake up shortly after only to die as the Gothon stomps on"
        print "your head and eats you."
        print "Your mom would be proud....if she were smarter."

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'
            


class laserWeaponAmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
