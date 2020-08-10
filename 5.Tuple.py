##### TUPLE
#################
## Similar to list, but immutable
#################
tup = (1, 'Iron Man', 'Red and Gold')
print(tup) #(1, 'Iron Man', 'Red and Gold')
print(tup[1]) # Iron Man
print(tup[0:]) # (1, 'Iron Man', 'Red and Gold')
print(len(tup)) # 3

str1 = "welcome home" 
tuple1 = tuple(str1)  
## Have to pass iterable, like string or list or dictionary

print(tuple1)
# ('w', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 'h', 'o', 'm', 'e')

print('number of e in tuple',tuple1.count('e'))
# number of e in tuple 3

print('length of tuple: ',len(tuple1))
# length of tuple:  12

print('index of e in tuple: ',tuple1.index('e'))
# index of e in tuple:  1

dict1 = { 1 : 'one', 2 : 'two' }  
tuple2 = tuple(dict1) 
print(tuple2) # (1, 2)
