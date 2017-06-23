print "You're faced with 3 scenarios, which one do you pick? Scenario #1, #2, #3"

scenario = raw_input(">")

if scenario == "1":
    print "You're offered a job by Apple, Facebook or Google?"

    company = raw_input(">")

    if company == "Apple":
        print "Well, good luck dealing with their attitude."
        print "Wait, how much are they gonna pay you? 10k, 20k or 50k?"

        pay = raw_input(">")

        if pay == "10k":
            print "Damn. That's low as fuck mate"
        elif pay == "20k":
            print "Kai. Still kinda low for Apple no?"
        elif pay == "50k":
            print "Not bad at all. Entry level for tech, but not bad."
        else:
            print "Good stuff mate. Make that money fam!"

    elif company == "Facebook":
        print "Not bad. You get to hang out with Mark & steal Snap's ideas."
    elif company == "Google":
        print "Well done. Get ready to learn a lot of machine learning."

elif scenario == "2":
    print "You see a girl you find really attractive. What do you do?"
    print "1. Walk up to her and ask for her number."
    print "2. Ask her friend to ask for her number."
    print "3. Be shy and ignore her."

    decision = raw_input(">")

    if decision == "1":
        print "She nails you or she agrees to give you her number. Well done!"
    elif decision == "2":
        print "Her friend calls you a pussy or she calls you herself. Lmao!"
    else:
        print "You end up a lonely fucker. lmao!"
