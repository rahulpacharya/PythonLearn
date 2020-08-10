import nose

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

# from proj.circle import Circle
from nose.tools import assert_raises
class TestingCircleCreation:
    def test_creating_circle_with_numeric_radius(self):
        c1 = Circle(2.5)
        assert c1.radius == 2.5
        
    def test_creating_circle_with_negative_radius(self):
        with assert_raises(ValueError):
            Circle(-2.5)
    
    def test_creating_circle_with_greaterthan_radius(self):
        with assert_raises(ValueError):
            Circle(1000.1)
    
    def test_creating_circle_with_nonnumeric_radius(self):
        with assert_raises(TypeError):
            Circle('hello')

class TestCircleArea:
    def test_circlearea_with_random_numeric_radius(self):
        c1 = Circle(2.5)
        assert c1.area() == 19.63
        
    def test_circlearea_with_min_radius(self):
        c1 = Circle(0)
        assert c1.area() == 0
    
    def test_circlearea_with_max_radius(self):
        c1 = Circle(1000)
        assert c1.area() == 3141592.65

class TestCircleCircumference:
    def test_circlecircum_with_random_numeric_radius(self):
        c1 = Circle(2.5)
        assert c1.circumference() == 15.71
        
    def test_circlecircum_with_min_radius(self):
        c1 = Circle(0)
        assert c1.circumference() == 0
    
    def test_circlecircum_with_max_radius(self):
        c1 = Circle(1000)
        assert c1.circumference() == 6283.19
