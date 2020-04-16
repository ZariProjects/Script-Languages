import random
import string
import json

class Account:
    def __init__(self, name, balance):
        self.name = name
        id_size = random.randint(10, 20)
        random_id = ""
        for random_digit in range(id_size):
            random_digit = str( random.randint(1, 9) )
            random_letter = random.choice('a')
            random_id = random_id + random_digit + random_letter
        self.balance = balance
        self.id = random_id

    def deposit(self, amount):
        self.balance += amount

    def get_money(self, amount):
        if(amount <= self.balance):
            self.balance -= amount
        
    def get_info(self):
        print(f"Name: {self.name}; Account id: {self.account_id}; Balance: {self.balance}")

    def info_save_in_json(self):
        info = {
            'Name' : self.name,
            'Id' : self.id,
            'Balance' : self.balance
        }
        with open("json_file.json", "w+") as file:
            json.dump(info, file)

    def get_info_from_json_file(self):
        Account.info_save_in_json(self)
        file = open('json_file.json')
        account = json.load(file)
        print(account)
        
        
        

acc = Account("George", 1000)
print(acc.balance)
acc.get_money(50)
print(acc.balance)
acc.get_money(9950)
print(acc.balance)
acc.info_save_in_json()
acc.get_info_from_json_file()
