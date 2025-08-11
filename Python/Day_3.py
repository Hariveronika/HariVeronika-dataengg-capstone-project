# to comment code ctrl+/
# to remove ctrl k u
# palindrome_checker.py

# def is_palindrome(s):
#     s = s.lower().replace(" ", "")
#     return s == s[::-1]
# ## Driver code
# if __name__ == "__main__":
#     test_str = "Madam"
#     if is_palindrome(test_str):
#         print(f'"{test_str}" is a palindrome.')
#     else:
#         print(f'"{test_str}" is not a palindrome.')


# class Student():

#  def __init__(self,x,y,z):
#     self.name=x
#     self.rollno=y
#     self.marks=z

#  def display(self):
#     print("Student Name:{}\nRollno:{} \nMarks:{}".format(self.name,self.rollno,self.marks))

# s1=Student("Durga",101,80)
# s1.display()
# s2=Student("Sunny",102,100)
# s2.display()

# class Student():

#  def __init__(self,x,y,z):
#     self.name=x
#     self.rollno=y
#     self.marks=z

#  def display(self):
#     self.department='cse'
#     print("Student Name:{}\nRollno:{} \nMarks:{} \nDepartment:{}".format(self.name,self.rollno,self.marks,self.department))

# s1=Student("Durga",101,80)
# s1.display()
# s2=Student("Sunny",102,100)
# s2.display()
# s2.college='VIT'
# print(s2.__dict__) 


# class Hello:
#     def say_hello(self):
#         print("Hello from the Jan!")

# # Driver code
# obj = Hello()
# obj.say_hello()
  
#====================without init and attributes==========

# class Student:
#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}")

# # Create object
# s1 = Student()
# s2 = Student()
# # Set attributes manually
# s1.name = "Anand"
# s1.age = 44

# s2.name = "Jann"
# s2.age = 21

# s1.display()
# s2.display()  

#======================static and class method=========

# class Test:
#     # Class variable 'a' is defined at class level
#     a = 10

#     # Constructor (__init__) is called automatically when object is created
#     def __init__(self):
#         # Adds a class variable 'b' to the class (not to the instance)
#         Test.b = 20

#     # Instance method - can be called using object
#     def m1(self):
#         # Adds class variable 'c' to the class
#         Test.c = 30

#     @classmethod
#     def m2(cls):
#         # Adds class variable 'd1' using class reference
#         cls.d1 = 40
#         # Also adds another class variable 'd2'
#         Test.d2 = 400

#     @staticmethod
#     def m3():
#         # Static method: also modifies class variable
#         Test.e = 50


# # Before creating any object — only 'a' exists
# print("🔹 Initial class dictionary:")
# print(Test.__dict__)
# print("-----------")

# # Create object → constructor runs → adds 'b' to class
# t = Test()

# print("🔹 After object creation (constructor adds b):")
# print(Test.__dict__)
# print("-----------")

# # Call instance method → adds 'c' to class
# t.m1()

# print("🔹 After calling instance method m1 (adds c):")
# print(Test.__dict__)
# print("-----------")

# # Call class method → adds 'd1' via cls, 'd2' via Test
# Test.m2()

# print("🔹 After calling class method m2 (adds d1, d2):")
# print(Test.__dict__)
# print("-----------")

# # Call static method → adds 'e'
# Test.m3()

# print("🔹 After calling static method m3 (adds e):")
# print(Test.__dict__)
# print("-----------")

# # Manually add another class variable 'f'
# Test.f = 60

# print("🔹 After manually adding Test.f = 60:")
# print(Test.__dict__)
# print("-----------")

# class Employee:
#     def __init__(self,eno,ename,esal):
#         self.eno=eno
#         self.ename=ename
#         self.esal=esal
#     def display(self):
#         print("Employee Number:",self.eno)
#         print("Employee Name:",self.ename)
#         print("Employee salary:",self.esal)
# class test:
#     def modify(emp):
#         emp.esal=emp.esal+10000
#         emp.display()
# e=Employee(100,'durga',10000)
# test.modify(e)

#=====================polymorphism and inheritance===========

# Base class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} is starting...")

    def drive(self):
        print(f"Driving a generic {self.brand} car.")


# Subclass 1 - inherits from Car
class ElectricCar(Car):
    def __init__(self, brand, model, battery_range):
        super().__init__(brand, model)
        self.battery_range = battery_range

    # Overriding the drive method (Polymorphism)
    def drive(self):
        print(f"{self.brand} {self.model} (Electric) is driving silently for {self.battery_range} km.")


# Subclass 2 - inherits from Car
class SportsCar(Car):
    def __init__(self, brand, model, top_speed):
        super().__init__(brand, model)
        self.top_speed = top_speed

    # Overriding the drive method (Polymorphism)
    def drive(self):
        print(f"{self.brand} {self.model} (Sports) zooms at a top speed of {self.top_speed} km/h!")


# Subclass 3 - inherits from Car
class SUV(Car):
    def drive(self):
        print(f"{self.brand} {self.model} (SUV) drives smoothly on rough terrains.")


# 🔸 Driver code to demonstrate inheritance and polymorphism
def main():
    # Creating objects of each class
    car = Car("Generic", "BaseModel")
    tesla = ElectricCar("Tesla", "Model 3", 500)
    ferrari = SportsCar("Ferrari", "F8", 340)
    fortuner = SUV("Toyota", "Fortuner")

    # List of cars (polymorphic collection)
    car_list = [car, tesla, ferrari, fortuner]

    # Using polymorphism to call appropriate drive methods
    for c in car_list:
        c.start()
        c.drive()
        print("-----")


if __name__ == "__main__":
    main()

 