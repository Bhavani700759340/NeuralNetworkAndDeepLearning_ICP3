'''In class programming:
1. Create a class Employee and then do the following
• Create a data member to count the number of Employees
• Create a constructor to initialize name, family, salary, department
• Create a function to average salary
• Create a Fulltime Employee class and it should inherit the properties of Employee class
• Create the instances of Fulltime Employee class and Employee class and call their member functions.'''

class Employee:
    ecount = 0  # Data member to count the number of Employees

    def __init__(self, ename, efamily, esalary, edepartment):
        self.ename = ename
        self.efamily = efamily
        self.esalary = esalary
        self.edepartment = edepartment
        Employee.ecount += 1

    def averageSalary(self, totalSalary):
        return totalSalary / Employee.ecount

class FulltimeEmployee(Employee):
    # Inheriting properties from the Employee class
    pass

# Creating instances of Employee class
employee1 = (
    Employee("Bhavani", "Dasari", 200000, "CSE"))
employee2 = (
    Employee("Sindhuri", "Dasari", 70000, "ECE"))

# Creating instances of FulltimeEmployee class
fulltimeEmployee1 = (
    FulltimeEmployee("Sanju", "Reddy", 65000, "HR"))
fulltimeEmployee2 = (
    FulltimeEmployee("Harika", "Srivanas", 75000, "IT"))

# Calling member functions
totalSalaryOfEmployees = employee1.esalary + employee2.esalary
averageSalaryOfEmployees = employee1.averageSalary(totalSalaryOfEmployees)

totalSalaryOfFulltimeEmployees = fulltimeEmployee1.esalary + fulltimeEmployee2.esalary
averageSalaryOfFulltimeEmployees = fulltimeEmployee1.averageSalary(totalSalaryOfFulltimeEmployees)

# Displaying results
print("Average Salary for Employees:", averageSalaryOfEmployees)
print("Average Salary for Fulltime Employees:", averageSalaryOfFulltimeEmployees)
