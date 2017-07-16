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

#alter before or alter after
class Parent(object):
    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"

        #call super with arguments Child and self. Then call the function altered on whatever it returns
        super(Child,self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()


#All three combined
class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

#Composition
class Other(object):

    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

Class Child(object):

def __init__(self):
    self.other = Other()

def implicit(self):
    self.other = implicit()

def override(self):
    print "CHILD override()"

def altered(self):
    print "CHILD BEFORE OTHER altered()"
    self.other.altered()
    print "CHILD, AFTER OTHER altered()"



son = Child()

son.implicit()
son.override()
son.altered()
