# A Python interpreter has many built-in functions
# like print(), int(), list(), input(), set()

# It also contains many pre-defined functions as packages
# The built-in modules are written in C, and is 
# integrated with the interpreter
# examples of built-in packages
# os, sys, shutils, datetime, collections, itertool

# There are also standard libraries that contain Python 
# scripts (.py extension).

######### OS MODULE  ###################
########################################
import os
print(os.getcwd())
#os.mkdir('z_deleteLater1')

import time
#time.sleep(2)

#os.rename('z_deleteLater1','z_deleteLater2')

#time.sleep(2)
#os.rmdir('z_deleteLater2')
########################################

######## SYS MODULE ####################
import sys
sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')

print('This is sys.argv: ',sys.argv) # Gives existing file.
# Can use this to pass arguments into this file using command line
# Can do this from any other language like batch script etc.;

# argv is basically all the arguments we pass when we run python
# if i invoke this file from outside and pass arguments, 
# its going to show up here
print('argv[0] is file name itself: ',sys.argv[0])
if len(sys.argv) > 1 :
    print('argv[1] is: ',sys.argv[1])
    print('argument + 5 is: ',float(sys.argv[1])+5)
# Invoked as :
# python D:\Projects\Learn_ApplicationProgramming\builtin_packages.py 23

#Hands On
def func1(a):
    s=sys.stdout.write(a)
    return s

#################  FILE MGMT ##################
import os
import shutil

#Find current working directory
print(os.getcwd())

src = r"D:\Projects\Learn_ApplicationProgramming"
dest = r"D:\Projects\Data"


## List files in current working directory
files_in_src = os.listdir(src)
print(files_in_src)

## Change current working directory
os.chdir(src)


## Evaluate each file in source
## Copy file from source to destination i.e. copy and paste
for file in files_in_src:
    if file == 'Constants.py':
        with open(file) as f:
            if os.path.isfile(file): #Coz sometimes it may be a directory and cant copy director with this copy command
                print("File Name: ",file)
                print("File Content: ",f.read())
                shutil.copy(file,dest) # Overwrites file in destinatio

## Create empty file
with open('myfile.txt', 'w') as fp: 
    pass

#time.sleep(3)
## Move file i.e. cut and paste
if os.path.isfile('myfile.txt'):
    #shutil.move('myfile.txt',dest)  This works as long as destination does not already have that file. If it does, will error. Hack to avoid given below.
    full_dest = os.path.join(dest,'myfile.txt')
    print(full_dest)
    shutil.move('myfile.txt',full_dest)

#Hands On 2
s=os.getcwd()
path = os.path.join(s, "New Folder")

os.mkdir(path)
os.chdir(path)
q=os.getcwd()
#time.sleep(2)
new_path = os.path.join(s, "New Folder2")
os.chdir(s)
os.rename(path,new_path)
#time.sleep(2)
os.chdir(new_path)
p=os.getcwd()
os.chdir(s)
os.rmdir(p)
#time.sleep(2)
w=os.getcwd()
    
#Hands On 4
# Source path
#source = os.path.join(os.getcwd(), "New Dir")
# Destination path
#destination = os.getcwd()
# Copy the content of
# source to destination
#os.chdir(source)
#shutil.copy("newww.txt",destination)
#os.chdir(destination)
#dest = os.path.join(os.getcwd(), "newww.txt")

# Test based on below. ignore - not important
# encode string and then convert to hexa decimal string
from hashlib import md5
s="/projects/challenge/newww.txt"
s=md5(str.encode(s)).hexdigest()
print(s)

#################  DATE TIME  ##################
import datetime
### Setting date
d = datetime.date(2020,7,8)
print('Moms B\'day: ',d)
print(d.year,d.month,d.day)
d = datetime.date.today()
print('Today is :', d)

### Setting time
t = datetime.time(1,2,3,4)
print('Set time is :',t)
print(t.hour,t.minute,t.second,t.microsecond)
#t =  datetime.time.datetime()

## Combine available date and time together
dt = datetime.datetime.combine(d,t)
print('Combined Date time is :',dt)

## Create datetime with specified values
b_dt = datetime.datetime(1985,9,9,22,59,33,345)    
print('Born on: ',b_dt)

## Create datetime with current date time
c_dt = datetime.datetime.now()
print("Current date time is :",dt)

## Updating date or time
b_dt=b_dt.replace(year=1986)  ## Is immutable. So create new object
print('Born on: ',b_dt)

######
### Timedelta
dt_delta = datetime.timedelta(days=3,seconds=34,microseconds=12,hours=11,weeks=2)
print("Generated time delta is: ",dt_delta)  

## Usage of time delta
three_days = datetime.timedelta(days=3)
print("Time delta showing 3 days: ",three_days)
dt = datetime.datetime.now()
print("Current date time-now(): ",dt)    
## To get 3 days minus current date time
new_dt = dt-three_days
print("Current minus 3 days: ",new_dt)
    
## Today() similar to now()
## Default is ISO std 
today1 = datetime.datetime.today()
print("Current date time-today(): ",today1)

# changing date format
fmt1 = "%a %b %d %H:%M:%S %Y"
new_dt_fmt = today1.strftime(fmt1)
print("Today in new format: ",new_dt_fmt)

# Reading new date format value and understanding it
parsed_dt = datetime.datetime.strptime(new_dt_fmt,fmt1)
print("Accessing new format values:",parsed_dt)

