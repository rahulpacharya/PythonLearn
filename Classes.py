## CLASS
# A template which contains 
# instructions to build an object.
# methods that can be used by the object to exhibit a specific behaviour.
class Person:
    'Represents a person.'  #This is docstring
    def __init__(self, fname, lname): #Initializer method
        'Initialises two attributes of a person.'
        self.fname = fname
        self.lname = lname
p1 = Person('George', 'Smith')   
print(p1.fname, '-', p1.lname)           # -> 'George - Smith'
print(help(Person))



class Planet():
    def __init__(self,radius,weight):
        self.__radius=radius
        self.__weight=weight
    def getArea(self):
        return 4*3.14*(self.__radius**2)
    def getWeight(self):
        return self.__weight
############################
### Descriptors
############################
## Descriptors help created managed attributes. Like getter/setter
## Python allows a programmer to manage the attributes 
## simply with the attribute name, without losing their protection.
## This is achieved by defining a descriptor class, that 
## implements any of __get__, __set__, __delete__ methods.
############################

## The descriptor, EmpNameDescriptor is defined to 
## manage empname attribute.
## It checks if the value of empname attribute is a string or not.
class EmpNameDescriptor:
    def __get__(self, obj, owner):
        return self.__empname
    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError("'empname' must be a string.")
        self.__empname = value
#############################
## The descriptor, EmpIdDescriptor is defined to 
## manage empid attribute.
class EmpIdDescriptor:
    def __get__(self, obj, owner):
        return self.__empid
    def __set__(self, obj, value):
        if hasattr(obj, 'empid'):
            raise ValueError("'empid' is read only attribute")
        if not isinstance(value, int):
            raise TypeError("'empid' must be an integer.")
        self.__empid = value
##############################
class Employee:
    empid = EmpIdDescriptor()           
    empname = EmpNameDescriptor()       
    def __init__(self, emp_id, emp_name):
        self.empid = emp_id
        self.empname = emp_name

e1 = Employee(123456, 'John')
print(e1.empid, '-', e1.empname)  
e1.empname = 'Williams'
print(e1.empid, '-', e1.empname)
## e1.empid = 76347322  ## this will result in the ValueError

################################
### Descriptors can also be created using property() type.
################################
class Employee:
    def __init__(self, emp_id, emp_name):
        self.empid = emp_id
        self.empname = emp_name
    def getEmpID(self):
        return self.__empid
    def setEmpID(self, value):
        if not isinstance(value, int):
            raise TypeError("'empid' must be an integer.")
        self.__empid = value
    empid = property(getEmpID, setEmpID)
# empid attribute created using property
    
    def getEmpName(self):
        return self.__empname
    def setEmpName(self, value):
        if not isinstance(value, str):
            raise TypeError("empname' must be a string.")
        self.__empname = value
    def delEmpName(self):
        del self.__empname
    empname = property(getEmpName, setEmpName, delEmpName)
#  empname attribute created using property

e1 = Employee(123456, 'John')
print(e1.empid, '-', e1.empname)    # -> '123456 - John'
del e1.empname    # Deletes 'empname'
# print(e1.empname) #Raises 'AttributeError'

################################
### Descriptors can also be created using property decorator
################################
class Employee:
    def __init__(self, emp_id, emp_name):
        self.empid = emp_id
        self.empname = emp_name
    @property
    def empid(self):
        return self.__empid
    @empid.setter
    def empid(self, value):
        if not isinstance(value, int):
            raise TypeError("'empid' must be an integer.")
        self.__empid = value
    @property
    def empname(self):
        return self.__empname
    @empname.setter
    def empname(self, value):
        if not isinstance(value, str):
            raise TypeError("'empname' must be a string.")
        self.__empname = value
    @empname.deleter
    def empname(self):
        del self.__empname
    
