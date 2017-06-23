#A bit unclear on what the argument variable does. Oh, so it lists the possible arguments present in the list. so a sys one should have the defaults or basics
from sys import argv

#from this, create a script
script, filename = argv

#This gives you the instruction on what we'll be printing
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL_C (^C)."
print "If you do want that, hit RETURN."

#raw_input allows you make the choice about what you'd want to do
raw_input("?")

#In order for you to proceed, you have to open the document that'll let you make changes. The target command does that.You appaz can't make any modifications without confirming that you want to by doing target = open(filename, 'w')
print "Opening the file..."
target = open(filename,'w')

#Once the file is loaded on python, you can use the target.truncate() command to delete the content
print "Truncating the file. Goodbye!"
target.truncate()


print "Now I'm going to ask you for three lines."

#Create new lines within the same file we just loaded. But rather than hardcode then, ask for frontend input through the raw_input command
line1 = raw_input("line 1: ") #So I'm just realising that we can run a script within the raw_input command
line2 = raw_input("line 2:") #I have to remember that with script, you add the quotes.
line3 = raw_input("line 3:") #I assumed that it would only be a placeholder.

print "I am going to write to the file."

#these are the commands that then write the lines into the document.
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

#Now I have to figure out how to reduce the codes so its a lot shorter. Figured it out, but not exaclty clear on what the role of the \n does.


print "And finally, we close it."
target. close()
