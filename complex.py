
class complex(object):

 	def __init__(self, r, i):
 		self.real_part = r
 		self.imag_part = i


#overloading 4 binary operators
 	def __add__(self, other):
 		return complex(self.real_part + other.real_part, self.imag_part + other.imag_part)


	def __sub__(self, other):
 		return complex(self.real_part - other.real_part, self.imag_part - other.imag_part)
	

	def __mul__(self, other):
 		return complex((self.real_part * other.real_part - (self.imag_part * other.imag_part)),
 		 (self.imag_part * other.real_part + self.real_part * other.imag_part))
	


	def __div__(self, other):
		denom = other.real_part **2 + other.imag_part **2
		result_real = (self.real_part * other.real_part + self.imag_part * other.imag_part)/denom
		result_imag = (self.imag_part * other.real_part - self.real_part * other.imag_part)/denom
 		return complex(result_real, result_imag)

#print statements
 	def concat_output(self):

 		if (self.imag_part == 1):

 			imag_str = ''
 		elif(self.imag_part == 0):

 			imag_str = '0'
 		else:
 			imag_str = str(self.imag_part)

 		if(self.real_part == 0):

 			real_str = ''

 		else:
 			real_str = str(self.real_part)


		plus = '+'

		if self.imag_part < 0:
			plus = ''

 		complex_image = str(real_str) + plus + str(imag_str) + "i"
		
		return complex_image

############################################################################

r1 = int(raw_input("real coefficient of first number     "))
i1 = int(raw_input("imaginary coefficient first number   "))


r2 = int(raw_input("real coefficient of second number    "))
i2 = int(raw_input("imaginary coefficient second number  "))


c1 = complex(r1, i1)
c2 = complex(r2, i2)

print "First complex number is " , c1.concat_output()
print "Second complex number is " , c2.concat_output()

confirm = raw_input("Do you confirm? Y/N     ")

if confirm == "N":
	print "Make up your goddamn mind!"
	exit()

c_add = c1 + c2
c_sub = c1 - c2
c_mul = c1 * c2
c_div = c1 / c2

print "when adding we get" , c_add.concat_output()
print "when subtracting we get" , c_sub.concat_output()
print "when multplying we get" , c_mul.concat_output()
print "when dividing we get" , c_div.concat_output()


#implement a dictionary that associates complex prime wi
