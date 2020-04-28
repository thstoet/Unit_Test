import unittest
from unitTest.Test_Modul_Fibo import fib
from unitTest.unitModul_fac1 import fact1


class Test(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(fib(10), 55)

    def test_fact(self):
        self.assertEqual(fact1(5), 120)

    def test_fact1(self):
        self.assertEqual(fact1(4), 24)

    @unittest.skip("demo skipping")  #decorator
    def test_Calc(self):
        self.assertEqual(1+1, 2)

class NumbersTest(unittest.TestCase):

    #Test that numbers between 0 and 5 are all even
    def test_even(self):
        for i in range(0,6,2):
            with self.subTest(i=i):   # without using a subtest, execution wold stop after first failure
                self.assertEqual(i%2,0)


if __name__ == "__main__":
    unittest.main()