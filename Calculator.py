class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b
cal = Calculator()
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(f" Addition of ({a},{b}) is {cal.add(a,b)}")
print(f"Substraction of ({a},{b}) is : {cal.sub(a,b)}")
print(f"Multiplication of ({a},{b}) is :{cal.multiply(a,b)}")
print(f"Division of ({a},{b}) is :{cal.divide(a,b)}")
