
class complex(object):

 	def __init__(self, r, i):
 		self.real_part = r
 		self.imag_part = i

 	def __add__(self, other):
 		return complex(self.real_part + other.real_part, self.imag_part + other.imag_part)


	def __sub__(self, other):
 		return complex(self.real_part - other.real_part, self.imag_part - other.imag_part)
	

	def __mul__(self, other):
 		return complex(self.real_part * other.real_part, self.imag_part * other.imag_part)
	

	def __div__(self, other):
 		return complex(self.real_part / other.real_part, self.imag_part / other.imag_part)

 	def concat_output(self):
 		complex_image = str(self.real_part) + "+" + str(self.imag_part) + "i"
		return complex_image

############################################################################
r1 = raw_input("real coefficient of first number")
i1 = raw_input("imaginary coefficient first number")

r2 = raw_input("real coefficient of second number")
i2 = raw_input("imaginary coefficient second number")

c1 = complex(r1, i1)
c2 = complex(r2, i2)

print c1.concat_output()
print c2.concat_output()

c_sum = c1 + c2

print c_sum.concat_output()