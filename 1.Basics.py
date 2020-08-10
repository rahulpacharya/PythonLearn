##############################
# Simple for loop
for i in range(1,3):
    print("In for loop - looping: ",i)
##############################
# Square of a number
x=3    
#x=int(input("Enter an integer: "))
# Got to convert input default string to integer
print("Square of your input is: ",x**2)
##############################
# Accepting arguments
import sys
print("Sys.argv[0] is : ",sys.argv[0])
## sys.argv[0] is the name of the file itself
## sys.argv[1] only relevant if you pass an argument when running this file
##############################
# Data types
print(type(3)) # <class 'int'>
print(type(-3)) # <class 'int'>
print(type(3.0)) # <class 'float'>
print(int('3'))  # 3
print(int(3.4))  # 3
print(int(3.9))  # 3
print(int(-6.5)) # -6
print(1j)  # 1j
#print(int(1j)) #TypeError: can't convert complex to int
print(float(5))  # 5.0
print(float('5'))  # 5.0
print(7.6+8.7)  # 16.299999999999997 not 16.3
## because of underlying C lang stores this as fractions
print(round(7.6+8.7))  # 16
print(round(7.6+8.7,1)) # 16.3    # round to 1 decimal

if (1.1+1.1+1.1 == 3.3):
    print('They are equal')
else:
    print('They are unequal')  
# this prints 'They are unequal, unless you use round(val,1)

print(1.1+1.1)  # 2.2
print(1.1+1.1+1.1)  # 3.3000000000000003
# again because of reason stated earlier
##############################
print("Maf opers")
a=3.0
b=7.0
c=2
d=4
print(a+b) # 10.0
print(a-b) # -4.0
print(a*b) # 21.0
print(a/b) # 0.42857142857142855
print(c/d) # 0.5
print(d/c) # 2.0
print(b%a) # 1.0
## Boolean
if a == b:
    print(True)
else:
    print(False)
# prints False
    
if a != b:
    print(True)
else:
    print(False)
# prints True

print(a>b)
# Prints False
# Returns boolean value
##############################
# Converting int/string to bool
print("Boolean conversions")
print(bool(-28)) #True
print(bool(3))   #True
print(bool(0))   #False     
# Only 0 converted to False. 
# All other numbers to True.
print(bool("Alan")) #True
print(bool(" "))    #True
print(bool(""))     #False  
# Only empty string converted to False. 
# All other string converted to True

# Converting bool to integer
print(int(True))  #1
print(int(False)) #0
print(5+True) #6
##############################

## LOOPS ##
###########
sum = 0
for i in range(5):
    sum = sum + i
print(sum)  #10
##################
sum = 0
i = 0
while i<5:
    sum = sum + i
    i += 1
print(sum) #10
##################
# Find sum of first 10 natural numbers
total = 0
for i in range(1,11):
    total += i
print(total)  #55
##################

#################
## RANGE
## range(start,end,step)
#######
l1 = [0,1,2,3,4,5]
l2 = list(range(6))
print(l1) #[0, 1, 2, 3, 4, 5]
print(l2) #[0, 1, 2, 3, 4, 5]
print(list(range(1,11))) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#######
t1 = tuple(range(1,11))
print(t1) #(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
t2 = tuple(range(1,11,2))
print(t2) #(1, 3, 5, 7, 9)
#################