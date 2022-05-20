###list

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


## tuple

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

#### sets

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


##### dictionary #####
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