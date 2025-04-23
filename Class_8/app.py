#                        ----------------------Task_1----------------------
# f = open("poem.txt")
# content = f.read()
# if("python" in content):
#     print("python is present")

# else:
#     print("python is not present")


# f.close()










#                        ----------------------Task_2----------------------

# import random

# def game():
#         print("You are playing the Game")
#         score = random.randint(1, 50)
#         with open("hiscore.txt") as f:
#             hiscore = f.read()
#             if hiscore != "":
#                 hiscore = int(hiscore)
#             else:
#                  hiscore = 0

#         print(f"Your score is {score}")
#         if score > hiscore:
#              with open("hiscore.txt", "w") as f:
#                 f.write(str(score))


#         return score
            

# game()











#                        ----------------------Task_3----------------------

# def generate_table(n):
#     table = ""
#     for i in range(1, 11):
#         table += f"{n} x {i} = {n * i}\n" 
#         with open(f"tables/{n}.txt", "w") as f:
#             f.write(table)


# for i in range(2, 21):
#     generate_table(i)














#                        ----------------------Task_4----------------------

# word = "Donkey"

# with open("file.txt", "r") as f:
#     content = f.read()

#     contentNew = content.replace(word, "#####")

# with open("file.txt", "w") as f:
#     f.write(contentNew)













#                        ----------------------Task_5----------------------

# words = ["Donkey", "bad", "idiot"]

# with open("file.txt", "r") as f:
#     content = f.read()

#     for word in words:
#         content = content.replace(word, "#" * len(word))


# with open("file.txt", "w") as f:
#     f.write(content)









#                        ----------------------Task_6----------------------
# with open("log.txt") as f:
#     content = f.read()

# if "python" in content:
#     print("python is present")
# else:
#     print("python is not present")








#                        ----------------------Task_7----------------------

# with open("log.txt") as f:
#     lines = f.read()

# lineno = 1
# for line in lines:
#     if "python" in line:
#         print(f"python is present {lineno}")
#         break
#     lineno += 1

# else:
#     print("python is not present")










#                        ----------------------Task_8----------------------

# with open("this.txt") as f:
#     content = f.read()


# with open("this_copy.txt", "w") as f:
#     f.write(content)






#                        ----------------------Task_9----------------------

# with open("this.txt") as f:
#     content_1 = f.read()

# with open("this_copy.txt") as f:
#     content_2 = f.read()

#     if(content_1 == content_2):
#         print("Both files are Same")
#     else:
#         print("Both files are Different")




#                        ----------------------Task_10----------------------

# with open("log.txt", "w") as f:
#     f.write("")





#                        ----------------------Task_11----------------------
# with open("log.txt") as f:
#     content = f.read()

# with open("rename.txt", "w") as f:
#     f.write(content)