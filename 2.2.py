class Train:
    def __init__(self, destination='Саратов', number='42', time='10:30'):
        self.destination = destination
        self.number = number
        self.time = time

train_obj = Train()

number = input('Введите номер поезда: ')
if number == train_obj.number:
    print(f'Пункт назначения: {train_obj.destination}\nВремя отправления: {train_obj.time}')
else:
    print('Не удалось найти поезд с таким номером')