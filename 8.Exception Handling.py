## Handling exceptions
######
### using try..except
#####################
# The code to be handled is written inside try clause 
# and the code to be executed when an exception occurs 
# is written inside except clause.
try:
    a = pow(2, 4)
    print("Value of 'a' :", a)
    b = pow(2, 'hello')   # results in exception
    print("Value of 'b' :", b)
    c = 2/10
    print("Value of 'c' : ", c)
except TypeError as e:
    print('oops!!! is type errorerrr')
except ZeroDivisionError as e:
    print('oops!!! is 0div errorerrr')
print('Out of try ... except.')

# raise keyword is used when a programmer wants a 
# specific exception to occur
try:
    raise TypeError("Simply raising")
except TypeError as e:
    print(e)

try:
    a = 2; b = "d2"
    if not (isinstance(a,int) and isinstance(b,int)):
        raise TypeError("input must be integers")
    print(a+b)
except TypeError as e:
    print(e)
##############################
## Can create custom exceptions, derived from 
## base Exception class.
class CustomError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

try:
    a = 2; b = 'hello'
    if not (isinstance(a, int) and isinstance(b, int)):
        raise CustomError('inputs must be integers')
    c = a**b
except CustomError as e:
    print(e)
#################################
## finally can be optionally used with try..except
## all stmt in finally will be executed
def divide(a,b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Dividing by Zero error.")
    finally:
        print("In finally clause.")

print('First call')
print(divide(14, 7))
# In finally clause.
# 2.0
print('Second call')
print(divide(14, 0))
# Dividing by Zero error.
# In finally clause.

##################################
## else can be optionally used with try..except
## executed only when no exception occurs in try clause.
try:
    a = 14 / 7
except ZeroDivisionError:
    print('oops!!!')
else:
    print('First ELSE. SO no except-ion occured')
# First ELSE. SO no except-ion occured
try:
    a = 14 / 0
except ZeroDivisionError:
    print('oops!!!')
else:
    print('Second ELSE')
################################