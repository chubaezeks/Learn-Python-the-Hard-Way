
class Scene(object):
    def enter(self):
        pass

class Engine(object):
    def __init__(self, scene_map):
        pass

class Death(Scene):
    pass

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
