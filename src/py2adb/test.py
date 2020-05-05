#from package import *
import unittest
import connect
from __init__ import Phone

class Py2adbTest(unittest.TestCase):
    def test_get_addr(self):
        self.assertEqual(type(connect.get_addr()), type({}))

def main():
    unittest.main()
