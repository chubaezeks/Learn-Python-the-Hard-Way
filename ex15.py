#Reading Files

#This pulls in the argument variable
from sys import argv

#Unbundle the argument variable to get the filename
script, filename = argv

#defines the variable by the action to open the file
txt = open(filename)

#Combines a string with the file
print "Here's your file %r:" % filename

#The .read defines action taken on the text in the file, in this case, read.
print txt.read()

#This provides a prompt to pull in the file
print "Type the filename again:"
file_again = raw_input(">")

#If I was asked to open text within a textfile in a python environment, what would be my steps?
