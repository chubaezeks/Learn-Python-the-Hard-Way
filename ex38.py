ten_things = "Apple Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

#This takes the function and splits every word into a list
# stuff = ten_things.split(" ")

stuff =ten_things.split(' ')

#create a new list
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#The while loop allows us run a loop till the condition is met
#The condition is that the length of the string be 10
while len(stuff) != 10:

#create new function that takes element from the new list
#and runs it using the .pop() function.

    next_one = more_stuff.pop()

#We can then tell what gets added when we print
#so it loops over this until it gets to the last one
#Then
    print "Adding:", next_one

#We can use the append argument to add each of the strings we just took out to the old list
    stuff.append(next_one)

#This prints the number of items in the list after its run the loop
    print "There are %d items now." % len(stuff)

#Once the while loop is done running, we print to see the new contents of the old list
print "There we go:", stuff

print "Let's do some things with stuff."

#This gets out the second item in the list
print stuff[1]
#This gets out the last item in the list
print stuff[-1] #whoa! fancy
#This takes the last item out the list and shows it.
print stuff.pop()
#This asks us to place nothing between the items on the list
print ''.join(stuff) #what? cool!
#This asks us to join everything in the list using the # in the middle
#However, it only takes from 3-6 and not 7
print '#'.join(stuff[3:7]) #super stellar


#Practicing len() to see how it works
str = "I love to get on...I love to get too on!"

print "String length:", len(str)
