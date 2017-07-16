  #Implicit Inheritance
#create class Parent with implicit function
#Book example
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

#my example
class Country(object):
    def revenue(self):
        print "The country makes most of the money and the state makes some of it."

class State(Country):
        pass

country = Country()
state = State()

country.revenue(self)
state.revenue(self)

#Override Explicitly
class Parent(object):

    def override(self):
        print "PARENT override()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()
