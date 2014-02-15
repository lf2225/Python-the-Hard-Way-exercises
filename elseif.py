three_int  = (raw_input("Triangle sides?").split())

slist_three_int = sorted(three_int)

a = int(slist_three_int[0])
b = int(slist_three_int[1])
c = int(slist_three_int[2])

print a, b, c
	
#validity of sides, statement to determine illegal, isosceles, scalene or equilateral
if (a == 0 or b == 0 or c == 0):
	print "Sides have to be positive"


elif(a + b < c or a + c < b or b + c < a):
	print "Sides wont reach, ILLEGAL TRIANGLE"



elif(a == b and b == c):
	print "This triangle is EQUILATERAL"



elif(a == b or b == c or c == a):
	print "This triangle is ISOSCELES"



else:
	print "This triangle is SCALENE"


#right obtuse or acute determination statements
if (c^2 == a^2 + b^2):
	print "This triangle is RIGHT"

elif (c^2 < a^2 + b^2):
	print "This triangle is ACUTE"

else:
	print "This triangle is OBTUSE"

