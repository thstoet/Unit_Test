import logging
import unittest
import sys

'''
Content von TB soll geloggt werden.
V2 = weittere Variante
prinzipiell richtig, aber log file wird nicht erstellt
Mitunter ist dort der Testrunner anders definiert

'''



class unit_foo:

    def foo(self,num):
        if num == 1:
            return False
        return True

class testLogger(unittest.TestCase):

    def test_foo(self):

        myUnit_foo = unit_foo()
        result = myUnit_foo.foo(1)

        self.assertFalse(result)


def main(out = sys.stderr, verbosity = 2):
    loader = unittest.TestLoader()

    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)

if __name__=="__main__":
    with open("testing.out", "w") as f:
        main(f)