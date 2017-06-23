def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)


#simplier way to print this
def print_two_again (arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1,arg2)

#if you want to print one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# If you want to print a function with no argument
def print_none():
    print "I got nothin'."

print_two ("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
