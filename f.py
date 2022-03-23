class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def print_data(self):
        print(f'the person {self.name} has age ===  {self.age}')




# p1 = Person('hossam',44)


class Person_child(Person):
    def address(self,address):
        print(f'the person live in address {address}')

p1 = Person_child('hossam',55)


p1.print_data()
p1.address('giza')    