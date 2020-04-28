import logging
import unittest
import sys

logging.basicConfig(filename="foo_logging.log",level=logging.INFO) #alles ab Info wird geloggt
logger= logging.getLogger("backend")

class unit_foo:

    def foo(self,num):
        if num == 1:
            logger.warning("1 is not accepted")
            return False
        return True


'''
assertLog testet ob Log in Testklasse ausgelöst wird
Da die Klasse nur getestet wird, gibt es keine Logeinträge

'''

class testLogger(unittest.TestCase):

    def test_foo(self):

        myUnit_foo = unit_foo()

        with self.assertLogs("backend", level="INFO") as logs:   #NAME und MindestLogLevel des zu testenden Loggers werden definiert

            result = myUnit_foo.foo(1)

        self.assertFalse(result)
        self.assertIn("WARNING:backend:1 is not accepted",logs.output)  #LogEintrag wird verglichen


if __name__=="__main__":
    unittest.main()