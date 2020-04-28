import unittest
from Logging import calc_advanced

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc_advanced.add(3,4),7)
        self.assertEqual(calc_advanced.add(-1, -1), -2)

    def test_dev(self):
        with self.assertRaises(ValueError):
            calc_advanced.div2(10, 0)

if __name__ == "__main__":
    unittest.main()