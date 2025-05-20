class Worker:
    def __init__(self, name, surname, rate, days):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days
    def get_name(self):
        return self.__name
    def get_surname(self):
        return self.__surname
    def get_rate(self):
        return self.__rate
    def get_days(self):
        return self.__days
    def inf(self):
        print(f"Имя: {self.get_name()} {self.get_surname()}")
        print(f"Ставка: {self.get_rate()} руб/день")
        print(f"Отработано дней: {self.get_days()}")
    def GetSalary(self):
        return self.__rate * self.__days
worker = Worker('a', 'b', 18000, 20)
worker.inf()
print(f"Зарплата: {worker.GetSalary()} руб")