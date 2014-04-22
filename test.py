# Keep .pyc files from being generated
import sys
sys.dont_write_bytecode = True

import unittest

# Here's our "unit".
def IsOdd(n):
    return n % 2 == 1

# Each inport will represent a unit
from app.controllers import get_ingredient_ids

class Get_Ingredient_Ids_Tests(unittest.TestCase):

    def testOne(self):
        print get_ingredient_ids()

    def testTwo(self):
        self.failIf(IsOdd(2))

def main():
    unittest.main()

if __name__ == '__main__':
    main()




# Here's our "unit tests".
class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.failUnless(IsOdd(5))

    def testTwo(self):
        self.failIf(IsOdd(2))

def main():
    unittest.main()

if __name__ == '__main__':
    main()