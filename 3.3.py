class Calculation:
    calculationLine = '6'
    def SetCalculationLine(self):
        self.calculationLine = input()
    def SetLastSymbolCalculationLine(self):
        self.calculationLine += input()
    def GetCalculationLine(self):
        print(self.calculationLine)
    def GetLastSymbol(self):
        print(self.calculationLine[-1])
    def DeleteLastSymbol(self):
        self.calculationLine = self.calculationLine[:-1]
x = Calculation()
print('1 - изменить значение\n2 - добавить символ в конец строки\n3 - вывести значение\n4 - вывести последний символ\n5 - удалить последний символ')
while True:
    a = input()
    if a == '1':
        x.SetCalculationLine()
    elif a == '2':
        x.SetLastSymbolCalculationLine()
    elif a == '3':
        x.GetCalculationLine()
    elif a == '4':
        x.GetLastSymbol()
    elif a == '5':
        x.DeleteLastSymbol()
    else:
        break