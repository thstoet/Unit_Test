import unittest
from unitTest.unitModul_class_Faku import Faku

class FakultaetTestCase(unittest.TestCase):
    def setUp(self):
        self.fakultaet = Faku()

    def test_1_fakulaet(self):
        self.assertEqual(self.fakultaet.fact1(6), 720)

    def test_2_fakulaet(self):
        self.assertEqual(self.fakultaet.fact1(3), 6)

    def test_3_fakulaet(self):
        self.assertEqual(self.fakultaet.fact1(4), 24)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(FakultaetTestCase('test_1_fakulaet'))
    suite.addTest(FakultaetTestCase('test_2_fakulaet'))
    suite.addTest(FakultaetTestCase('test_3_fakulaet'))
    return suite

if __name__ == '__main__':
        runner = unittest.TextTestRunner()
        runner.run(suite())