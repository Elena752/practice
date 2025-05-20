class Calculation:
    def __init__(self, calculationLine='6'):
        self.calculationLine = calculationLine
    def SetCalculationLine(self):
        self.calculationLine = input("Введите новую строку: ")
    def SetLastSymbolCalculationLine(self):
        self.calculationLine += input("Введите символ для добавления: ")
    def GetCalculationLine(self):
        print("Текущая строка:", self.calculationLine)
    def GetLastSymbol(self):
        print("Последний символ:", self.calculationLine[-1])
    def DeleteLastSymbol(self):
        self.calculationLine = self.calculationLine[:-1]
        print("Последний символ удалён.")

calc = Calculation()
print('1 - изменить значение')
print('2 - добавить символ в конец строки')
print('3 - вывести значение')
print('4 - вывести последний символ')
print('5 - удалить последний символ')

while True:
    a = input("\nВыберите действие: ")
    if a == '1':
        calc.SetCalculationLine()
    elif a == '2':
        calc.SetLastSymbolCalculationLine()
    elif a == '3':
        calc.GetCalculationLine()
    elif a == '4':
        calc.GetLastSymbol()
    elif a == '5':
        calc.DeleteLastSymbol()
    else:
        break