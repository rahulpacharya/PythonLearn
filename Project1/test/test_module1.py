import unittest
from Project1.sample_module import add2num
from Project1.sample_module import pow2num
######################################
def setUpModule(): #later
    print('Executed before any test in the module')

def tearDownModule():  #later
    print('Executed after all tests in module are run')
######################################
class Testadd2num(unittest.TestCase):

    def test_sum_2pos_num(self):
      self.assertEqual(add2num(6, 7), 13)

    def test_sum_1pos_and_1neg_num(self):
      self.assertEqual(add2num(-10, 9), -1)
    
    def setUp(self): #later
        print('Executed before start of every test')

    def tearDown(self): #later
        print('Executed at the end of every test')
    
    @classmethod
    def setUpClass(cls): #later
        print('Executed before any test in the class runs.')

    @classmethod
    def tearDownClass(cls): #later
        print('Executed after all tests in class are run.')


######################################

class Testpow2num(unittest.TestCase):

    def test_pow_2pos_num(self):
        self.assertEqual(pow2num(3, 4), 81)

    def test_neg_pow(self):
        self.assertEqual(pow2num(10, -2), 0.01)

    def test_negnum_pow(self):
        self.assertEqual(pow2num(-3, 3), -26)
######################################

if __name__ == '__main__':
    unittest.main()


