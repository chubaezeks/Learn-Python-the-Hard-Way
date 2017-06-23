
#inches = 10.0
#centimeter = inches * 2.54
#print " %d inches converts to %d centimeter " %(inches, centimeter )

#kilograms=pounds/100
#print "%d pounds converts to %d kilograms" %(pounds,kilograms)

#Practice using relationship between variance and bias
term1 = "variance"
term2 ="bias"

print " The relationship between the %s and %s is based on the sample population" %(term1,term2)

#est out float elements
covariance= 20.0
stdev=8.0
corr= covariance/stdev
print "The correlation of two terms is derived by the division of the covariance with the stdev, i.e. %f divided by %f, this gets us %f " %(covariance, stdev,corr)

#This adds a value within a string
x = "There are %d types of people" % 10
#This creates a variable
binary = "binary"
do_not = "don't"
#This adds the strings into a string
y = "Those who know %s and those who %s." %(binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e



print "Mary had a little lamb."
print "Its fleece was as white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 #This replicates the period sign

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#The comma ensures both print lines end up on the same page
print end1 + end2 + end3 +end4 + end5 + end6,
print end7 + end8 + end9 +end10 +end11 +end12
