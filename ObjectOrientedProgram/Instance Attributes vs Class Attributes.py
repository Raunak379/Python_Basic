#Create a class BankAccount with a class attribute bank_name = "HDFC" and instance attributes holder_name and balance.
class BankAccount:
    bank_name = "HDFC"
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance
acc1 = BankAccount("Raunak", 5000)
acc2 = BankAccount("Aman", 12000)
print("Bank Name:", BankAccount.bank_name)
print("Account Holder:", acc1.holder_name)
print("Balance:", acc1.balance)
print("Account Holder:", acc2.holder_name)
print("Balance:", acc2.balance)

#Create 3 accounts, print each one's bank_name — confirm they're all the same.
class Bank:
    Bank_name = "hdfc"
    def __init__(self,name):
        self.name = name
Acc1 = Bank("Raunak")
Acc2 = Bank("Mehak")
Acc3 = Bank("himanshi")
print("Bank Name = ",Bank.Bank_name,",Holder name = ",Acc1.name)
print("Bank Name = ",Bank.Bank_name,",Holder name = ",Acc2.name)
print("Bank Name = ",Bank.Bank_name,",Holder name = ",Acc3.name)

#Now change bank_name using just one object (like acc1.bank_name = "SBI") 
#Print bank_name for all 3 objects and the class itself. Explain in your own words why the result looks the way it does.
class Bank:
    Bank_name = "hdfc"
    def __init__(self,name):
        self.name = name
Acc1 = Bank("Raunak")
Acc2 = Bank("Mehak")
Acc3 = Bank("himanshi")
Acc1.Bank_name = "sbi"
print("acc1:", Acc1.Bank_name)
print("acc2:", Acc2.Bank_name)
print("acc3:", Acc3.Bank_name)
print("Class", Bank.Bank_name)

#Create a class Counter with a class attribute count = 0. Inside __init__, increment it: Counter.count += 1, every time a new object is created. 
# Create 5 objects, then print Counter.count. What does this demonstrate about class attributes being shared?
class counter:
    count = 0
    def __init__(self):
        counter.count += 1

o1 = counter()
o2 = counter()
o3 = counter()
o4 = counter()
o5 = counter()
print(counter.count)

