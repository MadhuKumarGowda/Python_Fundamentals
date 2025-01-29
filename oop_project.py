from bank_accounts import *
print("Madhu Details".center(100,"*"))
Madhu = BankAccount("Madhu", 3000)
Madhu.getBalance()
Madhu.deposit(500)
Madhu.withdraw(250)
print("Mala Details".center(100,"*"))
Mala = BankAccount("Mala", 2500)
Mala.getBalance()
Mala.deposit(1000)
Mala.withdraw(4000)

Madhu.transfer(1000, Mala)
print("Abhi Details".center(100,"*"))

Abhi = InterestRewardsAcct("Abhi", 1000)
Abhi.getBalance()
Abhi.deposit(100)
Madhu.transfer(200, Abhi)

print("Yukthi Details".center(100,"*"))
Yukthi = SavingsAccount("Yukthi", 1000)
Yukthi.withdraw(200)
