class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

jatin = Employee()
jatin.salary = 100000
jatin.getSalary("Thanks!") # Employee.getSalary(harry)
jatin.greet() # Employee.greet()
jatin.time()

