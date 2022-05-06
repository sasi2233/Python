## string reverse

string = "python"
rev_str = ""
for i in string:
    rev_str = i + rev_str
print(rev_str)


##
string = "sasi"
rev_str = ""
for i in string:
    rev_str = i+rev_str
print(rev_str)


##
string = input("enter any name:")
rev_str = ""
for i in string:
    rev_str = i + rev_str
print(rev_str)

##
string = input("enter any string:")
ch = 0
wrd = 1
for i in string:
    ch =ch+1
    if(i == ''):
        wrd = wrd+1
print("no of char appear in this string are:",ch)
print("no of word appear in this string are:",wrd)


##
'''word = input("enter any name:")
for i in word:
    if(i.upper())==True:
        word+=(i.upper())
    elif(i.lower())==True:
        word+=(i.lower())
    elif(i.isspace())==True:
        word+=i
print(word)
'''


##
str = input("enter any string:")
i = 0
ch2 = ''
while str[i:]:
    ch = ord(str[i])
    if ch > 64 and ch < 91:
        ch2 += chr(ch+32)
    else:
        ch2 += chr(ch)
    i += 1
print("lower case str is:",ch2)


##
str = "this is a python programming"
A = {i:str.count(i) for i in str}
print(A)


###
string = "sasikala parchuri"
count = sum(map(lambda x : 1 if 's' in x else 0, string))
print("count of s in string is :", + count)

