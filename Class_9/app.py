#                        ----------------------Simple Class----------------------

# class Employee: # Employ is Noun
#     # language and salary are adjective or attributes of the class
#     language = "Python and JS" # class attribute
#     salary = 2000000


# object
# john = Employee()  # instance of emplolyee class and also an object of class
# john.name = "John"    # this is a property of the object and it's called an Object Attribute and instance attributee
# print(john.name, john.language, john.salary)


# robert = Employee()  # instance of emplolyee class and also an object of class
# robert.name = "Robert"    # this is a property of the object and it's called an Object Attribute and instance attributee
# print(robert.name, robert.language, robert.salary)









# class Employee: # Employ is Noun
#     language = "Python and JS" # class attribute
#     salary = 2000000


# john = Employee()
# john.name = "John"    # this is a property of the object and it's called an Object Attribute and instance attribute
# john.language = "Java"   # first preference is given to the object attribute and then class attribute
# print(john.name, john.language, john.salary)


# robert = Employee()  # instance of emplolyee class and also an object of class
# robert.name = "Robert"    # this is a property of the object and it's called an Object Attribute and instance attribute
# print(robert.name, robert.language, robert.salary)



# class Student:
#     name: str
#     age: int = 20
#     roll_no: int


# alice = Student()
# alice.name = "Alice"
# alice.roll_no = 205
# print(alice.name, alice.age, alice.roll_no, sep=", ")
# print("Alice class", alice)


# print(Student == Student)










#                        ----------------------Self perameter----------------------

# class Employee:
#     language = "Python" 
#     salary = "120000"

#     def get_info(self):
#         return f"Employee language is {self.language} and salary is {self.salary}"
    
#     def greet(self):
#         return f"hello from Employee Class"
    
# alice = Employee()

# print(alice.greet())
# # both lines are same
# print(alice.get_info()) # this line is converted to Employee.get_info(alice) internally
# print(Employee.get_info(alice))








#                        ----------------------Static Method Decorator----------------------

# class Employee:
#     language = "Python" 
#     salary = "120000"

#     def get_info(self):
#         return f"Employee language is {self.language} and salary is {self.salary}"
    
#     @staticmethod    # static method does not take self as dirst argument
#     def greet():
#         return f"hello from Employee Class"
    
# alice = Employee()
# print(alice.get_info())
# print(alice.greet())





# class Employee:

#     # constructor is a special method which is called when an object is created cunstructor is also called initializer and dunder method
#     def __init__(self, name, age, salary, language):  
#         print("Constructor is called")
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.language = language

#     def get_info(self):
#         return f"Employee language is {self.language} and salary is {self.salary}"
    
#     @staticmethod    # static method does not take self as dirst argument
#     def greet():
#         return f"hello from Employee Class"
    

# alice = Employee("alice", 20, 2000000, "Python")
# print(f"Employee name is {alice.name}, he is {alice.age} years old, and earn {alice.salary} PKR per month, with {alice.language} Programing Language")

























#                        ----------------------Inheritance----------------------

#                        **********************Single Inheritance**********************

# class Employee:      # Base class or Parent class 
#     company = "ICT"

#     def show(self):
#         return f"The name of Employee Company is {self.company}"


# class Programmer(Employee):      # Drive class or Child class
#     company = "ICT Tech"

#     # Don't need to define show method again here, because it will be inherited from Employee class
#     # def show(self):
#     #     return f"The name of Programmer Company is {self.company}"

#     def show_language(self, name, language):    
#         return f"The name is {name}, and he is Good with {language} language"

# a = Employee()
# b =  Programmer()

# print(a.company)
# print(b.show())











