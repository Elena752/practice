class num:
    a = 1
    b = 2

while True:
    print('\n1 - вывecти числа\n2 - изменить числа\n3 - найти сумму чисел\n4 - найти наибольшее число')
    a = input()
    if a == '1':
        print(num.a, num.b)
    elif a == '2':
        num.a = int(input('Введите первое число: '))
        num.b = int(input('Введите второе число: '))
    elif a == '3':
        print(f'{num.a} + {num.b} = {num.b+num.a}')
    elif a == '4':
        if num.a > num.b:
            print(num.a)
        else:
            print(num.b)
    else:
        break