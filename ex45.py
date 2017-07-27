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
    pass

class Winterfell(Scene):
    pass

class IronIslands(Scene):
    pass

class KingsLanding(Scene):
    pass

class Map(object):
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('WesterosRoad')
a_game = Engine(a_map)
a_game.play()
