
###### Data TYpes ###
# int
# float
# complex
# bool
# str
# bytes
# bytesarray
# range
# list
# tuple
# set
# frozenset
# dict
# None

### Int ###
# It holds integral values , whole numbers without decimal point
x = 123
print(type(x))

x = 10     # decimal value
y = 0b10   # binamry value
z = 0o10   # octal
a = 0x10   # hexadecimal

print(x)
print(y)
print(z)
print(a)


x = 456
print(x)

######### Base Functions ######
# bin()
# oct()
# hex()
# By using these 3 functons we can convert one base to another base

a = bin(0o234)
print(a)

b = oct(0x34)
print(b)

c = hex(10)
print(c)

##### float ####
a = 23.0
print(type(a))

b = 45.7895
print(b)

#c = 0x123.5
#print(c)

d = 1.2e3
print(d)
print(type(d))

############# complex #########

# a+bj     # ais real part and b is imaginary part where j is -1

a = 10+2j
print(type(a))
print(a)

# x = 10+2i  in complex any other is not allowed
# print(x)

a = 10+20j
b = 30+40j
print(a+b)
print(a.real)
print(a.imag)

######## bool ######
# True and False
a = True
print(a)

b = False
print(type(b))

a = 10>40
print(a)

b = 40<50
print(b)

c = a>b
print(c)

# True+True = 2
# True+False = 1
# True = 1
# False = 0

a = True+True
print(a)

b = True+False
print(b)

######## string ######3
# group of characters

a = 'sasi'
print(type(a))

b = "kalyan"
print(type(b))
print(b)

c = "this is python program"
print(c[0:4])
print(c[5::10])
print(c[-15:])
print(c[-20:-1])
print(c[::-1])
print(c[-1:-3])
print(c*3)
print(len(c))
# long data type is avilable in python2

########### Type Casting or Type coersion ########

# it is used to convert one data type to another data type.
#inbuilt functions of type casting

# int()
# float()
# complex()
# bool()
# str()

a = int(12.5)
print(a)

b = int('10')
print(b)

#c = int(10+2j)
#print(c)

## Typeerror: con't covert complex to int
d = int(True)
print(d)

##
#e = int("10.5")
#print(e)

# int to float
a = float(10)
print(a)

#b = float(10+9j)
#print(b)
# Type error

c = float(True)
print(c)

d = float('10')
print(d)

#e = float("sasi")
#print(e)
#ValueError: could not convert string to float: 'sasi'

#float to str
a = str(10.5)
print(a)

a = complex(10)
print(a)

b = complex(10.5)
print(b)

c = complex(True)
print(c)

d = complex(False)
print(d)

e = complex("10")
print(e)

#x = complex("sasi")
#print(x)

x = complex(10,20)
print(x)

# z = complex("10","20")
# print(z)
# TypeError: complex() can't take second arg if first is a string

###### BOOL ####

a = bool(1)
print(a)

b = bool(10)
print(b)

c = bool(-19)
print(c)

e = bool(0)
print(e)

e = bool(0.0)
print(e)

x = bool(20.7)
print(x)

z = bool(10+5j)
print(z)

v = bool(0+0j)
print(v)

z = bool("sasi")
print(z)

n = bool("")
print(n)

######### str #######
a = str(10)
print(a)

b = str(10.5)
print(b)

c = str(10.5+30j)
print(c)

d = str(True)
print(d)