e1 = Employee(123456, 'John')
print(e1.empid, '-', e1.empname)    # -> '123456 - John'
del e1.empname    # Deletes 'empname'
# print(e1.empname) #Raises 'AttributeError'
###############################################
###############################################
## CLASS METHODS
## A method defined inside a class is bound to its object, by default
## But if the method is bound to the class instead
## Its called "Class Method"
###############################################
## Defines the method getCirclesCount, bound to an object 
## of Circle class.
class Circle(object):
    no_of_circles = 0
    def __init__(self, radius):
        self.__radius = radius
        Circle.no_of_circles += 1
    def getCirclesCount(self):
        return Circle.no_of_circles
c1 = Circle(3.5)
c2 = Circle(5.2)
c3 = Circle(4.8)
print(c1.getCirclesCount())     # -> 3
print(c2.getCirclesCount())     # -> 3
print(Circle.getCirclesCount(c3)) # -> 3
# print(Circle.getCirclesCount()) # -> TypeError

################################################
## Defines the classmethod getCirclesCount, bound to 
## class Circle
## method is decorated with @classmethod this making it
## a class method bound to class Clircle
class Circle(object):
    no_of_circles = 0
    def __init__(self, radius):
        self.__radius = radius
        Circle.no_of_circles += 1
    @classmethod
    def getCirclesCount(self):
        return Circle.no_of_circles
c1 = Circle(3.5)
c2 = Circle(5.2)
c3 = Circle(4.8)
print(c1.getCirclesCount())     # -> 3
print(c2.getCirclesCount())     # -> 3
print(Circle.getCirclesCount()) # -> 3

## Here class Circle is passed as argument to getCirclesCount
## in both cases. i.e when called on objects and the class.
#################################################

#################################################
## STATIC METHOD
## A method defined inside a class and not bound to 
## either a class or an object.
#################################################
## Defines the method square, outside the class definition 
## of Circle, and uses it inside the class Circle.
def square(x):
        return x**2
class Circle(object):
    def __init__(self, radius):
        self.__radius = radius
    def area(self):
        return 3.14*square(self.__radius)
c1 = Circle(3.9)
print(c1.area())
print(square(10))
#################################################
## Defines the static method square, inside the class Circle, 
## and uses it.
class Circle(object):
    def __init__(self, radius):
        self.radius = radius
    @staticmethod
    def square(x):
        return x**2
    def area(self):
        return 3.14*self.square(self.radius)
    # can define to add anything really
    def __add__(self,other):
        return self.radius + other.radius
c1 = Circle(3.9)
c2 = Circle(3.1)
print(c1.area())  
# print(square(10)) # -> NameError
print(Circle.square(10))
print(c1.square(10))
print("Result of add is: ",c1+c2)
#################################################
#################################################
## ABSTRACT BASE CLASS (ABC)
## An Abstract Base Class mandates the derived classes to 
## implement specific methods from the base class.
##########################
## Not possible to create an object from a defined ABC class.
## Creating objects of derived classes is possible only when 
## derived classes override existing functionality of 
## all abstract methods defined in an ABC class
##########################
## An Abstract Base Class can be created using module abc.

## Abstract base class Shape is defined with 
## two abstract methods area and perimeter.
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
# s1 = Shape() ## --> results in type error. Can't instantiate abstract class Shape with abstract methods area, perimeter

## Creating object c1, with out defining perimeter inside 
## derived class, Circle, resulted in TypeError.
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
    @staticmethod
    def square(x):
        return x**2
    def area(self):
        return 3.14*self.square(self.__radius)
# c1 = Circle(3.9) ## Can't instantiate abstract class Circle with abstract methods perimeter
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
    @staticmethod
    def square(x):
        return x**2
    def area(self):
        return 3.14*self.square(self.__radius)
    def perimeter(self):
        return 2*3.14*self.__radius
print("Will work now since we've defined perimeter method")
c1 = Circle(3.9)
print(c1.area())
############################################


###########################################
        
###################
## INHERITANCE
###################
# abstracting common details into super class and storing specific ones in the subclass
# Child class inherits all the behaviours exhibited by their parent class
# Every class is inherited from "object" by default.
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
class Employee(Person):
    all_employees = []
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.empid = empid
        Employee.all_employees.append(self)

