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


