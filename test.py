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

		# Fail unless function returns a list
    def testOne(self):
			a = get_ingredient_ids()
			self.failUnless(isinstance(a, list))


def main():
	unittest.main()

if __name__ == '__main__':
  main()




