
# def is a function used to create own function


def fun():
  print("Hi World")
fun()                              # function calling


##
def fun1(name):                                # parameter
  print("hi "+ name +" goodafter noon")
fun1('krishna')                                # Argument


def fun(name):
  print("hi "+name+" good morning")
fun("sasi")


### scope of the funtion

def function():
  a = 4
  print("The scope inside the function is",a)    # inside the scope the function


a = 10
function()
print("The scope outside the function is:",a)    # outside the scope of the function


# string function

name = "sasikala"
print(len(name))

str_fun = "This is a python programmimg"
if "python"  in str_fun:
  print("this is present in str_fun")
else:
  print("this is not in str_fun")


## PASSING PARAMETER
def fun(name):  # name is an parameter
  print("Hello", name, "Good Morning")


fun("Rishi")  # Rishi is an argument
fun("krishna")


### square root of given number
def square(x):
  print("the square of {} is: {}".format(x, x * x))


square(10)
square(100)


## add
def add(a, b):
  return a + b
  print("return")


add(23, 56)


# even or odd

def evenodd(num):
  if num % 2 == 0:
    print("The number is even")
  else:
    print("The number is odd")

evenodd(45)
evenodd(50)


## factorial of given number

def fact(x):
  result = 1
  while x >= 1:
    result = result * x
    x = x - 1
  return result


for i in range(1, 6):
  print("the fact of {} is = {}".format(i, fact(i)))


###
def fact(a):
  if a == 1:
    return 1
  else:
    return (a * fact(a - 1))


fact(5)


### return multiple values

def fun(a, b):
  return (a + b, a - b, a * b, a / b)
  print("return")


fun(34, 2)


## fibonacci series

def fib(n):
  sum = 0
  n1 = 0
  n2 = 1
  for i in range(2, n):
    n1 = n2
    n2 = sum
    sum = n1 + n2
    print(sum)

fib(10)


### while loop
def fact(n):
  result = 1
  while n>1:
    result = result*n
    n = n-1
  return result

print(fact(10))



####### Types of Arguments #######

# positional
# keayword
# default
# Variable length

#### Positional Arguments ######

def fun(a,b):
  return a+b
fun (100,50)                    # These are positional arguments
fun (50,45)
fun('Kritika','Trivedi')
fun('Trivedi','Kritika')


####### Keyword Arguments #########

def fun(name,msg):
  print("hello",name,msg)

fun(name = 'sasi',msg = 'good morning')
fun(msg = 'good morning',name = 'sasi')
fun('sasi',msg = 'good morning')
#fun(msg = 'good morning','sasi')


####### Default Arguments #########

def fun(name='guest'):
  print("hello",name,"how are you")

fun('sasi')
fun()

##
# def fun(name='sasi',msg):
#   print('hello',name,msg)
# fun("sasi")

###
def fun(marks,age,name='guest',msg = 'gm'):
  print('student name:',name)
  print('student marks:',marks)
  print('student age:',age)
  print("msg:",msg)
fun(100,22,"sasi","gm")
fun(98, age=23, name="sasi", msg="good morning")
#fun(marks = 67,23,name="sasi",msg="gm")
#fun(98, age=23, "sasi","good morning")


######### Variable Length Argument ########

def sum(*n):
  result = 0
  for i in n:
    result = result+i
    print("the sum:",result)

sum()
sum(10)
sum(10,20)
sum(10,20,30)

##
def sum (*n,name):
  result = 0
  for x in n:
    result = result+x
    print("the sum by",name,":",result)

sum(name="sasi")
sum(10,name="sasi")
sum(10,20,name="sasi")