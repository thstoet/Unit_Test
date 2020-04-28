import  unittest
from unitTest.unitModul_class_Validator import Validator

class TestValidator(unittest.TestCase):

    def setUp(self):
        self.myValid = Validator()

    def test_len_of_username(self):
        username="Thisismuchtolongforvalidator"
        result = self.myValid.username_is_valid(username)
        self.assertFalse(result)

    def test_space_of_username(self):

        username="Thisgoes wrong"
        result = self.myValid.username_is_valid(username)
        self.assertFalse(result)

    def test_islower_of_username(self):

        username="wrong"
        result = self.myValid.username_is_valid(username)
        self.assertFalse(result)

    def test_accept_username(self):

        username="Right"
        result = self.myValid.username_is_valid(username)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()