## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
pass

## Class Dog is-a animal
class Dog(Animal):

def __init__(self, name):
    ## Class Dog has-a init that takes self and name parameters
self.name = name

## Class Cat is-a animal
class Cat(Animal):

def __init__(self, name):
    ## Class cat has-a init that takes self and name parameters
self.name = name

## Class Person is-a object
class Person(object):

    def __init__(self, name):
        ## Class person has-a init that takes self and name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Class employee is a person
class Employee(Person):

    def __init__(self, name, salary):
    ## class employee is a person that takes a self, name and salary parameters hmm what is this strange magic?
    super(Employee, self).__init__(name)
    ## super is-a employee that has-a init
    self.salary = salary


## class fish is an object
class Fish(object):
    pass

## class Salmon is-a fish
class Salmon(Fish):
    pass

## Class Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet that is-a satan
mary.pet = satan

## frank is-a employee
frank = Employee("Frank", 120000)

## frant has-a pet that is a rover
frank.pet = rover

##flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
