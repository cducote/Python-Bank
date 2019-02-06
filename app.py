#Simple Bank Account

class BankAccount:
  def __init__(self, account_type):
    self.type = account_type
    self.balance = 0

  def withdraw(self, amount):
    self.balance -= amount
    return amount

  def deposit(self, amount):
    self.balance += amount
    return self.balance

#More Advanced
# class BankAccount:
#   def __init__(self, account_type):
#     self.type = account_type
#     self.balance = 0

#   def withdraw(self, amount):
#     if self.balance - amount < 0:
#       return 'Insufficient funds.'
#     self.balance -= amount
#     return amount

#   def deposit(self, amount):
#     self.balance += amount
#     return self.balance

#The most Advanced
# class BankAccount:
#   def __init__(self, account_type):
#     self.type = account_type
#     self.balance = 0
#     self.overdraft_fees = 0

#   def withdraw(self, amount):
#     net_balance = self.balance - amount - self.overdraft_fees
#     self.balance -= amount if net_balance >= -100 else 0
#     if net_balance < -100:
#       return 'Insufficient Funds'
#     if self.balance < 0:
#       self.overdraft_fees += 20
#     return amount

#   def deposit(self, amount):
#     self.balance += amount
#     return self.balance