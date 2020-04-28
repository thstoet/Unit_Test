import logging
import unittest
import sys

logging.basicConfig(filename="test_Unitlog",level=logging.DEBUG)
logger= logging.getLogger("Test")

class unit_foo:

    def foo(self,num):
        if num == 1:
            return False
        return True

class testLogger(unittest.TestCase):

    def test_foo_False(self):

        logger.debug("Logging TC: test_foo_False")
        myUnit_foo = unit_foo()
        result = myUnit_foo.foo(1)
        self.assertFalse(result)



if __name__=="__main__":
    unittest.main()
