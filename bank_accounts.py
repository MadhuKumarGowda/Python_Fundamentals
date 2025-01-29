class BalanceException(Exception):
  pass
  
class BankAccount:
    def __init__(self, accountName, initialAmt):
      self.name = accountName     
      self.balance = initialAmt
      print(f"\nAccount {self.name} created.\nBalance = ${self.balance:.2f}")
      
    
    def getBalance(self):
      print(f"\nAccount {self.name} has balance of ${self.balance:.2f}")
      
    def deposit(self, amount):
      self.balance += amount
      print(f"\n${amount} has been deposited.")
      self.getBalance()
      
    def viableTransaction(self,amount):
      if self.balance >=  amount:
        return
      else:
        raise BalanceException(f"Sorry, {self.name} doesn't have sufficient money in your account.")
    
    def withdraw(self, amount):
      try:
        self.viableTransaction(amount)
        self.balance -= amount
        print(f"Withdraw done.")
        self.getBalance()
      except BalanceException as error:
        print(f"\n {error}")
        
    def transfer(self, amount, account):
      try:
        print("Beginning Transfer 🚀".center(75, "*"))
        self.viableTransaction(amount)
        self.withdraw(amount)
        account.deposit(amount)
        print(f"\n Transfer Completed. ✔")
      except BalanceException as error:
         print(f"\n {error} ❌")
         
class InterestRewardsAcct(BankAccount):
  def deposit(self, amount):
    self.balance += amount + (amount * 0.5)
    print("\n Deposit completed")
    self.getBalance()
      
class SavingsAccount(InterestRewardsAcct):
  def __init__(self, accountName,initialAmt):
    super().__init__(accountName, initialAmt)
    self.fee = 5
    
  def withdraw(self, amount):
    try:
      self.viableTransaction(amount + self.fee)
      self.balance -= (amount + self.fee)
      print(f"\nWithdraw completed.")
      self.getBalance()
    except BalanceException as error:
       print(f"\n {error} ❌")
