# FUNCTION
# piece of code, capable of performing a similar task repeatedly
def square(x):
    'Returns square of a number.'
    return x**2

print(square(3))
print(help(square))

# ITERATOR
# object, to traverse through all the elements of a 
# collection. Values can be accesses once only and in sequence
x = [6, 3, 1]
s = iter(x)            
print(next(s))      # -> 6
print(next(s))      # -> 3

x = [1,2,3,4,5]
s = iter(x)
while True:
    try:
        print(next(s))
    except StopIteration:
        break;

## LIST Comprehensions
## Alternative to for loops
## More concise, readable, efficient and mimic functional programming style
## Used to 
## Apply a method to all or specific elements of a list,
## Filter elements of a list satisfying specific criteria
x = [6, 3, 1]
y = [ square(i) for i in x ]   # List Comprehension expression
print(y)
##########################################
## GENERATOR
# Generator object is an iterator, whose values are 
## created at the time of accessing them.
x = [6, 3, 1]
g = (square(i) for i in x)  # generator expression
print(next(g))         # -> 36
print(next(g))         # -> 9

######
def gen_func():
    yield 1
    yield 2
    yield 3
print(type(gen_func()))
gen1 = gen_func()
print(next(gen1))
print(next(gen1))
#############################