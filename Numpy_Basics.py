# NumPy
# An essential library used for scientific computing in Python.
# Holds data in N-dimensional array (ndarray) objects, 
# which can store data in multiple dimensions.

# Supports performing efficient array operations through 
# Broadcasting feature.

# Each data element of a ndarray is of fixed size.
# All elements of a ndarray are of same data type.
######################################################
# pandas
# Provides functionality to deal with structured data.
# Stores Data in different Primary data structures: 
# Series, DataFrame and Panel.
######################################################
# N-dimensional array is an object, capable of holding 
# data elements of same type and of a fixed size in 
# multiple dimensions.

# Creation of a 1-D array of five elements,
import numpy as np
x = np.array([5, 8, 
              9, 10, 
              11]) # using 'array' method

print(type(x))   # Displays type of array 'x'
print(x) 

# Creation of 2-d array
y = np.array([[6, 9, 5], 
              [10, 82, 34]])  
print(y)
# Important attributes
print('Number of dimensions: ',y.ndim)
print('Shape in tuple: ',y.shape)
print('Total number of elements: ',y.size)
print('Type of each element: ',y.dtype)
print('Size of each element in Bytes: ',y.itemsize)
print('Total bytes consumed by all elements: ',y.nbytes)

# Data type can be explicitly specified with dtype argument.
y = np.array([[6, 9, 5],
              [10, 82, 34]], 
             dtype='float64')  
print(y)
print(y.dtype)

# Creation of 3-d array
a = [[[4.1, 2.5], [1.1, 2.3], [9.1, 2.5]], 
     [[8.6, 9.9],[3.6, 4.3], [6.6, 0.3]]]
x = np.array(a, dtype='float64')
print(x)
print(type(x), x.ndim, x.shape)

# creation of arrays with default values like 0, 1, or another value.
# using zeros methos
x = np.zeros(shape=(2,4))
print(x)
# using full method
y = np.full(shape=(2,3), fill_value=10.5)
print(y)

# Define a ndarray x2, whose shape is (3, 2, 2) 
#and contains all 1's.
z = np.full(shape=(3,2,2), fill_value=1)
print(z)

# Create new array based on shape of different array
x = np.array([[-1,0,1], [-2, 0, 2]])
y = np.zeros_like(x)
print(y)

# Numeric Sequence Generators
# (1) arange : Numbers created based on step value
# Syntax - numpy.arange([start, ]stop, [step, ]dtype=None)
x = np.arange(3, 15, 2.5) # 2.5 is step
print(x)

# (2) linspace : Numbers created based on size value.
# Syntax - numpy.linspace(start, stop, #num inbetween, endpoint=True, retstep=False, dtype=None)
y = np.linspace(3, 15, 5) # 5 is size of array 'y'
print(y)

# Random Numbers Generator
# random module of numpy is used to generate various random sequences.
np.random.seed(100) # setting seed
x = np.random.rand(2) # 2 random numbers between 0 and 1
print(x)
# Until you reset the seed, already generated nos wont repeat
# seed is actually used to multiple divide whatever to generate number
np.random.seed(100) # setting seed
y = np.random.randint(10, 50, 3) # 3 random integers between 10 and 50
print(y)

# Simulating Normal Distribution
# randn is used to simulate standard normal distribution
np.random.seed(100)
x = np.random.randn(3) # Standard normal distribution
print(x)

np.random.seed(100)
x = 10 + 2*np.random.randn(3) # normal distribution with mean 10 and sd 2
print(x)

# loadtxt is used to read data from a text file or any input data stream.
from io import StringIO
import numpy as np
x = StringIO('''88.25 93.45 72.60 90.90
72.3 78.85 92.15 65.75
90.5 92.45 89.25 94.50
''')
d = np.loadtxt(x,delimiter=' ')
print(d)
print(d.ndim, d.shape)
##############################################
print("*"*30)
# Reshaping ndarrays
# Shape of an array can be changed using reshape.
np.random.seed(100)
x = np.random.randint(10, 100, 8)
print(x, end='\n\n')

y = x.reshape(2,4)
print(y, end='\n\n')

z = x.reshape(2,2,2)
print(z, '\n\n')

print("*"*30)
# Stacking arrays vertically
# Two or more arrays can be joined vertically using the 
# generic vstack method.

x = np.array([[-1, 1], [-3, 3]])
y = np.array([[-2, 2], [-4, 4]])
print(np.vstack((x,y)))

# Stacking arrays horizontally
# Two or more arrays can be joined horizontally using the 
# generic hstack method.
x = np.array([[-1, 1], [-3, 3]])
y = np.array([[-2, 2], [-4, 4]])
z = np.array([[-5, 5], [-6, 6]])
print(np.hstack((x,y,z)))

# Splitting arrays vertically
# Arrays can be split vertically using the generic 
# vsplit method.

x = np.arange(30).reshape(6, 5)
print(x)
res = np.vsplit(x, 2)
print(res[0], end='\n\n')
print(res[1])

# It is also possible to split at specific row numbers using vsplit.
# Example : Spliting Vertically into three arrays

x = np.arange(30).reshape(6, 5)
print(x)
res = np.vsplit(x, (2, 5))
print(res[0], end='\n\n')
print(res[1], end='\n\n')
print(res[2])

