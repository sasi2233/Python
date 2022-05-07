
##Strings

a = "This is a python programming"
b = "and django"
print(type(a))
print(a[8:])

print(a[3:7])

print(a.upper())

print(a.lower())

print(a.find(a))

print(a.capitalize())

print(a.count("m"))

print(a.isalpha())

print(a.isascii())

print(a.endswith(a))

print(a.isnumeric())

print(a.startswith(a))

print(a.isspace())

print(a.isidentifier())

print(a.join(b))

print(len(a))





##List

#list can store multiple data.
# list can be a mutable. can change any data in list.
# It can be represented by [].

list = [5,20,45,36,75,48,50,45]

print(list [3])
print(list [0:5])
print(list [-5])


list.append(100)
print(list)

list.extend([90,50])
print()

list.insert(7,44)
print(list)

list1 = list.copy()
print(list1)

list.reverse()
print(list)

list.sort()
print(list)

list.sort(reverse = True)
print(list)

list.pop()
print(list)

list.pop(5)
print(list)

list.remove(90)
print(list)

print(list.count(50))

print(max(list))

print(min(list))

print(len(list))


list.clear()
print(list)




## Dictionary

# It is mutable , can chage data in dict but keys does not change
#can store data in keys and values.

person = {'name':'sasi','id':123,'branch':'mca','college name':'hindu'}

print(person.keys())

print(person.values())

a = person.update({'age': 24})
print(a)

print(person.pop('branch'))

print(person.popitem())

person2 = person.copy()
print(person2)

print(person.get('name'))

print(person.clear())




## Tuple
# tuple can store multiple data.
# It is immutable, cannot change or update an data in tuple.
# tuple can be represented by ()

fruits = ('apple', 'banana', 'mango', 'kiwi')
print(fruits[3])
print(fruits[-3])

tup = (1, 30, 45, 67, 3, 45, 65)

print(len(tup))

print(tup.count(45))

print(min(tup))

print(max(tup))

dict = {''}


## SETS

# set can be stored multiple data. These are unordered collection of items.
# It is mutable , can change any data in set.
# sets can be represented by{}
# Duplicate values are not alloed by set.
flowers = {'rose','lilly','jasmin','lotus'}
print(flowers)
print(len(flowers))

set = {1,3,2,50,40,65,67}
set1 = set.copy()
print(set1)

set.remove(65)
print(set)

set.pop()
print(set)

set1 = {10,20,30,40,50}
set2 = {2,3,4,50,40}

set1.update([23,45,67])
print(set1)

set2.add(90)
print(set2)


print(set1.union(set2))

print(set1.intersection(set2))

print(set1.difference(set2))
print(set2.difference(set1))

set1.discard(30)
print(set1)

print(set2.isdisjoint(set1))


set.clear()
print(set)


1.##print nested list unpacking

X = [[1,2,3,4,5],[6,7,8,9,10]]
for i in X:
    for j in i:
        print(j)
    print()

2.## get string from the list
list1 = [{"a":1, "b":2, "c":{"a":4, 2:{"d":5,  "f":"sasikala"}}}]
print(list1[0]['c'][2]['f'])
x = list1[0]['c'][2]['f']
print({i:x.count(i) for i in x})

3.##Transpose a list
def TransposeMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i]=matrix[i][j]

X =[[1,2,3],[4,5,6],[7,8,9]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
TransposeMatrix(X)
for r in result:
    print(r)


4.### Matrix concatination of  Two lists

list1 = [5,3,6]
list2 = [2,5,3]
list3 = []
print("list 1 value:",list1)
print("list 2 value:",list2)
for i in range (0, len(list1)):
    list3.append(list1[i] + list2[i])
print("sum of Two lists:",list3)

5.## unpacking of dictionary
def fun (a, b, c):
    print(a, b, c)
# unpacking of dictionary
d = {'a':10, 'b':20, 'c':30}
fun(*d)
fun(**d)


##
def fun(**kwargs):
    print(type(kwargs))
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))
fun(name='krishna', id='234',language="python")


6.## how can you call duplicate keys in dictionary
dict1 = {'john':345, 'games':654, 'krish':694, 'john':876}
print("dup keys dict:", dict1)
dict1.update({'john':675})
print("updated dup country value",dict1)


7.##Get all values in dict
dict = {'a':'sasikala', 'name':{'location':{'bangulore':{'marath','whitefeild'},'che':{1:{'hyd','mysur'}}}}}
print(dict.values())

##
dict = {'a':'sasikala', 'name':{'location':{'bangulore':{'marath','whitefeild'},'che':{1:{'hyd','mysur'}}}}}

for i in dict:
    print(i)

for i in dict:
    print(dict[i])



8.##user defined function user to call keys
a = {}
n = int(input("Enter number of elements:"))
for i in range(n):
    k = input("Enter key:")
    v = input("Enter value:")
    a.update({k:v})
print(a)
