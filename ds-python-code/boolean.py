# This program prints the usage of bool class in python

a = bool()

print('Value of a in string format(a) = '.format(a))	# format will display a string. False is an empty string
print('Value of bool constructor = ', a)

b = bool(True)

print('Value of b with constructor initialized format(b) = '.format(b))
print('Value of bool with initialized constructor = ', b)

val = 10

bVal = bool(val)	# boolean returns True for non-zero, False if val is zero

print('val = ',val)
print('boolean of val = ',bVal)

str = 'hello'		# boolean returns True for non-empty strings, False for empty string

bStr = bool(str)
print('str = ',str)
print('boolean of str = ',bStr)
