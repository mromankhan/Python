# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def show_num(self):
#         return f"{self.real}i + {self.img}j"
    
#     def __add__(self, num2):
#         new_real = self.real + num2.real
#         new_img = self.img + num2.img
#         return Complex(new_real, new_img)
    
#     def __sub__(self, num2):
#         new_real = self.real - num2.real
#         new_img = self.img - num2.img
#         return Complex(new_real, new_img)
        

# num1 = Complex(1, 3)
# print(num1.show_num())


# num2 = Complex(4, 6)
# print(num2.show_num())


# num3 = num1 + num2
# print(num3.show_num())


# num3 = num1 - num2
# print(num3.show_num())







# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def show_details(self):
#         print(f"""
#             Employee Role is {self.role}
#             Employee Department is {self.dept}
#             Employee Salary is {self.salary}""")








# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "5000000")



# e = Engineer("alice", 19)
# e.show_details()
        









class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price
    
odr1 = Order("fries", 50)
odr2 = Order("tea", 20)

print(odr1 > odr2)