# Learn Prompting and Passing

from sys import argv

script, user_name, nickname  = argv
prompt = '~'

print "Hi %s, I'm the %s script. I take it I can call you by your nickname %s?" % (user_name, script)
print "I'd like to ask you a few questions."

print "Do you like me %s? or should I say %s" %(user_name, nickname)
likes = raw_input (prompt)

print "Where do you live %s?" % (user_name, nickname)
lives = raw_input (prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
