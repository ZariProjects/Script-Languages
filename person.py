import datetime

class Person:
    def __init__(self, birth_year, birth_month, birth_day):
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day
    def getAge(self):
        current_year = datetime.date.today().year
        current_month = datetime.date.today().month
        current_day = datetime.date.today().day
        age_year = current_year - self.birth_year
        age_month = current_month - self.birth_month
        age_day = current_day - self.birth_day
        if(age_month < 0):
            age_year -= 1
            age_month *= -1
        if(age_day < 0):
            age_month -= 1
            age_day *= -1
        print(age_year)
        print(age_month)
        print(age_day)
        
    
age= Person(2000, 12, 11)
age.getAge()
