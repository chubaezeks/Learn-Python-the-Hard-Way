#Here we defined the function by two (not sure what to call them)
def cheese_and_crackers (cheese_count, boxes_of_crackers):
    print "You have %d cheese!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

#We take that function and give it a number directly, so no need to define what's in the function
#Just give the function numbers
print "We can just give the funtion numbers directly:"
cheese_and_crackers (20,30)

#We can also create variables that contain numbers
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#Then run the function by those variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Or we can run calculations within the function too
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 +6)

#Remember those variables we created earlier? We can also include them in the function
#as well as numbers to run calculations
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def me_and_you (chuba,mo):
    print "You love %d" % chuba
    print "I love %d" % mo
    print "We both love each other.\n"

print "We can represent ourselves as numbers!:"
me_and_you (100,100)

print "We can add variables and use it within the function:"
half_of_me = 0.5
half_of_you = 0.5

print " Let's work the math of both of us:"
me_and_you (25+25, 25+25)

print " We combine numbers and variables to get more of us:"
me_and_you (half_of_me + 0.5, half_of_you + 0.5)

me= 10 +10
you=10+10

print "What other combination can we run?:"
me_and_you(half_of_me,half_of_you)

print "What happens when we make a family?:"
me_and_you(me + 1, you + 1)
