class Worker:
    name = 'a'
    surname = 'b'
    rate = 1000
    days = 4
    def GetSalary(self):
        print(self.rate*self.days)
a = Worker()
a.GetSalary()