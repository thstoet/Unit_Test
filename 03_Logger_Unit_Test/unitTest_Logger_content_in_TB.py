import logging
import unittest
import sys

logging.basicConfig(stream=sys.stderr,level=logging.INFO)
logger= logging.getLogger("backend")

'''
Logging Content von zu testender Klasse wird im sysStream angezeigt

'''

class unit_foo:

    def foo(self,num):
        if num == 1:
            logger.warning("1 is not accepted")
            return False
        return True

class testLogger(unittest.TestCase):

    def test_foo(self):

        myUnit_foo = unit_foo()
        result = myUnit_foo.foo(1)
        self.assertFalse(result)


if __name__=="__main__":
    unittest.TextTestRunner().run(unit_foo())
