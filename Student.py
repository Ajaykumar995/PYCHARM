class Student:
    def __init__(self,name,marks):
        self.__name = ""
        self.__marks = 0
    def getName(self):
        return self.__name
    def getMarks(self):
        return self.__marks
    def setName(self,name):
        self.__name = name

    def setMarks(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            raise ValueError("Marks should be between 0 and 100")
        print(self.__marks)
s = Student("John",100)
s.setName("Alice")
print(s.getName())
s.setMarks(100)

# print(s.getMarks())