# Splitting arrays Horizontally
# Arrays can be split horizontally using the generic 
# hsplit method.
print("*"*30)
x = np.arange(10).reshape(2, 5)
print(x)
res = np.hsplit(x, (2,4))
print(res[0], end='\n\n')
print(res[1], end='\n\n')
print(res[2])


#########################################
## Basic Operations with Scalars
# Operations in Numpy are carried out element wise.
# Hence the expression x + 10, increases every element 
# of array x by 10.

x = np.arange(6).reshape(2,3)
print(x + 10, end='\n\n')
print(x * 3, end='\n\n')
print(x % 2)

# Operations between arrays also happen element wise.
x = np.array([[-1, 1], [-2, 2]])
y = np.array([[4, -4], [5, -5]])
print(x + y, end='\n\n')
print(x * y)

# Also possible to perform operations on arrays 
# with varying size and shape.
# This is due Broadcasting feature exhibited by numpy arrays.
x = np.array([[-1, 1], [-2, 2]])
y = np.array([-10, 10])
print(x * y)

# Broadcasting in NumPy
# Element wise operations between arrays are possible 
# only when they have the same shape 
# or 
# compatible for Broadcasting.

# Steps followed to verify the feasibility of Broadcasting 
# between arrays are:

# (1) Initially, compare the dimensions of all arrays.

# (2) If dimensions do not match, prepend 1's to shape of a 
# smaller array so that it matches dimensions of a larger array.

# (3) Start comparing array shapes from the last dimension 
# and move backward.

# (4) If the shape of both arrays are equal 
# or either of it has a shape of 1, continue the comparison.

# (5) Else at any dimension, if step 4 fails, broadcasting 
# between arrays is not feasible.

# (6) Finally, the resulted broadcasting array shape 
# would be maximum of two compared shapes in each dimension.

# Below examples show feasibility of broadcasting 
# between two arrays, having shape s1 and s2 respectively.
# s1 and s2 are shapes - remember
# Given: s1 = (4, 3); s2 = (3,)
# Step 1 and 2: s1 = (4, 3); s2 = (1, 3)
# Step 3 and 4: pass in 2 dimensions
#Result : Broadcasting feasible;
 #        resulted array shape - (4,3) 

# Given: s1 = (5,); s2 = (5,4,3)
# Step 1 and 2: s1 = (1, 1, 5); s2 = (5, 4, 3)
# Step 3 and 4: fail in last dimension. ( 5 != 3)
# Result : Broadcasting not feasible. 
######################################################
# NumPy Universal Functions
# Provides a lot of mathematical functions, in the form of 
# Universal functions.

x = np.array([[0,1], [2,3]])
print(np.square(x), end='\n\n')
print(np.sin(x))

# NumPy Array Methods
# Many of the universal functions are available as 
# methods of ndarray class.

# By default sum method adds all array elements.
# It is also possible to apply sum method on elements 
# of a specific dimension, using axis argument.

x = np.array([[0,1], [2, 3]])
print(x.sum(), end='\n\n')
print(x.sum(axis=0), end='\n\n')
print(x.sum(axis=1))

# Slicing refers to extracting a portion of existing array.
# This can be achieved with a slice object.
# A slice object is of the form start:end:step. 
# All three are optional.
# Having only a single number inside square brackets 
# refer to start index.
x = np.array([5, 10, 15, 20, 25, 30, 35])
print(x[1])  # Indexing
print(x[1:6]) # Slicing
print(x[1:6:3]) # Slicing

# Two slice objects, one for each dimension, are required 
# to slice a 2-D array.
# They are separated by a comma (,) and having only a 
# single slice object inside square brackets refers 
# to first dimension.
# All elements of a single dimension can be referred
# with a colon (:).
y = np.array([[0, 1, 2],
              [3, 4, 5]])
print(y[1:2, 1:3]) 
print(y[1])   
print(y[:, 1])

#Slicing Higher Dimensions ndarrays
#For slicing an n dimensional ndarray, n slice objects 
# are required.
#Having only a single slice object refers to first dimension.
z = np.array([[[-1, 1], [-2, 2]],
              [[-4, 4], [-5, 5]],
              [[-7, 7], [-9, 9]]])
print(z[1,:,1]) # index 1 element in row of index 1
print(z[1:,1,:]) # From all outer rows except the first, select 1st index element (which itself is an array) completely.
print(z[2]) # print 2nd index element

# Iterating using 'for'
# for loop can be used to iterate over every 
# dimensional element.
x = np.array([[-1, 1], [-2, 2]])
for row in x:
    print('Row :',row)
    
# Iterating using 'nditer'
# nditer method of numpy creates an iterator, which 
# enable accessing each element one after the other.

x = np.array([[0,1], [2, 3]])
for a in np.nditer(x):
    print(a)

# Boolean Indexing
# Checking if every element of an array satisfies a condition,
# results in a Boolean array.
# This Boolean array can be used as index to filter 
# elements that satisfy the condition.
x = np.arange(10).reshape(2,5)
print(x)
condition = x % 2 == 0
print(condition)
print(x[condition])

x = np.arange(4).reshape(2,2)
print(np.isfinite(x))