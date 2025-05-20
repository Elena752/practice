class Worker:
    def __init__(self, name='a', surname='b', rate=1000, days=4):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days
    def GetSalary(self):
        return self.rate * self.days
    def inf(self):
        print(f"Имя: {self.name} {self.surname}")
        print(f"Ставка: {self.rate} руб/день")
        print(f"Отработано дней: {self.days}")

worker = Worker()
worker.inf()
print(f"Зарплата: {worker.GetSalary()} руб")
