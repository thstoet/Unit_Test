import logging
import unittest
import sys

#logging.basicConfig(stream=sys.stderr,level=logging.DEBUG)
#logger= logging.getLogger("Test")

'''
Content von TB soll geloggt werden.
Auf HAndy funktioniert diese Variante
Mitunter ist dort der Testrunner anders definiert

Falls das mal funktioniert - gerne auch TCs Loggings in TB packen
und alles in eine externe Datei 

'''
class unit_foo:

    def foo(self,num):
        if num == 1:
            return False
        return True

class unitTester(unittest.TestCase):

    def test_foo_False(self):
        myUnit_foo = unit_foo()
        result = myUnit_foo.foo(1)
        self.assertFalse(result)

def suite():
    suite=unittest.TestSuite()
    suite.addTest(unitTester("test_foo_False"))
    return suite

if __name__=="__main__":
    log_file = "log_file.txt"
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)



#
# "C:\Python\Script_me\Test_logging\log_file.txt"