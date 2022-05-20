
a = True
print(a)
x = 123
print(type(x))

y = 12.5
print(type(y))

z = "sasi"
print(type(z))

x= 100
print(id(x))

y = 100
print(id(100))

v1 = "hyd"
v2 = "hyd"
v3 = "hyd"
print(id(v1))
print(id(v2))
print(id(v3))

x = 10
y = 10
print(x is y)
print(y is x)

x = 100
y = 100
print(x is y)

x = 257
y = 257
print(x is y)


# two types of variables
#instance variables and class or static variables

class car:

    wheels = 4   #  class variable, class namespace

    def __init__(self):
        self.mil = 10
        self.company = "Bmw"   # 10 , bmw are instance variable,instance namespace
c1 = car()
c2 = car()
print(c1.company,c1.mil,c1.wheels)
print(c2.company,c1.mil,c2.wheels)

# Namespace:
# namespace is an area where you can create and store object and variable

#####  class namespace
##### object/instance namespace

###
