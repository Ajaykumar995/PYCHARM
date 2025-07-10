from contextlib import nullcontext


class Employee:
    def __init__ (self):
        self.__name = ""
        self.salary = None
        self.age = None
    def getName(self):
        return self.__name
    def getSalary(self):
        return self.salary
    def getAge(self):
        return self.age
    def setName(self, name):
        self.__name = name
    def setSalary(self, salary):
        if 0 <= salary:
            self.salary = salary
        else:
            "Salary can't be less than zero"
    def setAge(self, age):
        if 18<=age<=100:
            self.age = age
        else:
            print("age must be between 18 and 100")
        # self.age = age
e = Employee()
e.setName("John Doe")
e.setSalary(20000)
e.setAge(2)
print(e.getName())
print(e.getSalary())
print(e.getAge())