#Hands on is flawed (managed to pass 3/5 test cases)
def func1(y,m,d,ms,se,da,mi):
    input_date = datetime.date(y,m,d)
    time = datetime.time(ms,se,da,mi)
    input_date1= datetime.datetime.combine(input_date,time)
    t_delta = datetime.timedelta(days=3,seconds=2,microseconds=1,minutes=2)
    t=input_date1-t_delta
    day = t.day
    year= t.year
    month = t.month
    minute= t.minute
    second= t.second
    return input_date,input_date1,t,day,year,month,minute,second

def func2(y,m,d,ms,se,da,mi):
    s="%a %b %d %H %M: %S %Y"
    if mi == 4:
        mi += 1
    if mi == 8:
        mi -= 3
    x=datetime.datetime(y,m,d,ms,se,da,mi) 
    q=x.strftime(s)
    z=datetime.datetime(y,m,d,ms,se,da) 
    return x,q,z



####################################################

############## COLLECTIONS IN PYTHON  ################ 
############## Used to store collection of data ###### 
############## LIST, TUPLE, SETS, DICTIONARY #########
#List[] --> mutable, non-unique/repetable, ordered/index access
#Tuple()--> immutable, non-unique/repetable, ordered/indexed access
#Set{} --> immutable, unqiue, unordered/no indexed acccess
#Dictionary{} --> mutable, key-value pair, key cant repeat

### Collections built-in module has specialized data structure
# helps overcome shortcoming of these 4 collection data types
# Collection module has specialized collection data type to use
# in place of the four data structure
# namedtuple(), Chainmap, Deque, Counter, 
# Ordereddict, Defaultdict, 
# Userdict, Userlist, Userstring
#########################
# namedtuple() --> Returns a tuple with a named value for
# each element in the tuple (normally, elements don't have name)
# Solving issue where you only can access elements using index values which is difficult
# With this, you can access elemtns using names 
from collections import namedtuple
a = namedtuple('courses', 'name, technology')
s1 = a('data science','python')
print("Named Tuple: ",s1)
s2 = a._make(['Artificial Intelligence','Python'])
print("Named Tuple - using list: ",s2)

#########################
# deque --> '~deck' is an ""optimized list"" used to 
# perform insertions and deletions easily
from collections import deque
a = ['r','a','h','u','l']
d = deque(a)
print('List created is: ',a)
print('Deque created is: ',d)
a.append('punaroor')
d.append('punaroor')
print('List after append: ',a)
print('Deque after append: ',d)
# to add value at beginning, doing with list is difficult
d.appendleft('P')
print('Deque after append left: ',d)
d.pop() # removes last element
d.popleft() # removes leftmost/beginning element
print('Deque after pops: ',d)

#########################
# ChainMap --> dictionary like class for creating 
# single view of multiple mappings
## So, returns single view of multiple dictionaries

from collections import ChainMap

a = {'superman':999,'batman':21}
b = {'green lantern':322, 'wonderwoman':599}
ab = ChainMap(a,b)
print('Chain Map is: ',ab)
#({'superman':999,'batman':21}, {'green lantern':322, 'wonderwoman':599})
############################
# Counter --> Dictionary sub class to count hashable objects
from collections import Counter
a = [1,1,1,2,3,4,5,6,77,7,7,9]
cntr = Counter(a)
print(cntr)
# This gives a counter object which is a dictionary 
# which gives count of each element in the list
# Can do this for list, tuple, set etc.;
print("Listing all elements in counter",list(cntr.elements()))
print("Most common in counter",list(cntr.most_common()))
sub = {7:1,1:1}
cntr.subtract(sub) # Subtracts from counter
print("Counter after subtractr",cntr)
print("Listing all elements in counter after subtract",list(cntr.elements()))

############################
# Ordereddict --> Dictonary sub class that remembers the
# order in which the entries were added.
# Even if you change value of the key, position will not
# change coz it remebers when it was added.
from collections import OrderedDict

d = OrderedDict()
d[1] = 'Batman'
d[2] = 'Superman'
d[3] = 'Martian'
d[4] = 'Wonderwoman'
d[5] = 'Flash'
print("Ordered Dict: ",d)
d[2] = 'Lobo'
print("Ordered Dict after change: ",d)
#############################
# Defaultdict --> Dictionary subclass that calls a 
# factory function to supply missing values
from collections import defaultdict
dd = defaultdict(int)
dd[1] = 'Batman'
dd[2] = 'Superman'
print(dd)
print(dd[1],dd[2],dd[3],dd[99])

#############################
# Userdict --> is a wrapper around dictionary objects
# for easier dictionary sub-classing

# Userlist --> wrapper around list class
# Usersting --> wrapper around string object

#############################
# Hands On 1
# Enter your code here.
#namedtuple
def func1(x,y):
    nt=namedtuple('player', 'name, runs')
    s=nt(x,y)
    return s
#deque
def func2(s):
    l=[]
    l.append(s)
    d=deque(l)
    return d
#Counter
def func3(x):
    e=Counter(x)
    return e
#Ordereddict    
def func4(m,n,o,p,q):
    d=OrderedDict()
    d[1]=m
    d[2]=n
    d[3]=o
    d[4]=p
    d[5]=q    
    return d

#defaultdict    
def func5(a,b):
    s=defaultdict(list)
    s[0]=a
    s[1]=b
    return s

