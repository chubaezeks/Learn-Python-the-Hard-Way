from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print "This scene has not been configured. Subclass and implement enter()"
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "n\-----"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

    # create a list with words to be said when the character dies
    quips = [
        "Vaga molorgus. All men must die...but gosh...you really deserved to die.",
        "Great job. Now you're one of the thousands that have perished in this war.",
        "Westeros is certainly better off now that you're gone."
        "Heard the white walkers are recruiting members. You might be more useful there."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class WesterosRoad(Scene):

    def enter(self):
        print "Tis the time for conquest. On the roads of Westeros your journey begins."
        print "You are Aegon Tagarean of the Dragons and you aim to conquer all that stands in your way"
        print "All that stands in your way are the Kingdoms in Weteros"
        print "Now you will make your hourney to conquer these kingdoms or you will perish along with your dragons."
        print "Which action will you take, proceed or decline?"

        action = raw_input(" > ")

        if action == "proceed":
            print "All men must die. Let's conquer!"
            print "You gather your armies of thousands ready to battle."
            print "You pay your sellswords and bribe them with women."
            print "You feed your dragons with 100s of lambs and get them ready to slaughter by fire."
            return 'winterfell'


        elif action == "decline":
            print "Craven! You gravely disappoint with your lack of a backbone"
            print "Run down to a pub and drown your cowardice in a pool of alcohol"
            print "At that pub, a sellsword steals your money and stabs you to death"
            return "Death"

        else:
            print "DOES NOT COMPUTE"
            return 'Westeros'



class Winterfell(Scene):
        print "Welcome to the North, thou of dragon blood."
        print "Thou wishest to take over, but we shall guard our kingdom to the end"
        print "This we swear on the old Gods."
        print "We shall give you two options, turn around or meet your death."


        def fight(self):
            print "You ready your men for battle, but you have to ready your dragons."
            print "They've been chained in the tower, and to release them you have to unlock the cell"
            print "There are two keys, No 24 and 47 - and you can only choose one."
            print "If you choose the wrong one, there will be dire consequences"
            box = [24,47]

        key = raw_input("> ")

            if key == "47" in box:
                print "Phew. You took the right key! Unlock the dragons and make the sky burn red with fire."
                return 'ironislands'

            elif key == "24" in box:
                print "Damn. That was the wrong key. Now the dragons are pissed and will proceed to burn you to a crisp."
                return 'death'

            else key !== "24" in box or "47" in box:
                print "You didn't take any of the keys. What the fuck is wrong with you."
                print "The dragons are disappointed in you and will proceed to burn you to a crisp."
                return 'death'


class IronIslands(Scene):
    print "Welome to the Iron Island. All we have to offer you is salt sea, rocks and death."
    print "What is dead may never die."
    print "If you choose to live, leave now and we shall offer you safe passage, "
    print "if you choose to fight, you shall perish."


    def enter(self):
        print "Your dragons will be instrumental in this war against wooden ships."
        print "You can choose to command or dismiss your dragons."

        action = raw_input(" > ")

        if action == "command":
            print "The dragons swoop down and burn the ships of ironborn."
            print " Upon defeat, the king of the IronIslands bends his knee to you."
            return 'kingslanding'

        elif action == 'dismiss':
            print "You dismiss your dragons and attempt to leave"
            print "The ironborn have never been true to their words"
            print "so they stab you in the back by sinking all your boats."
            return 'death'


class KingsLanding(Scene):
     print "You gather all the swords from the kingdoms"
     print "Then have your dragons melt and mould them into a throne made entirely of swords."
     print "Congratulations, you have won the game of Thrones."
     return exit


class Map(object):
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

ironisland = IronIslands(Scene)
kingslanding = KingsLanding(Scene)
winterfell = Winterfell(Scene)

a_map = Map('WesterosRoad')
a_game = Engine(a_map)
a_game.play()
