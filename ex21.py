def add(a, b):
    print "ADDING %d + %d" %(a , b)
    return a + b

def subtract(a ,b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a -b

def mutiply(a, b):
    print "MUTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" %(a, b)
    return a / b
print "Let's do some math with just funtions"

age = add(30, 5)
heigth = subtract(78, 4)
weigth = mutiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Heigth: %d, Weigth: %d, IQ: %d" %(age, heigth, weigth, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(heigth, mutiply(weigth, divide(iq,2))))

print "That becomes: ", what, "Can you do it by hand?"