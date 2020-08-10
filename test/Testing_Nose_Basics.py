import nose

# nose makes testing easier by extending unittest framework
# nose can be used to run automated tests and 
# also the tests written in other frameworks like unittest.

# Can write test outside a class (unlike unittest)
# Even if written in class, it need not be deerived from a base class

def test_sample_nosetest():
    assert 'HELLO' == 'hello'.upper()
    
# On command prompt
# python -m nose Testing_Nose_Basics.py
# python -m nose Testing_Nose_Basics.py -v
# nosetests  Testing_Nose_Basics.py -v

def add2num(x, y):
    return x + y

class Testadd2num:

    def test_sum_2pos_num(self):
      assert add2num(6, 7)==13

    def test_sum_1pos_and_1neg_num(self):
      assert add2num(-10, 9)==-1
    
    def test_sum_2neg_num(self):
      assert add2num(-6, -7)==-13

# nosetests Testing_Nose_Basics -v
# nosetests Testing_Nose_Basics:Testadd2num -v
# nosetests Testing_Nose_Basics:Testadd2num.test_sum_2pos_num -v

# TEST DISCOVERY IN NOSE
# nosetests -v #to run all the tests present in Project folder.

# TEST FIXTURES 
# setUpModule and tearDownModule are used at Module level.
# setUpClass and tearDownClass are used at class level.
# setUp and tearDown are used at test method level.
###################################################
# nose.tools methods 
from nose.tools import assert_equals

def test_sample_nose1test1():
    assert_equals('HELLO','hello'.upper())
###################################################
from nose.tools import ok_, eq_

def test_using_ok():
    ok_(2+3==5)   # like assert

def test_using_eq():
    eq_(2+3, 5)# like assert equals
###################################################
from nose.tools import raises

@raises(TypeError) # decorator used to decorate those steps which are expected to raise an exception
def test_using_raises():  
    eq_(2+'3', 5)   # test will be successful only if the exception raised is present in list of exceptions passed to raises decorator.
###################################################

#Report generation in xml
#nosetests Testing_Nose_Basics -v --with-xunit


if __name__ == '__main__':
    nose.main()









