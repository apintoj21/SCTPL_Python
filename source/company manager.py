class Employee():
    count = 0
    def __init__(self, salary, emp, repID, eID):
        self.salary=salary
        self.EType = emp
        self.reporting_to = repID
        
    def add (self,salary, emp, repID):
        self.eID = Employee.count+1

        

         
class HourlyEmployee(Employee):
    def __init__(self,hours, salary, managerID,etype='Hourly'):
        Employee.__init__(self,salary,etype,managerID)
        self.payment=(self.salary)*(self.hour)
        
class SalariedEmployee(Employee):
    def __init__(self, salary, managerID,etype='Salaried'):
        Employee.__init__(self,salary,etype,managerID)
        self.payment=(self.salary)/12    
        
class Manager(Employee):
    def __init__(self,salary,executiveID,etype='Manager'):
        Employee.__init__(self, salary, executiveID,etype='Manager')
        self.payment=(self.salary)/12    
        
class Executive(Employee):
    def __init__(self,name,salary,None,etype='Executive', bonus):
        Employee.__init__(self)
        self.bonus = bonus
        self.payment = (self.salary)/12 + bonus
        
class Manager(Employee):
    def __init__(self,name,salary):
super(Manager,self).__init__(name,salary)
