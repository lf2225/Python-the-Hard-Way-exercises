i = int(input("Enter #"))


product = 1

while(i >= 1):
	product *= i
	i -= 1

print product


for n in range(1, i+1):
	product *= i
	i -= 1

print product


def factorial(n):
	if(n == 1):
		ans = 1
	else:
		ans = n * factorial(n-1)
	return ans

print factorial(int(input("N?")))