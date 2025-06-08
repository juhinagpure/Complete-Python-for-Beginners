class Employee:
    def __init__(self):
        self._salary = 234
        self._increment = 20

    @property
    def salaryAfterIncrement(self):
        return self._salary * (1 + self._increment / 100)

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, new_salary):
        self._increment = (new_salary / self._salary - 1) * 100

e = Employee()
print(e.salaryAfterIncrement)  # Output: 280.8
