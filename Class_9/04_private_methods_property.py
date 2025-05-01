#                    ----------------------Private Method and Properties----------------------

# Private Method and Property are not acessable out of class only use in class block


# class Employee:
#     name = "Alice"
#     __company = "Microsoft"  # it is private can't acess out of class with "__" sign but acess in class

#     def __welcome(self):   # # it is private can't acess out of class with "__" sign but acess in class
#         print("Welcome")

#     def hello(self):
#         self.__welcome()
#         print(self.__company)  # it is ok because private properties or meathods are acessable in class



# e = Employee()
# # print(e.__company)  Throw Error because company property is Private
# e.hello() 
# e.__welcome()