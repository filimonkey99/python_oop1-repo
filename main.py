# object orienterad programmering i python

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d = Dog("Tim", 34)
d.set_age(354)
print(d.get_age())
