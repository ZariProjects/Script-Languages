class Account:
    def __init__(self, name, account_id, balance):
        self.name = name
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def get_money(self, amount):
        if(amount <= self.balance):
            self.balance -= amount
        
    def get_info(self):
        print(f"Name: {self.name}; Account id: {self.account_id}; Balance: {self.balance}")


acc = Account("George", "1212", 1000)
print(acc.balance)
acc.get_money(50)
print(acc.balance)
acc.get_money(9950)
print(acc.balance)
acc.get_info()