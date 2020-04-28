import unittest
from Logging.employee_root import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):    #runs once before the whole test session
        print("setUpClass\n")

    @classmethod
    def tearDownClass(cls):
        print("\ntearDOwnClass")  #runs once after the whole test session


    def setUp(self): #runs before every single test
        print("setUp")
        self.emp1 = Employee("Thomas", "Stoetzner", 5000)
        self.emp2 = Employee("Jakob", "Klamm", 30)

    def tearDown(self): #runs after every single test
        print("tearDown")

    def test_email(self):
        self.assertEqual(self.emp1.email, "Thomas.Stoetzner@email.com")
        self.assertEqual(self.emp2.email, 'Jakob.Klamm@email.com')

        self.emp1.first = "Juergen"
        self.emp2.first = "Werner"

        self.assertEqual(self.emp1.email, "Juergen.Stoetzner@email.com")
        self.assertEqual(self.emp2.email, 'Werner.Klamm@email.com')

    def test_fullname(self):

        self.emp1 = Employee("Thomas", "Stoetzner", 5000)
        self.emp2 = Employee("Jakob", "Klamm", 30)

        self.assertEqual(self.emp1.fullname, "Thomas Stoetzner")
        self.assertEqual(self.emp2.fullname, 'Jakob Klamm')

        self.emp1.first = "Juergen"
        self.emp2.first = "Werner"

        self.assertEqual(self.emp1.fullname, "Juergen Stoetzner")
        self.assertEqual(self.emp2.fullname, 'Werner Klamm')

    def test_apply_raise(self):
        self.emp1 = Employee("Thomas", "Stoetzner", 5000)
        self.emp2 = Employee("Jakob", "Klamm", 30)

        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 5250)
        self.assertEqual(self.emp2.pay, 31)

    def test_monthly_schedule(self):
        with patch("Logging.employee_root.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp1.monthly_schedule("May")
            mocked_get.assert_called_with("http://company.com/Stoetzner/May")
            self.assertEqual(schedule, "Success")

            mocked_get.return_value.ok = False

            schedule = self.emp1.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Stoetzner/June")
            self.assertEqual(schedule, "Bad response")


if __name__ == "__main__":
    unittest.main()