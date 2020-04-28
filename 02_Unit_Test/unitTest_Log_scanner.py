import unittest
from Logging.Generator import Log_scanner


class TestLogScanner(unittest.TestCase):
    #def setUp(self):
     #   self.TestGen = Log_scanner()

    def Test_Counter(self):
        TestGen = Log_scanner()
        result = TestGen.scan_Counter()
        #print("test Count Warnings and Errors")
        self.assertNotEqual(0, result)

if __name__ == "__main__":
    unittest.main()