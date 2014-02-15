#basics ex 19, with added modulo ops

def crackers_and_cheez(cheez, crackers):
	print "You have exactly %d cheeses!" % cheez
	print "You have %d crackers!" % crackers
	print "That's enough for the party!"
	print "Get a room. \n"



print "We can just gve the function numbers directly"
crackers_and_cheez(10, 20)


print "OR, we can use vars from our script:"
amt_of_cheez = 10
amt_of_crackers = 50

crackers_and_cheez(amt_of_cheez, amt_of_crackers)


print "We can even do math inside too, math math math:"
crackers_and_cheez(2 + 2 * 2, 100%6)



print "And we can combine the two, vars and math:"
crackers_and_cheez(amt_of_cheez%amt_of_crackers + 1000, amt_of_crackers%amt_of_cheez + 100)