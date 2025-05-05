class train:
    destination = 'Саратов'
    number = '42'
    time = '10:30'

number = input('Введите номер поезда: ')
if number == train.number:
    print(f'Пункт назначения: {train.destination}\nВремя отправления: {train.time}')
else:
    print('Не удалось найти поезд с таким номером')