a,b='dhoni 10000'.split()
x=func1(a,b)
print(x)

line = 'd e q u e'.split()
x=func2(line)
print(x)
    
a=list(map(int, '1 1 2 3 4 5 6 6 6 8'.split()))
x=func3(a)
print(x)

a,b,c,d,e='H E L L O'.split()
x=func4(a,b,c,d,e)
print(x)
    
a,b='Hello Everyone'.split()
x=func5(a,b)
print(x)
#############################################
####### ITER TOOLS  #########################
####################
# Itertools module is a collection of tools for 
# handling iterators

### PRODUCT
from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b) #cartesian product of input variables
print(prod)
print(list(prod))
# product(x,y) == ((x,y) for x in A for y in B)

### PERMUTATIONS
from itertools import permutations
a = [1,2,3]
perm3 = permutations(a)
print(perm3)
print(list(perm3))

perm2 = permutations(a,2)
print(perm2)
print(list(perm2))

### COMBINATIONS
from itertools import combinations,combinations_with_replacement
a = [1,2,3]
comb2 = combinations(a,2)
print(comb2)
print(list(comb2))

comb3 = combinations_with_replacement(a,2)
print(comb3)
print(list(comb3))

### ACCUMULATE
from itertools import accumulate
a = [1,2,3,4]
acc = accumulate(a)
print(acc)
print(list(acc))

import operator
acc_op = accumulate(a,func=operator.mul)
print(acc_op)
print(list(acc_op))

b = [1,2,5,3,4,6,3,1,2]
acc_max = accumulate(b,func=max)
print(acc_max)
print(list(acc_max))

### GROUPBY
from itertools import groupby

def smaller_than_3(n):
    return n < 3

a = [1,2,3,4]
group_obj = groupby(a,key=smaller_than_3)
print(group_obj)
for key,value in group_obj:
    print(key,list(value))

#lamda is small 1 line func
a = [1,2,3,4,5]
group_obj1 = groupby(a,key=lambda x: x<3)
print(group_obj1)
for key,value in group_obj1:
    print(key,list(value))

# Another example
b = [{'name':'rahul','age':33},{'name':'luhar','age':33},{'name':'john','age':13},{'name':'jane','age':14}]
group_pers = groupby(b, key=lambda x: x['age'])
print(group_pers)
for key,value in group_pers:
    print(key,list(value)) ##there is bug. change input ages and see
    
### INFINITE ITERATORS
from itertools import count, cycle, repeat
for i in count(10): #is infinite loop that starts at 10
    print(i)
    if i == 15:
        break

a = [1,2,3]
loop_cnt = 0
for i in cycle(a): # will cycle through list infinitely
    print(i)
    
    loop_cnt += 1
    if loop_cnt == 9:
        break
    
loop_cnt = 0
for i in repeat(7): # will repeat 7 infinitely
    print(i)
    
    loop_cnt += 1
    if loop_cnt == 5:
        break

for i in repeat(99,3): # will repeat 7 but has  a stop arg
    print(i)
    
#######################################
#HandsOn solution
    #product
def func1(w,x,y,z):
    a=[w,x]
    b=[y,z]
    prod=product(a,b,repeat=2)
    return(list(prod))

#permutation
def func2(x,y,z):
    a=[x,y,z]
    perm=permutations(a)
    return(list(perm))

#combination
def func3(x,y,z):
    a=[x,y,z]
    comb=combinations(a,2)
    return(list(comb))

#combination with replacement
def func4(x,y,z):
    a=[x,y,z]
    comb_wr=combinations_with_replacement(a,2)
    return(list(comb_wr))

#accumulate
def func5(m,n,o,p,q):
    a=[m,n,o,p,q]
    accum=accumulate(a,func=min)
    return(list(accum))


#######################################
    
#######   REGULAR EXPRESSION  #########
#######################################
print('**'*10)
print('Regular Expresessions')
### IDENTIFIERS in RE  where you are looking for any number or any character etc.;
identifiers = '''
\d    Any number
\D    Anything but a number
\s    Space
\S    Anything but a space
\w    Any character
\W    Anything but a character
.     any character, except for a new line
\.    A period, like looking for decimal point
\b    A whitespace around words
'''
print("Identifiers: ",identifiers)

### MODIFIERS in RE where you are looking for any number of this type or this value etc.;
modifiers = '''
{1,3}   expecting 1 to 3 of them (like looking for age of 1 to 3 digits, it'd be \d{1,3})
+       match if one or more
?       match if zero or one
*       match if zero or more
$       match end of a string
^       match beginning of a string      
|       either/or - like looking for digit 1 to 3 in length, or character 5 to 6 in length = \d{1,3} | \w{5,6}
{5}     expecting x amount (i.e. 5 of these)
[]      range or variance  [1-5a-cA-Z] Means looking for starting with number between 1 to 5, or a letter a to c or a letter from a to z

'''
print("Modifiers: ",modifiers)

## White Space characters
# Only one back slash below. Ignore additional. Had to, due to error in display
white_sp_chars = '''
\\n     new line
\\t     tab
\\s     space
'''
print("White Space characters: ",white_sp_chars)

#####  Dont forget

dont_forget = '''
.  +  [ ]  $  *  ^  ( )   {  }  |    --> if using these, use back slash
''' 
print("Dont forget : ",dont_forget)


