######################################################
## HANDS ON 1
######################################################
import math
import unittest

class Circle:
    def __init__(self, radius):
        # Define initialization method:
        if not ( ((isinstance(radius,float))) or (isinstance(radius,int))) :
            raise TypeError("radius must be a number")
        if radius > 1000 or radius < 0:
            raise ValueError("radius must be between 0 and 1000 inclusive")
        self.radius = radius

    def area(self):
        # Define area functionality:
        return round((math.pi*(self.radius**2)),2)
               
    def circumference(self):
        # Define circumference functionality:
        return round((math.pi*self.radius*2),2)


        
class TestCircleCreation(unittest.TestCase):

    def test_creating_circle_with_numeric_radius(self):
        # Define a circle 'c1' with radius 2.5, and check if 
        # the value of c1.radius is equal to 2.5 or not.
        c1 = Circle(2.5)
        self.assertEqual(c1.radius,2.5)

    def test_creating_circle_with_negative_radius(self):
        # Define a circle 'c' with radius -2.5, and check 
        # if it raises a ValueError with the message
        # "radius must be between 0 and 1000 inclusive".
        with self.assertRaises(ValueError) as e:
            c1 = Circle(-2.5)
        self.assertEqual(str(e.exception), "radius must be between 0 and 1000 inclusive")  

    def test_creating_circle_with_greaterthan_radius(self):
        # Define a circle 'c' with radius 1000.1, and check 
        # if it raises a ValueError with the message
        # "radius must be between 0 and 1000 inclusive".
        with self.assertRaises(ValueError) as e:
            c1 = Circle(1000.1)
        self.assertEqual(str(e.exception), "radius must be between 0 and 1000 inclusive")       
        
    def test_creating_circle_with_nonnumeric_radius(self):
        # Define a circle 'c' with radius 'hello' and check 
        # if it raises a TypeError with the message
        # "radius must be a number".
        with self.assertRaises(TypeError) as e:
            c1 = Circle('hello')
        self.assertEqual(str(e.exception), "radius must be a number")

######################################################
## HANDS ON 2
######################################################
class Circle:
    
    def __init__(self, radius):
        # Define initialization method:
        if not ( ((isinstance(radius,float))) or (isinstance(radius,int))) :
            raise TypeError("radius must be a number")
        if radius > 1000 or radius < 0:
            raise ValueError("radius must be between 0 and 1000 inclusive")
        self.radius = radius
        
    def area(self):
        # Define area functionality:
        return round((math.pi*(self.radius**2)),2)
               
    def circumference(self):
        # Define circumference functionality:
        return round((math.pi*self.radius*2),2)
        
class TestCircleArea(unittest.TestCase):
    
    def test_circlearea_with_random_numeric_radius(self):
        # Define a circle 'c1' with radius 2.5, and check if 
        # its area is 19.63.
        c1 = Circle(2.5)
        self.assertEqual(c1.area(),19.63)
        
    def test_circlearea_with_min_radius(self):
        # Define a circle 'c2' with radius 0, and check if 
        # its area is 0.
        c2 = Circle(0)
        self.assertEqual(c2.area(),0)
        
    def test_circlearea_with_max_radius(self):
        # Define a circle 'c3' with radius 1000.1. and check if 
        # its area is 3141592.65.
        c3 = Circle(1000)
        self.assertEqual(c3.area(),3141592.65)

######################################################
## HANDS ON 3
######################################################
class Circle:
    
    def __init__(self, radius):
        # Define initialization method:
        if not ( ((isinstance(radius,float))) or (isinstance(radius,int))) :
            raise TypeError("radius must be a number")
        if radius > 1000 or radius < 0:
            raise ValueError("radius must be between 0 and 1000 inclusive")
        self.radius = radius
        
    def area(self):
        # Define area functionality:
        return round((math.pi*(self.radius**2)),2)
               
    def circumference(self):
        # Define circumference functionality:
        return round((math.pi*self.radius*2),2)
        
class TestCircleCircumference(unittest.TestCase):
    
    def test_circlecircum_with_random_numeric_radius(self):
        # Define a circle 'c1' with radius 2.5, and check if 
        # its circumference is 15.71.
        c1 = Circle(2.5)
        self.assertEqual(c1.circumference(),15.71)
        
    def test_circlecircum_with_min_radius(self):
        # Define a circle 'c2' with radius 0, and check if 
        # its circumference is 0.
        c2 = Circle(0)
        self.assertEqual(c2.circumference(),0)
        
    def test_circlecircum_with_max_radius(self):
        # Define a circle 'c3' with radius 1000, and check if 
        # its circumference is 6283.19.
        c3 = Circle(1000)
        self.assertEqual(c3.circumference(),6283.19)









if __name__ == '__main__':
    unittest.main()
