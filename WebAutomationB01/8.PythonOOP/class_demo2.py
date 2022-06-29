class Person:

    def __init__(self, name, age=20):
        self.name = name
        self.age = age


p1 = Person("John", 40)

print(p1.name)
print(p1.age)

p2 = Person("Smith", 50)
print(p2.name)
print(p2.age)
