print "Let's practice something."
print 'You\'d need to know \'bout escapes with \\ that do \n new lines and \t tabs.'

poem '''
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of lovelynor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none 
'''

print '--------------------'
print poem
print '--------------------'


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_form(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates


start_pt = 10000
beans, jars, crates = secret_form(start_pt)

print "With a start point of: %d" % start_pt
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_pt = start_pt / 10

print "we can do that this way:"
print "We'd have %d beans, %d jars, and %d crates" % secret_form(start_pt)