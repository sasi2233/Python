
# string is a collection of characters and it is enclosed by ("") double and triple quotes.
# string does not support to change single character (single index)

a = "My self sasi"
b = "i am a python developer"
print(type(a))
print(a[8:])
print(a[3:7])
print(a.upper())
print(a.lower())
print(a.find(a))
print(a.capitalize())
print(a.title())
print(a.count("a"))
print(a.isalpha())
print(a.isascii())
print(a.endswith(a))
print(a.isnumeric())
print(a.startswith(a))
print(a.isspace())
print(a.isidentifier())
print(a.join(b))
print(b.center(6))
print(b.isalnum())
print(b.isdecimal())
print(b.isprintable())

# 1.string reverse
# str = input("enter any string:")
# print(str[::-1])

# 2. char by char str using for loop

str = "sasikala"
for ch in str:
    print(ch)


# 3.using reversed fun
str = "krishna"
r = reversed(str)
output = ''.join(r)
print(output)


##using while loop
s = "kalyan"
ouput = ''
i = len(s)-1
while i>=0:
    ouput = output+s[i]
    i = i-1
print(output)

####4. Reverse order of words in str
s = "Learn Python Is Very Easy"
l = s.split()
print(l)
l1 = l[::-1]
print(l1)
output = ''.join(l1)
print(output)

tup1 = ('hi', 'sasi')
out_tup = ' '.join(tup1)
print(out_tup)

##5. to reverse internal content of each word

s = "This is Python Program"
l = s.split()
print(l)
l1 = []
for word in l:
    l1.append(word[::-1])
print(l1)
output = ' '.join(l1)
print(output)


### 6. reverse internal second word of a string

s = "one two three four five six"
l = s.split()
print(l)
i = 0
l1 = []
while i<len(l):
    if i%2 == 0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    print(l1)
    i = i+1
output = ''.join(l1)
print(output)


##7.char present in even or odd index in string

s = "sasikala parchuri"
i = 0
print(" The char present in even index:")
while i<len(s):
    print(s[i])
    i = i+2

i = 1
print("The char present in odd index:")
while i<len(s):
    print(s[i])
    i = i+2
#at slicing operator
s = "sasikala parchuri"
print("The char present ineven index:",(s[::2]))
print("The char present inodd index:",(s[1::2]))

#### reverse string
# s = "sasi"
# i = 0
# while i<=0:
#     output = output+s[i]
#     i = i+1
# print(output)

