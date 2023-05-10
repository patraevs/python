# todo:
# Определите класс Person. При создании объекта p=Person
# (‘Иванов’, ‘Михаил’, ‘Федорович’) необходимо ввести полное имя человека.
# При печати объекта должно выводиться следующее:
# print(p) # чивородеФлиахиМвонавИ

class Person():
    first_name = 'First Name'
    last_name = 'Last Name'
    patronymic = 'Patronymic'

    def __init__(self, first_name, last_name, patronymic):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic

    def __str__(self):
        return (self.last_name + self.first_name + self.patronymic)[::-1]


p = Person("Иван", "Иванов", "Иванвоич")
print(p)
