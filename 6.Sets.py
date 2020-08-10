###################
## SETS
###################
# collection of unordered, unique, 
# unindexed elements (So can't do indexing ops)
######################
st1 = {21,44.5,'Cranberry','Life of a berry','axe'}
st2 = set([26,7.3,'Tomato','Life of a fruit','axe'])
st3 = set()
print('set 1:', st1)
# {'axe', 'Life of a berry', 'Cranberry', 44.5, 21}
print('set 2:', st2)
# {'Tomato', 'axe', 7.3, 'Life of a fruit', 26}
print('set 3:', st3)
# set()

print(dir(st1)) ## Gives all methods i can use on set

print('*************************************')
print('Length of set:',len(st1),len(st2),len(st3))
# Length of set: 5 5 0
print('*'*40)
print('Accessing elements in a set')
for el in st1:
    print(el)
# prints all elements in set st1  
print('*************************************')
print('Adding One element to a set')
print(st1)
# {'axe', 'Life of a berry', 'Cranberry', 44.5, 21}
st1.add('Lake') # Adds
st1.add(44.5)   # Does not add (coz sets are unique)
print(st1)
# {'axe', 'Lake', 'Life of a berry', 'Cranberry', 44.5, 21}
print('*************************************')
print('Adding multiple elements in a set')
print(st2)
# {'Tomato', 'axe', 7.3, 'Life of a fruit', 26}
st2.update(['Soil','India',7.3]) # Adds
print(st2)
# {'Tomato', 'axe', 7.3, 'Life of a fruit', 'India', 'Soil', 26}
print('*************************************')
print('Removing elements from a set')
print(st2)
# {'Tomato', 'axe', 7.3, 'Life of a fruit', 'India', 'Soil', 26}
st2.remove('Soil') # If element not found, throws error
st2.discard('Soil') # No error if element not found
#st2.pop() # Removes random element from the set
print(st2)
# {'Tomato', 'axe', 7.3, 'Life of a fruit', 'India', 26}
print('*************************************')
print('Union of sets')
print(st1|st2)  # can use a|b|c
print(st1.union(st2)) # can also use a.union(b,c)
# {'Tomato', 'axe', 'Lake', 'Life of a berry', 'Cranberry', 7.3, 44.5, 'Life of a fruit', 'India', 21, 26}
print('*************************************')
print('Intersection of sets')
print(st1&st2) 
print(st1.intersection(st2)) 
# {'axe'}
print('*************************************')
print('Difference of sets') 
#Elements in st1 but not common elements of a and b
# i.e. Elements in a but not in b
print(st1-st2) 
print(st1.difference(st2)) #can use a.difference(b,c)
# {'Lake', 'Life of a berry', 'Cranberry', 44.5, 21}
print('*************************************') 
print('Frozen set') 
# Elements can't be modified. Is immutable. 
# Used for set of keys in dictionary
st4=frozenset(st1)
print(st4)
# frozenset({'axe', 'Lake', 'Life of a berry', 'Cranberry', 21, 44.5})
# st4.add('abc') Will get attrbibute error