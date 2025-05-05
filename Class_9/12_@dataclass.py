from dataclasses import dataclass, asdict, astuple, replace

# @dataclass is a Decorator that was generate Specific Methods like __init__() __repr__() __eq__() etc 
# Dont need to write Constructors and methos manually in dataclass

# @dataclass
# class Book:
#     name: str
#     author: str
#     price: float

# b1 = Book("Python", "John", 499.99)
# b2 = Book("Python", "John", 499.99)

# print(b1)
# print(b1.author)
# print(b1 == b2)







# __init__ method will not generate
# @dataclass(init=False) # by default in dataclass init=True
# class Book:
#     name: str
#     author: str
#     price: float

# b1 = Book("Python", "John", 499.99)
# b2 = Book("Python", "John", 499.99)

# # print(b1)
# print(b1.author)
# print(b1 == b2)















# # no print friendly class
# @dataclass(repr=False) # by default in dataclass repr=True
# class Book:
#     name: str
#     author: str
#     price: float

# b1 = Book("Python", "John", 499.99) 
# b2 = Book("Python", "John", 499.99)

# print(b1)  # not working correctly print the refrence because repr=False
# print(b1.author)
# print(b1 == b2)
















# # dont generate __eq__ method
# @dataclass(eq=False) # by default in dataclass eq=True
# class Book:
#     name: str
#     author: str
#     price: float

# b1 = Book("Python", "John", 499.99) 
# b2 = Book("Python", "John", 499.99)

# print(b1) 
# print(b1.author)
# print(b1 == b2) # print False because __eq__ method are not generated because eq=False


















# @dataclass(order=True) # by default in dataclass order=False
# class Book:
#     name: str
#     author: str
#     price: float

# b1 = Book("Python", "John", 499.99) 
# b2 = Book("Python", "John", 499.99)

# # print(b1) 
# # print(b1.author)
# print(b1 == b2) # prints True because order=True 

















# # make the class immutable
# @dataclass(frozen=True) # by default in dataclass frozen=False 
# class Config:
#     db_name: str

# cnfg = Config("test")
# cnfg.db_name = "new"
# print(cnfg.db_name) # print error because db_name is immutable



















# @dataclass
# class Book:
#     name: str
#     author: str
#     price: float

# b1 = Book("Python", "John", 499.99)
# b2 = Book("Python", "John", 499.99)

# # replace: copy the instance of given dataclass and relace the value and return copied class
# b3 = replace(b2, price = 500.00)
# print(b3)

# # asdict: converts the class properties into Dictionary
# print(asdict(b1)) # prints {'name': 'Python', 'author': 'John', 'price': 499.99}

# # astuple: converts the class properties into Tuple
# print(astuple(b2)) # prints ('Python', 'John', 499.99)


























































# @dataclass
# class Employee:
#     name: str = "Anonymous"
#     age: int = 20
#     company: str = "Google"

#     def employee_info(self):
#         return f"Employee name is {self.name}, and {self.name} is {self.age} years old and {self.name} is currently working in {self.company}."
    

# e = Employee()
# print(e)
# print(e.name, e.age)
# print(e.employee_info())

# e = Employee("Alice", 20, "microsoft")
# print(e)
# print(e.name, e.age)
# print(e.employee_info())
