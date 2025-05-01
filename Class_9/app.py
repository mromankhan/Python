# class Account:
#     def __init__(self, acc_no, balance):
#         self.acc_no = acc_no
#         self.balance = balance

#     def credit(self, amount):
#         self.balance += amount
#         print(f"Rs. {amount} was Credited, Your new Balance is {self.balance}")

#     def debit(self, amount):
#         self.balance -= amount
#         print(f"Rs. {amount} was Debited, Your new Balance is {self.balance}")
        
#     @property
#     def check_balance(self):
#         print(f"Your Current Balance is Rs.{self.balance}")




# acc_1 = Account(12345, 10000)
# acc_1.debit(5000)
# acc_1.credit(50000)
# acc_1.check_balance