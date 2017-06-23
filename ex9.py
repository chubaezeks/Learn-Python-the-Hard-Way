days = "Mon Tue Wed Thur Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApril\nMay\nJun\nJuly\nAugust\nSept"

print "Here are the days:", days
print "Here are the months:", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

test1="I am 6'2\" tall."
test2='I am 6\'2" tall.'

tabby_cat ="\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


beast_mode = """
This month, I'll:
\v* Exercise every day
\v* Journal everyday
\v* Think more ambitiously
"""

print beast_mode


beast_mode = """
This month, I'll:
\f* Exercise every day
\f* Journal everyday
\f* Think more ambitiously
"""

print beast_mode

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you are %r old, %r tall and %r heavy." % (age, height, weight)
