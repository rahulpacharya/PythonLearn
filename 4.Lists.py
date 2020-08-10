###### LIST
#############
## Ordered collection of any type of data
#############
lst = [1,'Rahul Acharya',33]
print(lst) # [1, 'Rahul Acharya', 33]
print(lst[0],lst[1],lst[2]) #1 Rahul Acharya 33
print(lst[0:2])  #Slice  #[1, 'Rahul Acharya']

lst[1] = 'Rahul P Acharya' 
#LIST IS MUTABLE
print("list after name change- ",lst) 
#[1, 'Rahul P Acharya', 33]

lst.pop(2)  
#Can also use lst.pop(-1) : remove last
print("list after delete - ",lst)
# [1, 'Rahul P Acharya']

lst.append(34)
print("list after append - ",lst)
# [1, 'Rahul P Acharya', 34]

lst1 = list()
print(lst1) # []
lst1.append('Leroy!')
print(lst1) # ['Leroy!']
#############

##### SLICING ###
#################
## Way to extract certain elements from list
#################
# Slicing list
# list[start:end:step]
lst1 = ['a','b','c','d','e','f','g']
#        0   1   2   3   4   5   6
#       -7  -6  -5  -4  -3  -2  -1
print(lst1[2:6]) # ['c', 'd', 'e', 'f']
print(lst1[-5:-1]) # ['c', 'd', 'e', 'f']
print(lst1[2:-1])  # ['c', 'd', 'e', 'f']
print(lst1[2:])    # ['c', 'd', 'e', 'f', 'g']
print(lst1[:-1])   # ['a', 'b', 'c', 'd', 'e', 'f']
print(lst1[:])     # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(lst1[1:-1])  # ['b', 'c', 'd', 'e', 'f']
print(lst1[1:-1:1])# ['b', 'c', 'd', 'e', 'f']
print(lst1[1:-1:2]) #['b', 'd', 'f']
print(lst1[-1:1:-1]) # ['g', 'f', 'e', 'd', 'c']
print(lst1[-1:1:-2]) # ['g', 'e', 'c']
print(lst1[::-1])  # REVERSE A LIST ['g', 'f', 'e', 'd', 'c', 'b', 'a']
#################