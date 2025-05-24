class Counter:
    def __init__(self, initial_value=1):
        self.k = initial_value

counter = Counter()

x = input(f'1 - оставить значение по умолчанию({counter.k})\n2 - задать значение счетчику\n')
if x == '2':
    initial_value = int(input('Введите значение: '))
    counter = Counter(initial_value)

while True:
    print('\n1 - увеличить на 1\n2 - уменьшить на 1\n3 - текущее состояние')
    a = input()
    if a == '1':
        counter.k += 1
    elif a == '2':
        counter.k -= 1
    elif a == '3':
        print(counter.k)
    else:
        break
