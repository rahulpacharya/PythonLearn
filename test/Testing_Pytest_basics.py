import pytest

# PYTEST
################
# Pytest is another third party python library, used for unit testing.

def test_sample_pytest_test():
    assert 'HELLO' == 'hello'.upper()
    
# python -m pytest Testing_Pytest_basics.py
# py.test Testing_Pytest_basics.py



def add2num(x, y):
    return x + y

class Testadd2num:

    def test_sum_2pos_num(self):
      assert add2num(6, 7)==13

    def test_sum_1pos_and_1neg_num(self):
      assert add2num(-10, 9)==-1

#if this file were in test folder
# py.test -v test 
# py.test -v test/Testing_Pytest_basics.py
# py.test -v test/Testing_Pytest_basics.py::Testadd2num
# py.test -v test/Testing_Pytest_basics.py::Testadd2num::test_sum_2pos_num

# TEST DISCOVERY
# py.test -v
# Running this from project folder will discover and run 
# all tests found

# FIXTURES
# setup_module and teardown_module are module level fixtures.
# setup_class and teardown_class are class level fixtures. These fixtures need to be decorated with @classmethod.
# setup_method and teardown_method are method level fixtures.
# setup_function and teardown_function are function level fixtures.
      
# SKIPPING TESTS

@pytest.mark.skip("reason for skipping")
def test_sample1():
    assert add2num(5, 5)==10

x = 13

@pytest.mark.skipif(x==13,reason='reason for skipping')
def test_sample2():
    assert add2num(5, 6)==11

# RAISING EXCEPTIONS
#to detect exceptions in a test
def test_using_raises1():
    with pytest.raises(TypeError):
        2+'3' == 5

# GENERATING REPORTS
# py.test --resultlog=result.txt # text file 
# py.test --resultlog=result     # plain text report
# py.test --junitxml=result.xml  # xml report