p1 = Person('George', 'smith')
print(p1.fname, '-', p1.lname)
e1 = Employee('Jack', 'simmons', 456342)
e2 = Employee('John', 'williams', 123656)
print(e1.fname, '-', e1.empid)
print(e2.fname, '-', e2.empid)

# Can be also used to extend the built-in classes 
# like list or dict
# Extend list and creates EmployeesList, which can 
# identify employees, having a given search word 
# in their first name.

class EmployeesList(list):
    def search(self, name):
        matching_employees = []
        for employee in self:
            if name in employee.fname:
                matching_employees.append(employee.fname)
        return matching_employees

class Employee(Person):
    all_employees = EmployeesList()
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.empid = empid
        Employee.all_employees.append(self)
e1 = Employee('Jack', 'simmons', 456342)
e2 = Employee('George', 'Brown', 656721)
print(Employee.all_employees.search('or'))

#### POLYMORPHISM
# allows a subclass to override or change a  
# specific behavior, exhibited by the parent class
#######################
class Employee(Person):
    all_employees = EmployeesList ()
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.empid = empid
        Employee.all_employees.append(self)
    def getSalary(self):
        return 'You get Monthly salary.'
    def getBonus(self):
        return 'You are eligible for Bonus.'

class ContractEmployee(Employee):
   def getSalary(self):
        return 'You will not get Salary from Organization.'
   def getBonus(self):
        return 'You are not eligible for Bonus.'

e1 = Employee('Jack', 'simmons', 456342)
e2 = ContractEmployee('John', 'williams', 123656)
print(e1.getBonus())
print(e2.getBonus())


### Abstraction 
## working with something you know how to use 
## without knowing how it works internally.

### Encapsulation
## allows binding data and associated methods together 
## in a unit i.e class

## Abstracting data
## Direct access to data can be restricted by making 
## required attributes or methods private, just by  
## prefixing it's name with one or two underscores.
## An attribute or a method starting with:
## No Underscore --> Public
## Single underscore --> Private, still accessible from outside
## Double underscore--> Strongly Private, not accessible from outside


# empid attribute made strongly private and is accessible
# outside the class only using the method getEmpid.

class Employee(Person):
    all_employees = EmployeesList()
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.__empid = empid
        Employee.all_employees.append(self)
    def getEmpid(self):
        return self.__empid

e1 = Employee('JackO', 'Lantern', 456342)
print(e1.fname, e1.lname)
print(e1.getEmpid())
# print(e1.__empid) ## Attribute error #Single underscore would have been accessible

x = "Rahul is {} years old and in {} grade"
print(x.format(15,10))

y = "You can buy {2} kgs of {0}  for {1} dollars"
print(y.format('Surf excel',100.0,2))

import math

class Point():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return ("Point : ({}, {}, {})".format(self.x,self.y,self.z))
    #Runs like a repair method for debugging. Like when Str not found or if called explicitly
    def __repr__(self):
        return ("Point ({}, {}, {})".format(self.x,self.y,self.z))
    def distance(p1,p2):
        dist = math.sqrt( (p1.x-p2.x)**2 + (p1.y-p2.y)**2 + (p1.z-p2.z)**2 )
        return dist
    def __add__(p1,p2):
        x_new=p1.x+p2.x
        y_new=p1.y+p2.y
        z_new=p1.z+p2.z
        p = Point(x_new,y_new,z_new)
        return p
    
p1 = Point(2,3,7)
p2 = Point(3,3,3)
print(p1)
print(Point.distance(p1,p2))
print(p1+p2)


##########################################
import unittest
def isEven(n):
    if n%2==0:
        return True
    else:
        return False

class TestIsEvenMethod(unittest.TestCase):
    def test_isEven1(self):
        self.assertEqual(isEven(5),False)
    def test_isEven2(self):
        self.assertRaises(TypeError,isEven,"hello")
        
if __name__ == '__main__':
    unittest.main()
########################################
print("Unit test ran")

