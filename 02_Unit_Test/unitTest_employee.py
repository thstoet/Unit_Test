import unittest
from Logging.employee_root import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):

        emp1 = Employee("Thomas", "Stoetzner", 5000)
        emp2 = Employee("Jakob", "Klamm", 30)

        self.assertEqual(emp1.email, "Thomas.Stoetzner@email.com")
        self.assertEqual(emp2.email, 'Jakob.Klamm@email.com')

        emp1.first = "Juergen"
        emp2.first = "Werner"

        self.assertEqual(emp1.email, "Juergen.Stoetzner@email.com")
        self.assertEqual(emp2.email, 'Werner.Klamm@email.com')

    def test_fullname(self):

        emp1 = Employee("Thomas", "Stoetzner", 5000)
        emp2 = Employee("Jakob", "Klamm", 30)

        self.assertEqual(emp1.fullname, "Thomas Stoetzner")
        self.assertEqual(emp2.fullname, 'Jakob Klamm')

        emp1.first = "Juergen"
        emp2.first = "Werner"

        self.assertEqual(emp1.fullname, "Juergen Stoetzner")
        self.assertEqual(emp2.fullname, 'Werner Klamm')

    def test_apply_raise(self):
        emp1 = Employee("Thomas", "Stoetzner", 5000)
        emp2 = Employee("Jakob", "Klamm", 30)

        emp1.apply_raise()
        emp2.apply_raise()

        self.assertEqual(emp1.pay, 5250)
        self.assertEqual(emp2.pay, 31)


if __name__ == "__main__":
    unittest.main()