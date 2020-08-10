## String is immutable
## Once assigned can't be changed. 
## Immutable object of string class
welcome = "Hello"
print(id(welcome)) # An address value like 1412014930480
print(type(welcome)) # <class 'str'>
print(welcome) # Hello

welcome = "World" 
print(id(welcome)) # new address value like 1412014930864
print(type(welcome)) # <class 'str'>
print(welcome)  # World
print(welcome[0],welcome[1])  # w o
print(welcome[-1],welcome[-2]) # d l

# welcome[0] = "r" ## Error coz immutable, cant be assigned

##################################
## String operations
s="INfinity"
print(s.isalpha())  ## Check if alphabets only # True
print(s.isdigit())  ## check if digits only # False
print(len(s)) ## length of s # 8
print(s.lower()) ## convert string to lower case # infinity
print(s.upper())  ## convert string to upper case # INFINITY
print(s.count('i'))  ## count no. of occurence # 2
print(s.index('t'))  ## find index of character # 6

##################################
# Slicing string
url1 = "https://www.google.com"
print(url1[::-1]) 
# Reverses url/string 
# moc.elgoog.www//:sptth
print(url1[-4:])  
# Get top level domain (last 4 char)
# .com
print(url1[8:]) 
# Without https
# www.google.com
print(url1[8:-4])
# without top level domain and without https
# www.google
##################################

## String reverse
#### Initialize empty string. Traverse given string
#### Append each char to new string
print('String reversal 1 - for loop')
str1 = "rahul acharya"
rev_str1 = ""
for i in range(len(str1)-1,-1,-1):
    rev_str1 = rev_str1 + str1[i]
print(rev_str1) # ayrahca luhar
###################################
#### Use reversed function
print('String reversal 2 - reversed function')
str2 = "rahul p acharya"
rev_str2 = reversed(str2)
print(rev_str2) # <reversed object at 0x00000148C2A69E48>
print(''.join(rev_str2)) # ayrahca p luhar
###################################
#### Use slicing function like below
###################################
print('String reversal 3 - slicing')
str3 = 'rahul'
l1 = list(str3)
l1 = l1[::-1]  ## reverses the string
print(l1) # ['l', 'u', 'h', 'a', 'r']
ls_1 = '-'.join([str(i) for i in l1])
print(ls_1) # l-u-h-a-r
ls_1 = ''.join([str(i) for i in l1]) # one way
ls_2 = ''.join(map(str, l1))  # Another. or concat using for
print(ls_1) # luhar
print(ls_2) # luhar

print('String reversal - most straightforward: ')
print(str3[-1::-1])
## Dont need all of the above. Can slice string directly
## luhar
####################################
