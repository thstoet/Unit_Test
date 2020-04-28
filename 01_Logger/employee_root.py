import logging
import requests

logging.basicConfig(filename="employee.log", level=logging.INFO,
                    format="%(name)s - %(levelname)s : %(message)s")

class Employee:

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        #Kann gleich in Konstruktor geschrieben werden. logging wird beim instanzieren durchgezogen
        logging.info("Created employee: {} - {}".format(self.fullname, self.email))

    @property #Info: mit diesem Dekorator kann diese Funktion als Variable fungieren
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get(f"http://company.com/{self.last}/{month}")
        if response.ok:
            return response.text
        else:
            return "Bad response"

if __name__ == "__main__":

    emp_1 = Employee("Thomas","Stoetzner", 500)