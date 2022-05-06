# if condition
print("exm results:")
marks = 98
if marks == 35:
  print(" you passed the exam")
elif marks <= 50:
  print("you got c grade")
elif marks >= 70 and marks <=80:
  print("you got B grade")
elif marks >= 90:
  print("you got A grade")
else:
  print("you fail the exam")


## For loop
list1 = ['sasi','pavitra','sowjanya']
for i in list1:
    print(i)

##
str1 = "sasi"
for i in str1:
    print(i)

##
num = 30
for i in range(10):
    print(i)


##
for i in range(20,31):
    if(i % 5==0):
        print(i)


## while loop

i = 1
while i < 6:
    print(i,"This is a python program")
    i+=1


## unpacking list
list = [10,20,30]
a, b, c = list
print(a)
print(b)
print(c)


##
str = ["sasi","krishna","kalyan"]
for i in enumerate(str):
    print(i)


###
list1 = [50,60,70,80,90]
for i in list1:
    print(i)


##
tup = ("sasi",23,"kalyan",24)
for j in tup:
    print(j)


###
tup1 = ("sasi",23,"kalyan",24)
for j in enumerate(tup):
    print(j)

