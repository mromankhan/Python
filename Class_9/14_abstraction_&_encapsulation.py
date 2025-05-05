#                        ----------------------Abstraction & Encapsulation----------------------

# Abstraction = Hide Extra (Unnecessory) Details from User and only showing the essential features to the user
# Encapsulation = wrap the many components (Data) in one parent or Single Unit like Employee

# class Employee:     # Encapsulation
#     def __init__(self, name):
#         self.name = name

#     @property
#     def get_name(self):
#         return self.name

#     @get_name.setter         # Abstraction
#     def get_name(self, value):
#         if not value:
#             raise ValueError("Name cannot be empty")
#         self.name = value

    
# e = Employee("Alice ilos")
# e.name = 0
# print(e.name)            # Dont neet for () because this is property from @property decorator
# # print(e.get_name)






# class Car:  # Encapsulation 

#     def __init__(self):
#         self.acc = False
#         self.clutch = False
#         self.brk = False


#     def start_car(self):   # Abstraction
#         print("Car Starting...")
#         self.acc = True    # hide from user 
#         self.clutch = True # hide from user 
#         print("Car Started")


# car_1 = Car()
# car_1.start_car()