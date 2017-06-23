
# What about if there was a way we could make this code a lot shorter?
# So we change the order of things? Instead of having them choose to be creatures first, they should choose good or bad
# And if they choose good or bad, they then get the option to choose to be a warrior or magician, then choose race last.
# This way, we streamline the tree the right way
# so def type first, then def occupation then def race

from sys import exit


def race():
    print "You can choose to be human, elf or dwarf. Choose wisely."
    choice = raw_input(">")

    if choice == "human":
        print "Commendations. You have chosen to remain as you are. \n Blessed with the gift of numbers and resourcefullnes, you will thrive."

    elif choice == "elf":
        print "Great choice. You get to have long life and dashingingly good looks. Plus pointed ears."

    elif choice == "dwarf":
        print "Not a bad choice. You get to be mad wealthy with a crap ton of Gold. Means you live underground though."


def role():
    print "You can choose to be a warrior or a magician. Never both. Which do you choose?"
    choice = raw_input(">")

    if choice == "warrior":
        h_abilities = ["resourcefulness", "strength", "number"]
        print "You've been imbibed with the following abilities: %s" % h_abilities
        race()

    elif choice == "magician":
        m_abilities = ["intelligence", "magic", "lifespan"]
        print "You've been imbibed with the following abilities: %s" % m_abilities
        race()


def dead(why):
    print "Good job! NOT!", why
    exit(0)

def wow():
    print "What path do you choose to walk? Light or Darkness?"

    choice = raw_input(">")

    if choice == "light":
        print "The path of light is difficult and long, but rewarding. "
        role()

    elif choice == "darkness":
        print "Beware the path of darkness. For it bringeth temporary satisfaction and then doom. "
        role()

    else:
        dead("This is like a cliche movie. You're good or bad. Can't be both!")

wow()

#   The next step is to think about what else I can add to this to make it even more robust? What have I learnt that I'm not applying?
