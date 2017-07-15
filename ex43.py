
#Commands to import modules
from sys import exit
from random import randint

#Create scene class has a enter function that takes self parameter
class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement "
        exit(1)

#Class Engine class has an __init__ that takes self and scene_map parameters
class Engine(object):

    def __init__(self, scene_map):
#Get self from scene_map and set it to scene_map
        self.scene_map = scene_map

    def play (self):
#Get self attribute from the an instance of class opening_scene
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

#Create while loop indicating that when current_scene isn't equal to last_scene
#set nsn to an attribute of the instance of class enter()
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_map(next_scene_name)

            #be sure to print out the last scene
            current_scene.enter()

#This is the first scene we create
#Get scene from class death
class Death(Scene):

#crate list for quips
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

#create corridor scene with a if-elif-else scenarios
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


#Make the task to get the bomb interesting by introducing a guess game
class laserWeaponAmory(Scene):

    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan "
        print "for more Gothons that might be hiding. It's dead quet, too quiet"
        print "You stand up and run to the far side of the room and find the "
        print "neutron bomb in its container. There's a keypad lock on the door"
        print "and you need the code to get the bomb out. If you get the code"
        print "wrong 10 times then the lock closes forever and you can't"
        print "get the bomb. The code is 3 digits."
        #use that module randint to create a randomised code
        code = "%d%d%d" % (rand(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]>")
        #start guesses at 0, so subsequent can follow after
        guesses = 0

        #I had no idea you could run several conditions in a loop!
        #so here's a while loop for when the guess isn't correct and less than 10
        while guess != code and guesses < 10:
            print "BZZZZED!"
            guesses = +1
            guess = raw_input("[keypad]>")

        if guess == code:
            print "The container clicks open and the seal breaks, letting g"
            print "You grab the neuron bomb and run as fast as you can to the "
            print "bridge where you must place it in the right spot."
            return 'the_bridge'

        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from their ship and you die."
            return 'death'


class TheBridge(Scene):

    def enter(self):
            print "You burst onto the Bridge with the neutron destruct bomb"
            print "under your arm and surprise 5 Gothons who are trying to"
            print "take control of the ship. Each of them has an even uglier"
            print "clown costume than the last. They haven't pulled their"
            print "weapons out yet, as they see the active bomb under you"
            print "arm and don't want to set it off."


            action = raw_input(">")

            if action == "throw a bomb":
                print "In a panic you throw the bomb at the group of Gothons"
                print "and make a leap for the door. Right as you drop it a"
                print "Gothon shoots you right in the back killing you."
                print "As you die you see another Gothon frantically try to disable"
                print "the bomb. You die knowin they will probably blow up when"
                print "it goes off."
                return 'death'

            elif action == "slowly place the bomb:"
                print "You point your blaster at the bomb under your arm"
                print "and the Gothons put their hands up and start to sweat."
                print "You inch backward to the door, open it, and then carefully"
                print "place the bomb on the floor, pointing your blaster at it."
                print "You then jump back through the door, punch the close button"
                print "and blast the lock so the Gothons can't get out."
                print "Now that the bomb is placed you run to the escape pod to"
                print "get off this tin can."
                return 'escape_pod'

            else:
                print "DOES NOT COMPUTE"
                return "the_bridge"

class EscapePod(Scene):

    def enter(self):
        print "You rush throgh the ship desperately trying to make it to"
        print "the escape pd before the whole ship explodes. It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference. You get to the chamber with the escape pods,"
        print "now need to pick one to take. Some of them could be damaged."
        print "but you don't have time to look. There's 5 pods, which one"
        print "do you take?"

        good_pod = randint(1,5)
        guess = raw_input("[pod #]>")

        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return 'death'

        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below. As it files to the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, taking out the Gothon ship at the same"
            print "time. You won!"
            return 'finished'

class Finished(Scene):

        def enter(self):
            print "You won! Good job."
            return 'finished'


class Map(object):

#In the map, the scene classes are all placed in a dictionary
    scenes = {
    'central_corridor': CentralCorridor(),
    'laser_weapon_amory': laserWeaponAmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death': Death(),
    'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    #can't say I get why this is done
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
