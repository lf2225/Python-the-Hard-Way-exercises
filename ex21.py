def add(x, y):
	print "ADD %d + %d" % (x, y)
	return x + y

def sbtkt(x, y):
	print "SUBTRACT %d minus %d" % (x, y)
	return x - y

def multiply(x, y):
	print "multiply %d times %d" % (x, y)
	return x * y

def divd(x, y):
	print "divide %d by %d" % (x, y)
	return x / y

def mod (x, y):
	print "%d mod %d" % (x, y)
	return x % y

print "Let's do some math with just functions!"

age = add(30, 5)
height = sbtkt (78, 4)
weight = multiply (90, 3)
iq = divd(100, 1000)
iq2 = mod(101, 7)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)



print "Here's a puzz"

what = add(age, sbtkt(height, multiply(weight, divd(iq, mod(iq2, 2)))))

print "That becomes: ", what, "Can you do it by hand?"