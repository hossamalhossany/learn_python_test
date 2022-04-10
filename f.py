<<<<<<< HEAD
# from datetime import date

# # current_date = datetime.now()

# # current_day = current_date.day
# # current_month = current_date.month
# # current_year = current_date.year

# _today = datetime.date.today()

# # print(current_date)
# # print(current_month)
# # print(current_year)

# print(_today)


from datetime import datetime
current_date=datetime.now()
print(current_date.year,current_date.month,current_date.day)
=======
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
>>>>>>> b7fefdd81f912c83294a24d21594452ea48932e8
