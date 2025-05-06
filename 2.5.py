class Fifth:
    def __init__(self, v1='1', v2='2'):
        self.value1 = v1
        self.value2 = v2

    def __del__(self):
        print(f'Удаление объекта со свойствами: {self.value1}, {self.value2}')

    def display_properties(self):
        print(f'Свойства объекта: {self.value1}, {self.value2}')
print("1. Создание объекта с параметрами:")
obj1 = Fifth('rer', 123)
obj1.display_properties()

print("\n2. Создание объекта с одним параметром:")
obj2 = Fifth(15)
obj2.display_properties()

print("\n3. Создание объекта без параметров (по умолчанию):")
obj3 = Fifth()
obj3.display_properties()


