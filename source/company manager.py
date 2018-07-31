
class Employee:
    count = 0
    record={}
    def __init__(self,salary,etype):
        self.etype = etype
        self.salary = salary
        Employee.count += 1
        Employee.record[Employee.count] = [self.etype,self.salary]
    

    def add_employee(self,etype,salary):
        Employee.record[Employee.count+1] = [etype,salary]
        
    def del_employee(self,Id):
        del(Employee.record[Id])
    
        

class HourlyEmployee(Employee):
    def __init__(self, salary, no_hours):
            Employee.__init__(self, Id, salary)
        self._manager = manager

    def getManager(self):
        return self._manager

class Executive(Employee):
    def __init__(self, Id, wage, yearlyBonus):
        Employee.__init__(self, Id, wage) 
        self._yearlyBonus = yearlyBonus

    def wage(self):
        return Employee.wage(self)























