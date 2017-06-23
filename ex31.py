print "You enter a dark room with two doors. Do you go through door #1 or door #2? or door #3"

door = raw_input (">")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."


    bear = raw_input(">")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear =="2":
        print "The bear eats your leg off. Good job!"
    else:
        print "Well., doing %s is better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input(">")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
    print "You see a girl you find really attractive. What do you do?"
    print "1. Walk up to her and ask for her number."
    print "2. Ask her friend to ask for her number."
    print "3. Be shy and ignore her."

    decision = raw_input(">")

    if decision == "1":
        print "She nails you or she agrees to give you her number. Well done!"
    elif decision == "2":
        print "Her friend calls you a pussy or she calls you one herself. Lmao!"
    else:
        print "You end up a lonely fucker. lmao!"

else:
    print "You stumble around and fall on a knife and die. Good job!"
