class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

class Coder:
    language = "python"
    def printLanguage(self):
        print(f"Out of all the languages, I like {self.language} the most")

class Programmer(Employee, Coder):
    company = "Microsoft"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programmer()

b.name = "Juhi"  # assign name before using

b.show()             # From Employee
b.printLanguage()    # From Coder
b.showLanguage()     # From Programmer
