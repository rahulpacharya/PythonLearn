######################################
#### Higher order functions###########
######################################
#### A Higher Order function is a function that can 
## function as a data and be assigned to a variable.
## Can accept any other function as an argument.
## Can return a function as its result.
######################################
## Ability to build Higher order functions, 
## allows a programmer to create Closures, 
## which in turn are used to create Decorators.
######################################

### Function as data #######
def greet():
    return 'Hello Everyone!'
print(greet())
wish = greet        # 'greet' function assigned to variable 'wish'
print(type(wish))   
print(wish())
########################################
### Function as argument #####
def add(x, y):
    return x + y
def sub(x, y):
   return x - y
def prod(x, y):
    return x * y
def do(func, x, y):
   return func(x, y)
print(do(add, 12, 4))  # 'add' as arg
print(do(sub, 12, 4))  # 'sub' as arg
print(do(prod, 12, 4))  # 'prod' as arg
########################################
### Function as return argument ######
def outer():
    def inner():
        s = 'Hello world!'
        return s            
    return inner()    

print(outer())
########################################
########################################
### Function as return argument ######
def outer():
    def inner():
        s = 'Hello world!'
        return s            
    return inner    

print(outer())
func = outer()
print(type(func))
print(func())
########################################
########################################
### Closure : is a function returned by a higher order function,
#### whose return value depends on 
#### the data associated with the higher order function.
########################################
def multiple_of(x):
    def multiple(y):
        return x*y
    return multiple
c1 = multiple_of(5)  # 'c1' is a closure
c2 = multiple_of(6)  # 'c2' is a closure
print(c1(4))
print(c2(4))
########################################
def current_battery_power(power_left):
    def check_battery(model):
        if model == 'SAMSUNG':
            return (power_left*8)/100
        if model == 'iPhone':
            return (power_left*6)/100
    return check_battery
p1 = current_battery_power(40)
p2 = current_battery_power(50)
print(p1)
print(p2)
print(p1('SAMSUNG'))
print(p2('iPhone'))
########################################
def detecter(element):
    def isIn(sequence):
        if (element in sequence):
            return True
        else:
            return False
    return isIn
#Write closure function implementation for detect30 and detect45
detect30 = detecter(30)
detect45 = detecter(45)

print(detect30([2,30,45,6]))
print(detect45([2,30,45,6]))
print(detect30([8,30,4,6]))
print(detect45([8,30,4,6]))
########################################
def factory(n):
    def current():
        return n
    def counter():
        return(n + 1)
    return current,counter
    return counter

f_current, f_counter = factory(89)
print(f_current())
print(f_counter())
########################################
### Decorator function : evolved from concept of closures
### It is a higher order function that takes a function
### as an argument and returns the inner function.
######################
### Capable of adding extra functionality to an existing 
### function, without altering it.
######################
## The decorator function is prefixed with @ symbol 
## and written above the function.
######################
### Creation of closure function wish using the 
### higher order function outer.
def outer(func):
    def inner():
        print("Accessing :", 
                  func.__name__)
        return func()
    return inner
def greet():
   print('Hello!')
wish = outer(greet)
wish()
### Creation of decorator function outer, which is used to 
### decorate function greet. This is achieved with a 
### small change to Example1.
def outer(func):
    def inner():
        print("Accessing :", 
                  func.__name__)
        return func()
    return inner
def greet():
   return 'Hello!'
greet = outer(greet) # decorating 'greet'
greet()  # calling new 'greet'

### Shows decorating the greet function with 
### decorator function, outer, using @ symbol.
def outer(func):
    def inner():
        print("Accessing :", 
                func.__name__)
        return func()
    return inner
@outer
def greet():
    return 'Hello!'
greet()
############################################
## CO-ROUTINE
############################################
## A Coroutine is generator which is capable of 
## constantly receiving input data, process input data 
## and may or may not return any output
###############
## Are majorly used to build better Data Processing Pipelines.
###############
## Similar to a generator, execution of a coroutine stops
## when it reaches yield statement
##############
## send method is used to send any input value, 
## which is captured by yield expression.
##############
## TokenIssuer is a co-routine function. 
## It uses Yield to accept the name as input
def TokenIssuer():
    tokenId = 0
    while True:
        name = yield
        tokenId += 1
        print('Token number of', name, ':', tokenId)
t = TokenIssuer()
next(t)   ##--> without this stmt, this wont work
t.send('George')
t.send('Rosy')
t.send('Smith')
## Execution of coroutine function begins only when 
## next is called on coroutine t
#############
## This results in the execution of all the statements 
## till a yield statement is encountered
#############
## Further execution of function resumes when 
## an input is passed using send, and processes all statements 
## till next yield statement.
#############################
def TokenIssuer(tokenId=0):
    try:
       while True:
            name = yield
            tokenId += 1
            print('Token number of', name, ':', tokenId)
    except GeneratorExit:
        print('Last issued Token is :', tokenId)
t = TokenIssuer(100)
next(t)
t.send('George')
t.send('Rosy')
t.send('Smith')
t.close()
## You can also pass argument to set starting number for tokens
#####################
## When coroutine t is closed, statements under 
## GeneratorExit block are executed.
##############################################
## Passing input to coroutine is possible only after next stmt
## To avoid programmers from forgetting to use next,
## use decorator as shown below
def coroutine_decorator(func):
    def wrapper(*args, **kwdargs):
        c = func(*args, **kwdargs)
        next(c)
        return c
    return wrapper
@coroutine_decorator
def TokenIssuer(tokenId=0):
    try:
        while True:
            name = yield
            tokenId += 1
            print('Token number of', name, ':', tokenId)
    except GeneratorExit:
        print('Last issued Token is :', tokenId)
t = TokenIssuer(100)
t.send('George')
t.send('Rosy')
t.send('Smith')
t.close()
############################################
