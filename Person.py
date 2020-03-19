class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __add__(self, other_obj):
        return self.age + other_obj.age

    def __sub__(self, other_obj):
        return self.age - other_obj.age
    
    def __mul__(self, other_obj):
        return self.age * other_obj.age
    
    def __radd__(self, age):
        p3 = Person("Chochko", self.age + age)
        return p3


p1 = Person("Goshko", 15)
p2 = Person("Ivan", 14)