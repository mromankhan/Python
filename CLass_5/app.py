#                        ----------------------Task_1----------------------

# inp_1 = int(input("Enter a number 1: "))
# inp_2 = int(input("Enter a number 2: "))
# inp_3 = int(input("Enter a number 3: "))
# inp_4 = int(input("Enter a number 4: "))

# if(inp_1 > inp_2  and inp_1 > inp_3 and inp_1 > inp_4):
#     print(f"The Largest number is {inp_1}")

# elif(inp_2 > inp_1 and inp_2 > inp_3 and inp_2 > inp_4):
#     print(f"The Largest number is {inp_2}")

# elif(inp_3 > inp_1 and inp_3 > inp_2 and inp_3 > inp_4):
#     print(f"The Largest number is {inp_3}")

# elif(inp_4 > inp_1 and inp_1 > inp_2 and inp_1 > inp_3):
#     print(f"The Largest number is {inp_4}")








#                        ----------------------Task_2----------------------

# mark_1 = int(input("Enter Marks number 1: "))
# mark_2 = int(input("Enter Marks number 2: "))
# mark_3 = int(input("Enter Marks number 3: "))

# total_percentage = (100 * (mark_1 + mark_2 + mark_3)) / 300

# if(total_percentage >= 40 and mark_1 >= 33 and mark_2 >= 33 and mark_3 >= 33):
#     print(f"Your total percentage is {total_percentage}% and you are pass")

# else:
#     print(f"Your total percentage is {total_percentage}% and you are fail")








#                        ----------------------Task_3----------------------

# m1 = "Make a lot of money"
# m2 = "buy now"
# m3 = "subscribe this"
# m4 = "click this"

# msg = input("Enter your message: ")

# if((m1 in msg) or (m2 in msg) or (m3 in msg) or (m4 in msg)):
#     print(f"This is a Spam Message {msg}")

# else:
#     print(f"""This is not a Spam Message: 
#           '''{msg}''' """)










#                        ----------------------Task_4----------------------

# user_name = input("Enter you Name: ")

# name_length = len(user_name)

# if(name_length < 10):
#     print(f"You name is under 10 cheracters long")

# else:
#     print(f"Your name is more than 10 cheracters long")










#                        ----------------------Task_5----------------------

# l = ["ali", "ahmad", "saad", "sami"]

# name = input("Enter your Name: ").lower()

# if(name in l):
#     print(f"Hello {name}, you are already Registered")

# else:
#     print(f"Hello {name}, you are not Registered")












#                        ----------------------Task_6----------------------

# marks = int(input("Enter your marks: "))

# if(marks <= 100 and marks >=90):
#     grade = "A+"
    
# elif(marks < 90 and marks >= 80):
#     grade = "A"

# elif(marks < 80 and marks >= 70):
#     grade = "B"

# elif(marks < 70 and marks >= 60):
#     grade = "C"

# elif(marks < 60 and marks >= 50):
#     grade = "D"

# elif(marks < 50):
#     grade = "F"

# print(f"Your grade is {grade}")













#                        ----------------------Task_7----------------------


# desc = input("Enter your Description: ")

# if("positive".lower() or "positively" in desc.lower()):
#     print("This is a Positive Description")

# elif("negative".lower() or "negatively" in desc.lower()):
#     print("This is a Negative Description")