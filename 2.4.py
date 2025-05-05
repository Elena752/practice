class counter:
    k = 1

x = input(f'1 - оставить значение по умолчанию({counter.k})\n2 - задать значение счетчику\n')
if x == '2':
    counter.k = int(input('введите значение'))
while True:
    print('\n1 - увеличеть на 1\n2 - уменьшить на 1\n3 - текущее состояние')
    a = input()
    if a == '1':
        counter.k += 1
    elif a == '2':
        counter.k -= 1
    elif a == '3':
        print(counter.k)
    else:
        break