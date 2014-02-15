#declare the tuples
the_count = (1, 2, 3, 4, 5)
fruits = ('apples', 'oranges', 'pears', 'apricots')
change = (1, 'pennies', 2, 'dimes', 3, 'quarters')

#this first kind of for-loop goes through a list
for number in the_count:
	print "This is %d" % number

#same as above
for fruit in fruits:
	print "This is count %s" % fruit + fruit[1] 

#also we can go through mixed lists too
#notice we have to use %r since we dont know the type

for i in change:
	print "I got %r" % i+ fruit[1]

#we can also build lists, first start with an empty one
elements = []

#the use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	#append is a fucntion that lists understand
	elements.append(i)

#now we can print them out too
for i in elements:
	print "Element was: %d" % i
