"""
int str list tuple set dict
"""
#class
"""
person->name age id
Anna 23 123435
"""
class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello I'm {self.name}")

person1 = Person("Anna",23)
"""
Person.__init__(person1,"Anna",23)
person1.name = "Anna"
person1.age = 23
"""
print(person1.name)
print(person1.age)

class NoPerson:
    pass

no_person1 = NoPerson()
no_person1.age = 134
no_person1.name = "NoAnna"
no_person1.id = 12341234
print(no_person1.age)
print(no_person1.name)
no_person2 = NoPerson()
no_person2.location = "Haifa"
print(no_person2.location)
# print(no_person2.age)


person2 = Person("Alla",30,)
print(person2.name)
print(person2.age)
person1.greet()
Person.greet(person1)


person2.greet()
Person.greet(person2)

print(person1)