class Student:
    def __init__(self, surname='ab', date='02.08.2005', group='123', grade=[5, 3, 3, 4, 5]):
        self.surname = surname
        self.date = date
        self.group = group
        self.grade = grade

students = Student()

while True:
    print('\n1 - изменить фамилию\n2 - изменить дату рождения\n3 - изменить номер группы\n4 - вывести данные о студенте')
    a = input()
    if a == '1':
        students.surname = input('Введите фамилию: ')
    elif a == '2':
        students.date = input('Введите дату рождения(ДД.ММ.ГГГГ): ')
    elif a == '3':
        students.group = input('Введите номер группы: ')
    elif a == '4':
        print('Введите фамилию и дату рождения(ДД.ММ.ГГГГ)')
        surname = input()
        date = input()
        if surname == students.surname and date == students.date:
            print(f'Номер группы: {students.group}\nУспеваемость: {students.grade}')
        else:
            print('Не удалось найти такого студента')
    else:
        break