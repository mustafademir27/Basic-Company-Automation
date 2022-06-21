class Company():    
    def __init__(self,name):
        self.name = name    #name of company
        self.run = True

    def program(self):
        choice = self.menu()
        if choice == 1:
            self.hireEmployee()
        if choice == 2:
            self.fireEmployee()
        if choice == 3:
            self.totalSalary()   ## monthly salary
        if choice == 4:
            self.giveSalary()


    def menu(self):
        choice = int(input("\n\n***Welcome to {} Company***\n\nPlease choose what you want to do\n1-Hire Employee\n2-Fire Employee\n3-Total Salary to be paid\n4-Pay Salary\nChoose = ".format(self.name)))
        while choice < 1 or choice > 6:
            choice = int(input("Please make a choice between 1-6 : "))  ## the process to be do
        return choice

    def hireEmployee(self):
        id = 1      ## id number of employee.
        name = input("Name of Employee : ")
        surname = input("Surname of Employee : ")
        age = input("Age of Employee : ")
        gender = input("Gender of Employee : ")
        salary = input("Salary of Employee : ")

        with open("employeess.txt","r") as file:
            employeesList = file.readlines()

        if len(employeesList) == 0:
            id = 1
        else:
            with open("employeess.txt","r") as file:
                id = int(file.readlines()[-1].split(")")[0]) + 1
        
        with open("employeess.txt","a+") as file:
            file.write("{}){}-{}-{}-{}-{}\n".format(id,name,surname,age,gender,salary))

    def fireEmployee(self):
        with open("employeess.txt","r") as file:
            employess = file.readlines()

        displayEmployess = []   ## to add employess to new list
        for employee in employess:
            displayEmployess.append(" ".join(employee[:-1].split("-")))     ## [:-1] is for remove "\n" in the end of the line . split("-") is for remove "-" between words and " ".join is for add space between words

        for employee in displayEmployess:   ##to display all employess on the screen
            print(employee)

        choice = int(input("Please choose a id number of employee that you want to hire (1- {}) = ".format(len(displayEmployess))))
        while choice > 6 or choice < 1:
            choice = int(input("Please choose a id number of employee between (1-{}) = ".format(len(displayEmployess))))

        employess.pop(choice - 1)   ## remove the chosen employee

        changedEmployee = []    ## for new employeess text  
        counter = 1
        for employee in employess:
            changedEmployee.append( str(counter) + ")" + employee.split(")")[1] )   ## .split(")")[1] mean is that separate the line in the ) point and get 1. index
            counter += 1

        with open("employeess.txt","w") as file:    ## write new situation of employees list to employeess.txt
            file.writelines(changedEmployee)

    def totalSalary(self):
        with open("employeess.txt","r") as file:
            employees = file.readlines()

        salary = []   ## to keep salary of employees

        for employee in employees:
            salary.append(int(employee.split("-")[-1]))    ## split("-")[-1] mean is that separate the line in the - points and get last index 

        print("Total salary to be paid in this month = {}".format(sum(salary)))
        

    def giveSalary(self):
        with open("employeess.txt","r") as file:
            employees = file.readlines()
        salary = []     ## to keep salary of employees
        for employee in employees:
            salary.append(int(employee.split("-")[-1]))
        totalSalary = sum(salary) 

        ### get the budget info from budget.txt

        with open("budget.txt","r") as file:
            budget = int(file.readlines()[0])
            
        Currentbudget = budget - totalSalary
        print("Budget before not to pay salary= {}".format(budget))
        print("Budget after to pay salary = {}".format(Currentbudget))
        with open("budget.txt","w") as file:
            file.write(str(Currentbudget))



company1 = Company("Google")
company1.program()