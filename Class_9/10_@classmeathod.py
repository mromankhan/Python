#                        ----------------------@classmethod Decorator----------------------

# class Employee:
#     a = 10

#     @classmethod    # @classmethod is always save and send the Class Attribute not instance or object Attribute 
#     def show(cls):
#         print(f"The value of class attribute is {cls.a}")



# e = Employee()
# e.a = 50
# e.show()










# class Person:
#     name = "Anonymous"

#     def change_name(self, name):
#         self.name = name


# p = Person()
# p.change_name("alice")
# print(p.name)
# print(Person.name)









# class Person:
#     name = "Anonymous"

#     def change_name(self, name):
#         self.__class__name = name


# p = Person()
# p.change_name("alice")
# print(p.name)
# print(Person.name)

















# class Person:
#     name = "Anonymous"

#     def change_name(self, name):
#         Person.name = name


# p = Person()
# p.change_name("alice")
# print(p.name)
# print(Person.name)







# class Person:
#     name = "Anonymous"

#     @classmethod
#     def change_name(cls, name):
#         cls.name = name


# p = Person()
# print(Person.name)
# p.change_name("Alice")
# print(Person.name)