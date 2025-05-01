#                        ----------------------Task_1----------------------
# class Programmer:
#     company = "Microsoft"

#     def __init__(self, name, salary, pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin


# p1 = Programmer("Alice", 1200000, 12345)
# print(p1.name, p1.salary, p1.pin)

# p2 = Programmer("Robin", 1200000, 56789)
# print(p2.name, p2.salary, p2.pin)









#                        ----------------------Task_2----------------------

# class Calculator:
#     def __init__(self, n):
#         self.n = n

#     def square(self):
#             print(f"Square of {self.n} is {self.n * self.n}")

#     def cube(self):
#             print(f"cube of {self.n} is {self.n * self.n * self.n}")

#     def squareroot(self):
#             print(f"squareroot of {self.n} is {self.n ** 1/2}")


# a = Calculator(5)
# a.square()
# a.cube()
# a.squareroot()









#                        ----------------------Task_3----------------------

# class Alphabet:
#       a = 4


# o = Alphabet()
# o.a = 0
# print(o.a) 
# print(Alphabet.a)









#                        ----------------------Task_4----------------------

# class Calculator:
#     def __init__(self, n):
#         self.n = n

#     def square(self):
#             print(f"Square of {self.n} is {self.n * self.n}")

#     def cube(self):
#             print(f"cube of {self.n} is {self.n * self.n * self.n}")

#     def squareroot(self):
#             print(f"squareroot of {self.n} is {self.n ** 1/2}")
    
#     @staticmethod
#     def greet():
#           print("Hello There!")

# a = Calculator(5)
# a.greet()
# a.square()
# a.cube()
# a.squareroot()










#                        ----------------------Task_5----------------------

# from random import randint

# class Train:
#     def __init__(self, train_no):
#         self.train_no = train_no

#     def book_ticket(self, fro, to):
#         print(f"Ticket is booked from {fro} to {to} in train # {self.train_no}")

#     def get_status(self):
#         print(f"Train no is {self.train_no} is Running on time")

#     def get_fare(self, fro, to):
#         print(f"Ticket Fear in train no {self.train_no} from {fro} to {to} is {randint(5555, 9999)}")



# t = Train(12345)
# t.book_ticket("Karachi", "Lahore")
# t.get_status()
# t.get_fare("Karachi", "Lahore")




















#                        ----------------------Task_6----------------------

# from random import randint

# class Train:
#     def __init__(sel, train_no):
#         sel.train_no = train_no

#     def book_ticket(alice, fro, to):
#         print(f"Ticket is booked from {fro} to {to} in train # {alice.train_no}")

#     def get_status(self):
#         print(f"Train no is {self.train_no} is Running on time")

#     def get_fare(self, fro, to):
#         print(f"Ticket Fear in train no {self.train_no} from {fro} to {to} is {randint(5555, 9999)}")



# t = Train(12345)
# t.book_ticket("Karachi", "Lahore")
# t.get_status()
# t.get_fare("Karachi", "Lahore")

























# inhertance and abs






# class Two_d_vector:

#     def __init__(self, i, j):
#         self.i = i
#         self.j = j

#     def show(self):
#         return f"The Vector of 2D is {self.i}i + {self.j}j"
    


# class Three_d_vector(Two_d_vector):

#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.k = k


#     def show(self):
#         return f"The Vector of 3D is {self.i}i + {self.j}j + {self.k}k"
    



# two_d = Two_d_vector(5, 6)
# print(two_d.show())

# three_d = Three_d_vector(5, 6, 7)
# print(three_d.show())












# p2


# class Animal:
#     pass


# class Pets(Animal):
#     pass


# class Dog(Pets):

#     @staticmethod
#     def bark():
#         return f"Bow Bow"

# d = Dog()
# print(d.bark())



















# p3

# class Employee:
#     salary = 250
#     increment = 20

#     @property
#     def salary_after_inc(self):
#         return (self.salary + self.salary * (self.increment/100))
    
#     @salary_after_inc.setter
#     def salary_after_inc(self, salary):
#         self.increment = ((salary/self.salary) - 1) * 100


# e = Employee()
# # print(e.salary_after_inc)
# e.salary_after_inc = 300
# print(e.increment)










# class Complex:

#     def __init__(self, i, r):
#         self.i = i
#         self.r = r


#     def __add__(self, c2):
#         return Complex(self.r + c2.r, self.i + c2.i)
    
#     def __str__(self):
#         return f"{self.r} + {self.i}i"
    


# c1 = Complex(1, 2)
# c2 = Complex(3, 4)
# print(c1 + c2)
