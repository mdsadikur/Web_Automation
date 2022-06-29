'''
Object oriented programming
'''

class Calculator:

    def add_number(self, a, b):
        print(a + b)

    def sub_number(self, a, b):
        print(a - b)

    def name_upper(self, name):
        print(name.upper())


obj = Calculator()
obj.sub_number(20, 10)
obj.add_number(50, 50)
obj.name_upper('john')

