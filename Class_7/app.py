# 1

# def gratest_num(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else: 
#         return c

# print(gratest_num(12, 5, 50))










# 2

# def f_to_c(f):
#     c = (f - 32) * 5/9
#     return c


# f = float(input("Enter temperature in Fahrenheit: "))
# c = f_to_c(f)
# print(f"{round(c, 2)} celsius")















# 3

# print("a")
# print("b")
# print("c", end="")
# print("d", end="")







# 4
# def sum(n):
#     if(n == 1):
#         return 1
#     return sum(n-1) + n

# print(sum(2))










# 5

# def pattern(n):
#     if(n == 0):
#         return
#     print("*" * n)
#     pattern(n - 1)

# pattern(5)













# 6

# def inch_to_cm(inch):
#     return inch * 2.54


# n = int(input("Enter the number of inches: "))
# print(f"The Corresponding in cms is {inch_to_cm(n)}")










# 7

# def remove(l, word):
#     n = []
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n

# l = ["hello", "world", "shubhan", "an"]

# print(remove(l, "an"))









# 8 
# def table(n):
#     for i in range(1, 11):
#         print(f"{n} x {i} = {n * i}")


# table(5)