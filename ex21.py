def add(a,b):
    print "ADDING %d + %d" % (a,b)
    return a + b


def subtract(a,b):
    print "SUBTRACTING %d - %d" % (a,b)
    return a - b

def multiply(a,b):
    print "MULTIPLY %d * %d" % (a,b)
    return a * b

def divide(a,b):
    print "DIVIDE %d / %d" % (a,b)
    return a / b

print "Let's do some maths with just functions!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here's a puzzle."

what = add(age, subtract(height,multiply(weight,divide(iq,2))))

print "That becomes:", what, "Can you do it by hand?"


# This involves having the numerator and denominator in two definitions. Then
# create a third for divide and run the two definitions  division(addition, subtraction)

num = add(24,34)
den = subtract(100,1023)
solution = divide(num,den)

print "The answer is:", solution
