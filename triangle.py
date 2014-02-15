# Triangles
# Read in three sides
# Determine whether they can be triangle sides
# Determine whether the triangle is obtuse, right, or acute
# Determine whether the triangle is scalene, isosceles, or equilateral

# Get legal input

legal_input = False
while (not legal_input):
	three_int = raw_input("Enter three sides of a triangle ")
	side_str = three_int.split()
	side = sorted( [int(side_str[0]), int(side_str[1]), int(side_str[2])] )

	print "Sides are ",
	print side

	# Sides are sorted; side[2] is longest side.
	# side[0] is least number; if this is positive. all sides are positive
	
	if (side[0] > 0):

		# Are the shorter two sides are long enough to reach across the longest?
	
		legal_input = (side[0] + side[1] > side[2])
		if (not legal_input):
			print "The two short sides won't stretch to span the long one"

	else:	# side[0] <= 0
		print "All sides must be positive"
		
# end while -- legal input		

	
# The three sides form a triangle
# Determine equal sides

if (side[0] == side[2]):		# sides are sorted; if 1st == 3rd, then 2nd is also equal
	print "Triangle is equilateral"
elif (side[0] == side[1]  or  side[1] == side[2]):
	print "Triangle is isosceles"
else:
	print "Triangle is scalene"
	
# Determine [ right | obtuse | acute ] triangle

pyth_diff = side[2]**2 - (side[0]**2 + side[1]**2)
if (pyth_diff > 0):
	print "Triangle is obtuse"
elif (pyth_diff == 0):
	print "Triangle is right"
else:
	print "Triangle is acute"
	