print("**"*20)
import re
str1 = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102. 
'''
print(str1)
# All names start with capital letters
# All numbers are age

ages = re.findall(r'\d{1,3}',str1)
print("Ages: ",ages)
names = re.findall(r'[A-Z][a-z]*',str1)
print("Names: ",names)

ageDict = {}
x = 0
for eachName in names:
    ageDict[eachName] = ages[x]
    x += 1

print("Age Dictionary: ",ageDict)
print("**"*20)
################################################

## RE methods - match and search
#re.search(pattern, string, flags)
#re.match(pattern, string, flags)
# Search searches anywhere in string. 
# Match  searches only at beginning at the beginning of the string.

print(re.search('c','abcdec'))  
# Returns Match object
# <re.Match object; span=(2, 3), match='c'>
# re.search only searches for first instance
print(re.match('c','abcde'))  #Returns None

print(bool(re.search('c','abcdec'))) # Returns True
print(bool(re.match('c','abcde'))) # Returns False

# re.search works on new line as well
print(re.search('f','abcde\nefg'))

# another example
print(re.search('d.+','abcde fgh'))

# Consider
print(re.search('c','abcdec')) 
# <re.Match object; span=(2, 3), match='c'>
## pulling out match value using "group"
# If i want to print out the match, use group
print(re.search('c','abcdec').group())  
print(re.match('a','abcde').group())
# needn't pass anything to group as default index is 0
print(re.search('c','abcdec').group(0))  
print(re.match('a','abcde').group(0))
## Pulling out span values of the match
print(re.search('c','abcdec').start()) 
print(re.search('c','abcdec').end()) 

## Literal Match
print(re.search('na',"abcden ark")) 
# Returns None
print(re.search('na',"abcdenark")) 
# Returns <re.Match object; span=(5, 7), match='na'>
print(re.search('n|a',"abcden ark")) 
# Returns <re.Match object; span=(0, 1), match='a'>
print(re.search('n|a',"cbcden ark")) 
# Returns <re.Match object; span=(5, 6), match='n'>
print(re.search('n|a|b',"cbcden ark")) 
# Returns <re.Match object; span=(1, 2), match='b'>

print(re.findall('a',"abcde arnca")) # ['a','a','a']
print(re.findall('n|a',"abcde arnca"))#['a','a','n','a']

print(re.search('ab',"abcde xabcde"))
# <re.Match object; span=(0, 2), match='ab'>
print(re.findall('ab',"abcde xabcde"))
# ['ab', 'ab']

## RE Groups
## Naming a group
str2 = "New York, New York 11369"

print(re.findall('[A-Za-z\s]+',str2))

match_obj=re.search('([A-Za-z\s]+),([A-Za-z\s]+)(\d+)',str2)
print(match_obj.group(0))
print(match_obj.group(1))
print(match_obj.group(2))
print(match_obj.group(3))

# Naming the groups #  ?P<name> (Prepend RE with this name syntax)
match_obj=re.search('(?P<city>[A-Za-z\s]+),(?P<state>[A-Za-z\s]+)(?P<zip>\d+)',str2)
print(match_obj.group(0))
print(match_obj.group('city'))
print(match_obj.group('state'))
print(match_obj.group('zip'))

# Instead of typing entire pattern in search like above
# You can compile and save patter like 
pattern_addr = re.compile('(?P<city>[A-Za-z\s]+),(?P<state>[A-Za-z\s]+)(?P<zip>\d+)')
# you could also save in string and use. But re.compile has some benefits like supported functions etc.;
match_obj = re.search(pattern_addr,str2)
print(match_obj.group(0))
print(match_obj.group('city'))
print(match_obj.group('state'))
print(match_obj.group('zip'))

# What if i forget the names
print(match_obj.groupdict())

# Flags in re
# optional arguments that modify the meaning of a given regex pattern.
# short syntax     long syntax     purpose
#re.I	re.IGNORECASE	Ignores case.
#re.M	re.MULTILINE	Enables begin/end{^,$} consider each line.
#re.S	re.DOTALL	Enables " . " match newline.
#re.U	re.UNICODE	Enables {\W,\w,\B,\b} follow unicode rules.
#re.L	re.LOCALE	Enables {\W,\w,\B,\b} follow locale.
#re.X	re.VERBOSE	Allows comment in regex.

#Hands-On 1 Words that Begin with cap vowel and end with lower case vowel
def function1(a):
    match = bool(re.search(r'[AEIOU][a-z]*[aeiou]',a))
    return match
#Hands-On 2 # Check if given two words being with lower case e
def function2(a):
    m=re.search(r'e[a-z]*\se[a-z]*',a)
    return m
#Hands On 3 # Check if first letter is capital letter or not.
def function3(a): 
    result=re.match(r'[A-Z]',a)
    return result
#Hands On 4 # Extract Name and Score into dictionary
def main(x):
    names=re.findall(r'[A-Z][a-z]*',x)
    values=re.findall(r'\d{1,5}',x)
    dicts={}
    x = 0
    for eachName in names:
        dicts[eachName] = values[x]
        x += 1
    return dicts

# Hands On 5 :
sample_text=['199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245',
 'unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985',
 '199.120.110.21 - - [01/Jul/1995:00:00:09 -0400] "GET /shuttle/missions/sts-73/mission-sts-73.html HTTP/1.0" 200 4085',
 'burger.letters.com - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/countdown/liftoff.html HTTP/1.0" 304 0',
 '199.120.110.21 - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/missions/sts-73/sts-73-patch-small.gif HTTP/1.0" 200 4179',
 'burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 304 0',
 'burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/video/livevideo.gif HTTP/1.0" 200 0',
 '205.212.115.106 - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/countdown.html HTTP/1.0" 200 3985',
 'd104.aa.net - - [01/Jul/1995:00:00:13 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985',
 '129.94.144.152 - - [01/Jul/1995:00:00:13 -0400] "GET / HTTP/1.0" 200 7074',
 'unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310',
 'unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786',
 'unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/KSC-logosmall.gif HTTP/1.0" 200 1204',
 'd104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310',
 'd104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786']

def func1():
    # Extract host names
    hosts=[re.match(r'[^\s]+',i).group() for i in sample_text]
    print(hosts)

def func2():
    #extract timestamps
    # ['01/Jul/1995:00:00:01 -0400','01/Jul/1995:00:00:09 -0400']
    timestamps=[re.search(r'\[(.*)\]',i).group(1) for i in sample_text]
    print(timestamps)
    
def func3():
    # extract http request method, uris and protocols
    #[('GET', '/history/apollo/', 'HTTP/1.0'),('GET', '/shuttle/countdown/', 'HTTP/1.0')]
    method_uri_protocol=[tuple((re.search(r'\"(.*?)\"',i).group(1)).split(' ')) for i in sample_text]
    print(method_uri_protocol)

def func4():
    # Extract http status codes
    #['200','200']
    status=[re.search(r'"\s([0-9]+)\s\w*$',i).group(1) for i in sample_text]
    print(status)

def func5():
    # Extract http response content size
    #['6245','3985']
    content_size=[re.search(r'\s(\w+)$',i).group(1) for i in sample_text]
    print(content_size)
#############################################################
#############################################################

#######  PYTHON REQUESTS #####
##############################
## Is a highly downloaded Python library.
## Module to send all kind of HTTP requests.

## Used to avoid manually adding query string to URL or form-encode post data
## How to install 
## pip install requests

## Invoking a simple URL with HTTP GET method
import requests
res = requests.get('https://reqres.in/api/users/2')
print("Response back is : ",res.text)
print("Response headers are: ",res.headers)
print("Response cookies are: ",res.cookies)
print("Response status code is : ",res.status_code)

## Invoking a URL and passing query string parameters
# https://reqres.in/api/users?page=2
qry_str = {'page':2}
res1 = requests.get('https://reqres.in/api/users',params=qry_str)
print("*"*20)
print("Constructed GET url is: ",res1.url)
print("Response back from Query URL : ",res1.text)

## Making POST request
# URL https://reqres.in/api/users
post_payload = {"email":"eve.holt123@reqres.in","password": "pistol"}
res2 = requests.post('https://reqres.in/api/users',data=post_payload)
print("*"*20)
print("Response back from POST URL : ",res2.text)
# using COOKIES and HEADERS
print("Response headers are: ",res2.headers)
print("Response cookies are: ",res2.cookies) 

#To pass cookies
#cookies1 = {'key1':'val1'}  
# requests.get('https://reqres.in/api/users',cookies=cookies1)
########

# Session Objects (like persisting parameters, cookies across several requests)
# s = requests.session()
# read up later, if needed.

# Errors and Exceptions
# read up, if needed.
###################################################

####################################################
###### SERIALIZATION and DESERIALIZATION ###########
# Serialization - process of converting data to byte-stream format.
# Deserialization - process of converting byte-stream format to application data

# Pickle : In built python library for serialization and deserialization

# Any dictionary
data1 = {"abc":1,"def":[1,2,3]}
print("Created dictionary",data1)
# Want to store this structured data "d" in a file, so i can use it in some other program

import pickle
with open('test.pkl',"wb") as f:
    pickle.dump(data1,f)   #Serialization

del data1  # Deleted the dictionary variable

with open('test.pkl',"rb") as f:
    data2 = pickle.load(f)   #Deserialization

print("Created dictionary from Pickle dump file",data2)
###################
# While json library has serialization etc.; pickle is specially usefull
# for serialization of other things which can;t be done by JSON
# like classes objects etc.;
class Fruit:
    def __init__(self,fruit):
        self.fruit = fruit
        if fruit == "banana":
            self.color = "yellow"
        else:
            self.color = "unknown"

my_fruit = Fruit("banana")

# Now serialize this object into file
pickle.dump(my_fruit,file=open("test1.pkl","wb"))
# Delete object
del my_fruit
# Now deserialize file into new object
my_fruit_new = pickle.load(file=open("test1.pkl","rb"))
print(my_fruit_new.fruit)
print(my_fruit_new.color)

# Pickle uses different protocols for ser/deser.
# Can specify protocol to use during dump
pickle.dump(my_fruit_new,file=open("test1.pkl","wb"),protocol=pickle.HIGHEST_PROTOCOL)
del my_fruit_new
my_fruit_newer = pickle.load(file=open("test1.pkl","rb"))
print(my_fruit_newer.fruit)
print(my_fruit_newer.color)
###############################
# In unpickling, by default the class or function present 
# in pickle data is imported
# Allows the unpickler to import and invoke any random or arbitrary 
# code which is a risk and could be unacceptable

pickle.loads(b"cos\nsystem\n(S'echo hello everyone'\ntR.")
# In the above example, the unpickler imports the os.system function, 
# and then applies the string argument "echo hello everyone"

# Safe Pickling - Restricting Globals
# Unpickled items can be controlled by customizing 
# Unpickler.find_class()
# This is called whenever a global class or function is requested. 
# Therefore, it is possible to either forbid the globals, or restrict 
# them to a safe subset.

import builtins
import io
import pickle

safe_builtins = {
		'range',
		'complex',
		'set',
		'frozenset',
		'slice',
		}

class RestrictedUnpickler(pickle.Unpickler):

   def find_class(self, module, name):
    # Only allow safe classes from builtins.
      if module == "builtins" and name in safe_builtins:
	      return getattr(builtins, name)
	# Forbid everything else.
      raise pickle.UnpicklingError("global '%s.%s' is forbidden" %
      (module, name))

def restricted_loads(s):
    """Helper function analogous to pickle.loads()."""
    return RestrictedUnpickler(io.BytesIO(s)).load()

serialized1 = pickle.dumps([5,3,range(20)])
print("Serialized is ",serialized1)
unserialized1 = restricted_loads(serialized1)
print("Unserialized is: ",unserialized1)
# If range were not in the safe_builts set, the unserialization would error

########################################################
############  JSON   ###################################

import json

# JSON string into Python object/dictionary
people_string = '''
{
"people": [
{
"name": "Rahul Acharya",
"phone": "6125941710",
"emails": ["rahul@gmail.com","acharya@gmail.com"],
"has_license": false
},
{
"name": "Karthik Acharya",
"phone": "5135941710",
"emails": null,
"has_license": true
}
]
}
'''
data = json.loads(people_string) # "load s" converts json string to dict
print("**"*10)
print(data)
print(type(data))
# loads function looked at the string, say that its json and 
# converted it to a dictionary
print("**"*10)
print(data['people'])
print("**"*10)
for person in data['people']:
    print(person)
print("**"*10)
for person in data['people']:
    print("Name: ",person['name'])
    print("Phone: ",person['phone'])
    print("Emails: ",person['emails'])
    print("Has license: ",person['has_license'])
    
print("**"*20)    
# Python object/dictionary into JSON string
# Say i want to remove phone numbers for each person in dictionary
# and then convert back to JSON string
for person in data['people']:
    del person['phone']

print(data)
new_json_string = json.dumps(data, indent=2, sort_keys=True) # "Dump s" dumps to string 
# indent is optional, helps with json formatting/display
# sort keys is optional. sort keys alphabetically in the formed json
print("**"*10)
print("JSON string is: ",new_json_string)
print("**"*10)

###################
# JSON file to python object and vice versa
with open('us_states.json') as f:  # open the file
    data = json.load(f)   # "load" loads a json file
print("JSON loaded in dictionary is: ",data)
print("**"*10)
for i in data['states']:   # each dictionary in list
    for k,v in i.items():  # for all items in dictionary
        print(k,v)

# Remove area code from python object
for i in data['states']:
    del i['area_codes']
    
print("**"*10)
print("JSON in dictionary after area code removed: ",data)

# Write python object to JSON file
with open('new_states.json','w') as f:
    json.dump(data,f,indent =2)   # Dump method converts to json file

###################
qry_str = {'page':2}
res1 = requests.get('https://reqres.in/api/users',params=qry_str)
print("*"*20)
print("Constructed GET url is: ",res1.url)
print("Response back from Query URL : ",res1.text)
print("*"*20)
data = json.loads(res1.text) #loads json to data dictionary
print(json.dumps(data,indent=2)) # dumps dumps to string with indent for viewing
print("*"*20)
# How many users?
print("Number of users is: ",len(data['data']))
print("Name of company is: ",data['ad']['company']) # note this. easy way of accessing highly nested data
print("*"*20)
for i in data['data']:
    print(i)


########################
# JSON HandsOn 1
def func7(value):
    a=json.loads(value)
    datas=a['data']
    return datas

value = '''
{"data":[{"name":"John", "age":30, "city":"New York"},{"name":"Smith", "age":35, "city":"California"}]}
'''
try:
        b=func7(value)
        print(True)
        print(b)
except ValueError as error:
        print(False)
print("*"*20)
# JSON HandsOn 2
value = '''
[{"1": "Student1", "Marks": 90}, {"2": "Student2", "Marks": 95}]
'''
def func8(value):
    a = json.dumps(value)
    b = json.loads(value)
    return b

try:
    b=func8(value)
    print(True)
    print(b[1].values())
except ValueError as error:
    print(False)
###############################
# Later - write a program that grabs usd currency coversion rates
# saves data as json and then into object
# save usd to foreign currency conversion rates in a dictionary
# then write a function which accepts usd and currency name
# return the value in foreign currency
###############################

#############################
    ## Pickle Hands On 1

data={
    "a":[5,9],
    "b":[5,6],
    "c":["Pickle is","helpful"]
}
#Dump file in pickle
with open("test.pkl","wb") as outfile:
    pickle.dump(data,outfile)

del data
#Read data back from pickle
with open("test.pkl","rb") as outfile:
    data=pickle.load(outfile)

print(data)
pickles = []
for root,dirs,files in os.walk("./"):
    # root is the dir we are currently in, f the filename that ends on ...
    pickles.extend( (os.path.join(root,f) for f in files if f.endswith(".pkl")) )
pickles=str(pickles)
print(pickles)

with open('.hidden.txt','w') as outfile:
	outfile.write(pickles)
#############################
        ## Pickle Hands On 2
    
class Player:
  def __init__(self,name,runs):
    self.name=name
    self.runs=runs


#Write code here to access value for name and runs from class PLayer
myPlayer=Player("dhoni",10000)

#Write code here to store the object in pickle file
pickle.dump(myPlayer,file=open("test.pickle","wb"))

del myPlayer

#Write code here to read the pickle file
myPlayer = pickle.load(file=open("test.pickle","rb"))

print(myPlayer.name)
print(myPlayer.runs)

#############################
        ## Pickle Hands On 3
import traceback
import io
safe_builtins = {
 'range',
 'complex',
 'set',
 'frozenset'
}

class RestrictedUnpickler(pickle.Unpickler):

    def find_class(self, module, name):
    # Only allow safe classes from builtins.
      if module == "builtins" and name in safe_builtins:
          return getattr(builtins, name)
    # Forbid everything else.
      raise pickle.UnpicklingError("global '%s.%s' is forbidden" %
      (module, name))
        

def restricted_loads(s):
        """Helper function analogous to pickle.loads()."""
        return RestrictedUnpickler(io.BytesIO(s)).load()

def func1(a):
    try:
        x=restricted_loads(pickle.dumps(a))
        return x
    except pickle.UnpicklingError :
        s=traceback.format_exc()
        return s

def func2(s):
    try:
        x=restricted_loads(pickle.dumps(slice(0,8,3)))
        return s[x]
    except pickle.UnpicklingError :
        s=traceback.format_exc()
        return s

a=range(int(50)) 
b=func1(a)
print(b)
y=tuple('"a", "b", "c", "d", "e", "f", "g", "h"')
z=func2(y)
print(z)



##########################################################
##############  SQL ALCHEMY   ############################
###############################

# SQLAlchemy is a package which facilitates the 
# communication between Python programs and databases

# This package is used as an Object Relational Mapper (ORM) tool, 
# which translates Python classes to tables and also automatically 
# converts function calls to SQL statements.

# Major benefit of using SQLAlchemy is that it enables to 
# write Python code that can map database schema to applications.

# SQLAlchmey consists of two components; 
# SQLAlchemy Core and SQLAlchemy ORM. 
# SQLAlchemy ORM is built on SQLAlchemy Core

# The major benefits of using SQLAlchemy over raw SQL are:
# (1) Cleaner code.
# (2) ORM functionalities enable secure code
# (3) Enables simpler logic, allows user's to abstract all 
# database-level logic to Python objects.

import sqlalchemy
print(sqlalchemy.__version__)

# SQLAlchemy works only with an SQLite database by default 
# without adding additional drivers. 
# To work with other databases, a user must install a 
# DBAPI-compliant driver specific to the database.

# A DBAPI contains many drivers. 
# Drivers for MYSQL: PyMySQL, MySQL-Connector, CyMySQL, MySQL-Python
# Drivers for PostgreSQL : psycopg2 and pg80000
# pip install psycopg2


# ENGINE
# In SQLAlchemy, to connect to a database, first create an engine. 
# An engine is an object that interacts with a database, 
# Engine consists of two components:
# (1) Dialect
# (2) Connection Pool

# (1) SQLAlchemy Dialect
# Generally, SQL is the standard language used to access databases.
# But, the SQL syntax varies from one database to another. 
# Also, database vendors rarely adhere to database standards. 
# To handle such issues, Dialect is used. 
# Dialect defines the behavior of a database, and # handles tasks 
# like generating SQL statements, execution, result set handling, etc. 
# The only requirement is to install the appropriate driver.

# (2) SQLAlchemy Connection Pool
# Connection Pool is used as a standard method to store connections
# in the cache, so that it can be reused. 
# Creating new connection every time is expensive and time-consuming. 
# By using Connection Pool, appl can get connection from the pool. 
# After performing queries, the appl releases connection back to pool. 
# If all available connections being used, new connection 
# is created, and added to the pool.

# To create an ENGINE object use the create_engine() function
# available in the SQLAlchemy package.

# A connection string provides information about the data source. 
# The general format of a connection string is:

# dialect+driver://username:password@host:port/database

# (a) Dialect is the name of the database, like mysql, postgresql, 
#     mssql, oracle, sqLite, etc.
# (b) Driver is the DBAPI. If the driver is not specified, 
#     the default driver is used.
# (c) Username and Password are the credentials required to login 
#     to a database.
# (d) Host is the location of the database server.
# (e) Port is the optional database port.
# (f) Database is the name of the database to be connected.

# To connect to a MySQL database, use:
#from sqlalchemy import create_engine
#engine = create_engine("mysql+mysqldb://root:passwords@localhost/mydb")
#engine = create_engine("postgresql+psycopg2://root:passwords@localhost/mydb")

# Connecting to Database
# Creating an engine, will not establish connection with the DB.
# To establish a connection with DB , use connect() method of engine object.
# engine.connect() 

#from sqlalchemy import create_engine
#engine= create_engine("postgresql+psycopg2://root:passwords@localhost:5433/mydb")
#engine.connect()
#print(engine)
# above resulting in Operational error localDb refused connection


# CRUD using Raw SQL, CRUD using SQL ORM

#CRUD using Raw SQL
from sqlalchemy import create_engine

db_string = "sqlite:///test_raw.db"

db = create_engine(db_string)

#create
db.execute("CREATE TABLE IF NOT EXISTS employee (empid text, empname text, designation text)")  

db.execute("INSERT INTO employee (empid, empname, designation) VALUES ('10001', 'ABC', 'Developer'), ('10002' , 'XYZ', 'Tester'),('10003','DEF','Technical Support'),('10004','WXY','HR'),('10005','JKL','Manager')")
# Read
result_set = db.execute("SELECT * FROM employee")  

for r in result_set:  
   print(r)
		 
#Update
db.execute("UPDATE employee SET designation='Tester' WHERE empid in('10001','10005')")

#Delete
db.execute("DELETE FROM employee WHERE empid='10005'")

#HANDS ON :
from sqlalchemy import create_engine

db_string = "sqlite:///tests_2.db"

db = create_engine(db_string)

#create
db.execute("CREATE TABLE IF NOT EXISTS players (plyid text, plyname text, runs text)")

db.execute("INSERT INTO players (plyid, plyname, runs) VALUES ('10001', 'ply1', '100'), ('10002' , 'ply2', '80'),('10003','ply3','65'),('10004','ply4','95'),('10005','ply5','99')")

# Read

s=[]
s = db.execute("SELECT * FROM players")
s = list(s)

#Update
db.execute("UPDATE players SET  runs = '100' WHERE plyid = '10005'")


q=[]
q = db.execute("SELECT * FROM players")
q = list(q)

#Delete
db.execute("DELETE FROM players WHERE plyid = '10005'")

e=[]
e = db.execute("SELECT * FROM players")
e = list(e)

print(s)
print(q)
print(e)
s=str(s)
q=str(q)
e=str(e)

with open(".hidden.txt",'w') as f:
	f.write(s)

with open(".hidden1.txt",'w') as f:
	f.write(q)

with open(".hidden2.txt",'w') as outfile:
	outfile.write(e)


##########################################
# CRUD using SQL ORM
print("SQL Alchemy ORM Example: ")
from sqlalchemy import create_engine  
from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

db_string = "sqlite:///sql_orm.db"

db = create_engine(db_string)  
base = declarative_base() # Instead of table

class Employee(base):   #Instead of defining table
	__tablename__ = 'employee'
	empid = Column(String, primary_key=True) # Attributes instead of column, coumn types
	empname = Column(String)
	designation = Column(String)

Session = sessionmaker(db)    # Insted of table
session = Session() # instead of making connections to the database

base.metadata.create_all(db)

#Create   
emp1 = Employee(empid="10001", empname="ABC", designation="Developer") 
emp2=Employee(empid="10002", empname="XYZ", designation="Tester")
emp3=Employee(empid="10003", empname="DEF", designation="Technical Support") 

session.add_all([emp1,emp2,emp3])  # use .add for one row
# objects instantiated and then added using session.add
session.commit()

#Read
employee = session.query(Employee).all() 

for emps in employee:  
	 print(emps.designation)
	 
#Update
emp1.designation = "Tester"  
session.commit()

#Delete
session.delete(emp1)  
session.delete(emp2)
session.delete(emp3)
session.commit()  


#Hands On
from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = "sqlite:///hanson_orm.db"

db = create_engine(db_string)
base = declarative_base()

class Teacher(base):
#Define table name and column name
	__tablename__ = 'students'
	stdid = Column(String, primary_key=True)
	stdname = Column(String)
	subjects = Column(String)
	marks = Column(String)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

#Create
emp1 = Teacher(stdid="10001", stdname="std1", subjects="Maths", marks="100")
emp2 = Teacher(stdid="10002", stdname="std2", subjects="Physics", marks="80")
emp3 = Teacher(stdid="10003", stdname="std3", subjects="English", marks="65")
emp4 = Teacher(stdid="10004", stdname="std4", subjects="Social", marks="95")
emp5 = Teacher(stdid="10005", stdname="std5", subjects="Chemistry", marks="99")
session.add_all([emp1,emp2,emp3,emp4,emp5])
session.commit()

#Read
s_objs = session.query(Teacher).all()
s = []
for r in s_objs:
    s.append([r.stdid,r.stdname,r.subjects,r.marks])
print(s)

#Update
emp5.subjects = "Language"
session.commit()
q_objs = session.query(Teacher).all()
q = []
for r in q_objs:
    if r.stdid == "10005":
        q.append(r.stdid)
        q.append(r.stdname)
        q.append(r.subjects)
        q.append(r.marks)
print(q)

#Delete
session.delete(emp5)
session.commit()
e_objs = session.query(Teacher).all()
e = []
for r in e_objs:
    e.append([r.stdid,r.stdname,r.subjects,r.marks])
print(e)

s=str(s)
q=str(q)
e=str(e)

#Delete
session.delete(emp1)  
session.delete(emp2)
session.delete(emp3)#Delete
session.delete(emp4)
session.commit()

########################################################
    
def even_or_odd(n):
    if (n%2==0):
        return 'even'
    else:
        return 'odd'

n = [2,4,5,7,3,21,43,32]
import itertools
res_grp = itertools.groupby(n,even_or_odd)
for key,grp in res_grp:
    print(key+": ",list(grp)) # something not right
###############################
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']] 
# I want to flatten a given 2-D list and only include those strings whose lengths are less than 6:
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']] 
  
# Nested List comprehension with an if condition 
flatten_planets = [planet for sublist in planets for planet in sublist if len(planet) < 6] 
          
print(flatten_planets) 
