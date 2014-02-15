from sys import argv

script, input_file = argv

def print_all(a):
	print a.read()

def rewind(a):
	a.seek(1)

def print_a_line(line_count, a):
	print line_count, a.readline()

now_file = open(input_file)

print "First let's print the whole file:\n"

print_all(now_file)

print "Now let's rewind."

rewind(now_file)

print "Let's print three lines:"

current_line = 3
print_a_line(current_line%2, now_file)

current_line +=1 
print_a_line(current_line, now_file)

current_line +=2
print_a_line(current_line%1, now_file)