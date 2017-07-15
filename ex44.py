  #Implicit Inheritance
#create class Parent with implicit function
  class Parent(object):

      def implicit(self):
          print "PARENT implicit()"

#create class Child & have only pass as a placeholder
#This means that the child inherits the behaviour of the parent
class Child(Parent):
        pass
#create aliases for the classes
dad = Parent()
son = Child()

#This is where it finally clicked for me!
#This tells the code to run implicit function from the parent class, now with alias dad
dad.implicit()
son.implicit()
