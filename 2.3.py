class Num:
    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b
nums = Num()

while True:
    print('\n1 - вывести числа\n2 - изменить числа\n3 - найти сумму чисел\n4 - найти наибольшее число')
    a = input()
    if a == '1':
        print(f"Числа: {nums.a}, {nums.b}")
    elif a == '2':
        nums.a = int(input('Введите первое число: '))
        nums.b = int(input('Введите второе число: '))
    elif a == '3':
        print(f'{nums.a} + {nums.b} = {nums.a + nums.b}')
    elif a == '4':
        print(f'Наибольшее число: {max(nums.a, nums.b)}')
    else:
        break