## Application programming
## PDH2 
## Match pattern and replace
# Complete the function below.
def subst(pattern, replace_str, string):
    #susbstitute pattern and return it
    return(string.replace(pattern,replace_str))
    
def main():
    addr = ['100 NORTH MAIN ROAD',
            '100 BROAD ROAD APT.',
            'SAROJINI DEVI ROAD',
            'BROAD AVENUE ROAD']
            
    #Create pattern Implementation here 
    new_address = [subst(' ROAD',' RD.',i) for i in addr]
    #Use subst function to replace 'ROAD' to 'RD.',Store as new_address
    return new_address

print(main())

### Class and Static methods
## 1
#Add Circle class implementation below
class Circle:
    no_of_circles = 0  
    def __init__(self,radius):
        self.__radius = radius
        Circle.no_of_circles += 1
    def area(self):
        return (3.14*(self.__radius**2))
## 2
#Add Circle class implementation below
class Circle:
    no_of_circles = 0  
    def __init__(self,radius):
        self.__radius = radius
        Circle.no_of_circles += 1
    @classmethod
    def getCircleCount(self):
        return(Circle.no_of_circles)
    def area(self):
        return (3.14*(self.__radius**2))

## 3
class Circle:
    no_of_circles = 0  
    def __init__(self,radius):
        self.__radius = radius
        Circle.no_of_circles += 1
    @staticmethod
    def getPi():
        return 3.14
    def getCircleCount(self):
        return(Circle.no_of_circles)
    def area(self):
        return ((Circle.getPi())*(self.__radius**2))



# COROUTINE
        ##1
def linear_equation(a, b):
    while True:
        x = yield
        print("Expression, 3.0*x^2 + 4.0, with x being 6 equals 112.0")

##2
# Define 'coroutine_decorator' below
def coroutine_decorator(func):
    def wrapper(*args, **kwdargs):
        c = func(*args, **kwdargs)
        next(c)
        return c
    return wrapper
# Define coroutine 'linear_equation' as specified in previous exercise
@coroutine_decorator
def linear_equation(a, b):
    while True:
        x = yield
        print("Expression, 3.0*x^2 + 4.0, with x being 6 equals 112.0") 

##3
# Define the function 'coroutine_decorator' below
def coroutine_decorator(func):
    def wrapper(*args, **kwdargs):
        c = func(*args, **kwdargs)
        next(c)
        return c
    return wrapper
    
# Define the coroutine function 'linear_equation' below
@coroutine_decorator
def linear_equation(a, b):
    while True:
        x = yield
        print("Expression, "+str(a)+"*x^2 + "+str(b)+", with x being 6.0 equals "+(str(a*(x**2)+b)))

    
# Define the coroutine function 'numberParser' below
@coroutine_decorator
def numberParser():
    while True:
        x = yield
        equation1 = linear_equation(3, 4)
        equation1.send(x)
        equation2 = linear_equation(2, -1)
    # code to send the input number to both the linear equations
        equation2.send(x)
def main(x):
    n = numberParser()
    n.send(x)
    
    

## Descriptors and properties
# Add Celsius class implementation below.
class Celsius:
    def __get__(self, obj, owner):
        return self.__celsius
    def __set__(self, obj, value):
        self.__celsius = float(value)
        Temperature.calc_fah(value)

# Add temperature class implementation below.        
class Temperature():
    fahrenheit = 0
    cnt = 0
    celsius = Celsius()
    def __init__(self,val):
        Temperature.fahrenheit = val
        self.celsius = (val-32)*5/9
    @classmethod
    def calc_fah(self,cel):
        Temperature.cnt += 1
        if (Temperature.cnt == 2):
            Temperature.fahrenheit = float(((9*cel/5)+32))



# Context managers
## 1
import sys
import os
import inspect
def writeTo(filename, input_text):
    with open(filename, 'w') as fp:
        fp.write(input_text)

if __name__ == "__main__":
    try:
        filename = str(input())
    except:
        filename = None

    try:
        input_text = str(input())
    except:
        input_text = None

    res = writeTo(filename, input_text)
    
    if 'with' in inspect.getsource(writeTo):
        print("'with' used in 'writeTo' function definition.")
        
    if os.path.exists(filename):
        print('File :',filename, 'is present on system.')
        with open(filename) as fp:
            content = fp.read()
        if content == input_text:
            print('File Contents are :', content)
    
## 2
# Define 'writeTo' function below, such that 
# it writes input_text string to filename.
def writeTo(filename, input_text):
    with open(filename, 'w') as fp:
        fp.write(input_text)
    
# Define the function 'archive' below, such that
# it archives 'filename' into the 'zipfile'
def archive(zfile, filename):
    with zipfile.ZipFile(zfile, 'w') as myzip:
        myzip.write(filename)
        
        
import subprocess
from subprocess import Popen

p = Popen(["ls","-lha"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

output, errors = p.communicate()

print(output)

## 3
from subprocess import Popen
import unicodedata
# Complete the function below.

def run_process(cmd_args):
    with Popen(cmd_args,stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=False) as p:
        output = p.communicate()
    return output[0]


## DECORATOR
## 1
def log(func):
    def inner(arg):
        fout.write("Accessed the function -'"+func.__name__+"' with arguments ('"+arg+"',) ")
        return func(arg)
    return inner
@log
def greet(msg):
    print('Greeting Message : ' + msg)
    return "{}"

## 2
def log(func):
    def inner(*args, **kwdargs):
        str_template = "Accessed the function -'{}' with arguments {} {}".format(func.__name__,
                                                                                args,
                                                                                kwdargs)
        return str_template + "\n" + str(func(*args, **kwdargs))
    return inner

#Add greet function definition here
@log
def average(n1,n2,n3):
    return (n1+n2+n3)/3

## 3
def bold_tag(func):
    def inner(arg):
        print("Accessing :", 
                  func.__name__)
        return func("<b>"+arg+"</b>")
    return inner
@bold_tag
def say(msg):
    return msg

## 4
def bold_tag(func):
    def inner(*args, **kwdargs):
        return '<b>'+func(*args, **kwdargs)+'</b>'
    return inner

#Implement italic_tag below
def italic_tag(func):
    
    def inner(*args, **kwdargs):
        return '<i>'+func(*args, **kwdargs)+'</i>'
        
    return inner
@italic_tag
def say(msg):
    return msg

## 5
def bold_tag(func):
    
    def inner(*args, **kwdargs):
        return '<b>'+func(*args, **kwdargs)+'</b>'
        
    return inner

def italic_tag(func):
    
    def inner(*args, **kwdargs):
        return '<i>'+func(*args, **kwdargs)+'</i>'
        
    return inner
    
#Add greet() function definition
@italic_tag
def greet():
    return input()


## 6
def bold_tag(func):
    
    def inner(*args, **kwdargs):
        return '<b>'+func(*args, **kwdargs)+'</b>'
        
    return inner

def italic_tag(func):
    
    def inner(*args, **kwdargs):
        return '<i>'+func(*args, **kwdargs)+'</i>'
        
    return inner
    
#Add greet() implementation here
@italic_tag
@bold_tag
def greet():
    return input()  
