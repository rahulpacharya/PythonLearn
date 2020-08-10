# A xUnit-style library contains the following components.
# Test case class : It is the base class of all test classes 
# written in test modules.

# Text fixtures : These are the methods that run before and 
# after the execution of test code.

# Assertions : These are the functions or methods that check 
# the behavior of variables being tested.

# Test Suite: It is the collection of related tests that can be
# executed together.

# Test Runner: It is the block of code that runs the test suite.

# Test result formatter : It formats the test results output 
# in human readable formats like plaintext, HTML, XML, etc.

def add2num(x, y):
    return x + y

import unittest

def setUpModule(): #later
    print('Executed before any test in the module')

def tearDownModule():  #later
    print('Executed after all tests in module are run')

class Testadd2num(unittest.TestCase):

    def test_sum_2pos_num(self):
      self.assertEqual(add2num(6, 7), 13)

    def test_sum_1pos_and_1neg_num(self):
      self.assertEqual(add2num(-10, 9), -1)
    
    def setUp(self): #later
        print('Executed before start of every test-Testadd2num')

    def tearDown(self): #later
        print('Executed at the end of every test-Testadd2num')
    
    @classmethod
    def setUpClass(cls): #later
        print('Executed before any test in the class runs.-Testadd2num')

    @classmethod
    def tearDownClass(cls): #later
        print('Executed after all tests in class are run.-Testadd2num')

# Run this using
# python -m unittest Testing_UnitTest_Basics
      
# python -m unittest Testing_UnitTest_Basics -v
# (For verbose o/p)
      
# python -m unittest Testing_UnitTest_Basics.Testadd2num 
# (To only run tests related to this class)

# python -m unittest Testing_UnitTest_Basics.Testadd2num.test_sum_2pos_num
# (Single test in a class)

######################################
def pow2num(x, y):
    """Returns x power of y.
    >>> pow2num(2, 6)
    64
    >>> pow2num(10, -3)
    0.001
    """
    return x**y

class Testpow2num(unittest.TestCase):

    def test_pow_2pos_num(self):
        self.assertEqual(pow2num(3, 4), 81)

    def test_neg_pow(self):
        self.assertEqual(pow2num(10, -2), 0.01)

    def test_negnum_pow(self):
        self.assertEqual(pow2num(-3, 3), -27)
        
    #def test_negnum_pow(self):
    #    self.assertEqual(pow2num(-3, 3), -26)

###############################################
### TEST FIXTURES
###############################
# Test Fixtures are the activities to be performed before 
# and after the tests.
       
# Test fixtures are generally implemented as methods 
# of a test class derived from unittest.TestCase.

#  Major test fixtures used in unit test are
# setUpModule, tearDownModule, setUpClass, tearDownClass,
# setUp, and tearDown

# In above example, the two fixture methods, setUp and tearDown
# test method level fixtures and are run 
# before and after executing every test method 

# setUpClass and tearDownClass are class methods. 
# setUpClass runs once before any method of the class runs 
# tearDownClass runs after all methods of the class are executed.

# setUpModule runs once before any test is executed in a module
# tearDownModule runs once after all tests in a module are executed.

####################################
    #### TEST DISCOVERY
#####################################

## Test Discovery is the process of finding all tests 
# present in a project folder and executing them 
# automatically.
    
# python -m unittest discover
    
# All files containing tests must be either modules 
# or packages. In case of packages, they must be 
# importable from top directory of the project.
    
# By default, test discovery always searches for 
# modules or packages starting with test pattern 
# in their names. test pattern is case insensitive.
    
# By default, the test discovery always starts 
# from working directory and it is recursive.
    
#################################
## TYPES OF ASSERTIONS
#################################
#Frequently used assert methods in unittest are:
#assertEqual(a, b) - Tests if a equals to b
#assertAlmostEqual(a, b) - Tests if round(a-b, 7) is 0.
#assertTrue(x) - Tests if bool(x) is True.
#assertIs(a, b) - Tests if a is b.
#assertIsNone(x) - Tests if x is None
#assertIn(a, b) - Tests if a in b
#assertIsInstance(a, b) - Tests if a is an instance of b.
#assertRegexpMatches(s, r) - Tests if the re pattern r is found in string s.
#assertItemsEqual(a, b) - Tests if sorted(a) equals to sorted(b)
#assertListEqual(a, b) - Tests if two lists a and b are same.
#assertMultiLineEqual(a, b) - Tests if two multiline strings a and b are equal.
#assertRaises  - check if a specified Exception is raised, when the test runs
#################################
###### ASSERT RAISES
#################################
## to check if a specified Exception is raised, when 
# the test run
## if the specified exception is raised, test passes. else fails

class SampleTestClass1(unittest.TestCase):
    def test_sample1(self):
        self.assertRaises(TypeError, add2num, 3, 'hello')
    def test_sample2(self):
        with self.assertRaises(TypeError) as e:
            r = add2num(3, 'hello')
        self.assertEqual(str(e.exception), "unsupported operand type(s) for +: 'int' and 'str'")
    # this is another way of writing prev test using with
    # this also validates the error message thrown
########################################
#####  Skipping unit test
########################################
#unittest.skip --> skips a decorated test unconditionally
#unittest.skipIf --> skip if condition satisfied
#unittest.skipUnless --> skips unless condition is true
#unittest.expectedFailure --> marks a test as a failure test. i.e even if the decorated test fails, it is not counted as a failure one
class SampleTestClass2(unittest.TestCase):
    @unittest.skip('Don\'t like test_sample3')
    def test_sample3(self):
      self.assertEqual(add2num(2, 2), 4)
      
    @unittest.skipIf(2==2, "Skip if")
    def test_sample4(self):
      self.assertEqual(add2num(1, -9), -8)
    
    @unittest.skipUnless(2==3, '"Skip unless')
    def test_sample5(self):
      self.assertEqual(add2num(22, -4), 18)
   
    @unittest.expectedFailure
    def test_sample6(self):
      self.assertEqual(add2num(22, 0), 23)




##################
# All the test cases written in a file can be run by adding 
# the following lines at the end of the file
if __name__ == '__main__':
    unittest.main()

# the name == main block will ensure that code inside the 
# block will be executed only when this module is run as a 
# program.
# So all tests in this can be run when the entire module is run 
# python Testing_UnitTest_Basics.py
# python Testing_UnitTest_Basics.py -v