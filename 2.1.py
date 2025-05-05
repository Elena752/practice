class student:
    surname = 'aboba'
    date = '02.08.2005'
    group = '123'
    grade = [1, 2, 3, 4, 5]

while True:
    print('\n1 - изменить фамилию\n2 - изменить дату рождения\n3 - изменить номер группы\n4 - вывести данные о студенте')
    a = input()
    if a == '1':
        student.surname = input('Введите фамилию: ')
    elif a == '2':
        student.date = input('Введите дату рождения(ДД.ММ.ГГГГ): ')
    elif a == '3':
        student.group = input('Введите номер группы: ')
    elif a == '4':
        print('Введите фамилию и датy рождения(ДД.ММ.ГГГГ)')
        surname = input()
        date = input()
        if surname == student.surname and date == student.date:
            print(f'Номер группы: {student.group}\nУспеваемость: {student.grade}')
        else:
            print('Не удалось найти такого студента')
    else:
        break