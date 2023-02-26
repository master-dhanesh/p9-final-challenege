import json
from pathlib import Path
import random
import string


class Employee:
    __database = "Package/employee.json"
    # __employee is the database where all employee present
    # use Employee.__employee to access and manipulate database
    __employee = []

    try:
        if not Path(__database).exists():
            with open(__database, 'w') as fw:
                fw.write(json.dumps(__employee))
        else:
            with open(__database, 'r') as fr:
                __employee = json.loads(fr.read())
    except Exception as err:
        print("ERROR >> ", err)

    @classmethod
    def UpdateData(cls):
        try:
            with open(cls.__database, 'r') as fr:
                cls.__employee = json.loads(fr.read())
        except Exception as err:
            print("ERROR >> ", err)

    # create a dunder/magic method, so that if user try to print
    # object it should print "CAN NOT ACCESS DATA DIRECTLY." instead
    # of showing object address.

    def RegisteredEmployees(self):
        return self.__employee

    def __generateid(self):
        # write a code to generate random 8 alphanumeric-symbolic id
        # widht the help of random and string package
        # and return the generated id
        pass

    @classmethod
    def ShowAllEmployee(cls):
        return cls.__employee

    def CreateEmp(self):
        try:
            emp = {}
            # write a code to create an employee and append it in __employee
            # in emp(dict) take inputs from user
            # id from genetateid()
            # name from user input
            # email from user input
            # designation from user input
            # and append it in Employee.__employee.

            with open(Employee.__database, 'w') as fw:
                fw.write(json.dumps(Employee.__employee))

            Employee.UpdateData()
            return f"{emp['name']} WITH ID {emp['id']} REGIASTERED SUCCESSFULLY!"
        except Exception as err:
            print("ERROR >> ", err)

    def ReadSingleEmp(self):
        try:
            id = input("Enter Employe Id: ")
            for i, v in enumerate(Employee.__employee):
                if v['id'] == id:
                    return f"Employe Information >> {v}"
            return "EMPLOYEE NOT FOUND!"
        except Exception as err:
            print("ERROR >> ", err)

    def ReadAllEmp(self):
        # write the code to read all employees and return them.
        # must user exception handling
        pass

    def DeleteEmp(self):
        try:
            id = input("Enter Employe Id: ")

            filterdump =  # start coding here
            # write the logic to delete the employe with the help of id
            # and store it in filterdump

            with open(Employee.__database, 'w') as fw:
                fw.write(json.dumps(filterdump))

            Employee.UpdateData()
            return "Employee Deleted!"
        except Exception as err:
            print("ERROR >> ", err)

    def UpdateEmp(self):
        try:
            id = input("Enter Employe Id: ")
            for i, v in enumerate(Employee.__employee):
                if id == v["id"]:
                    print("SKIP BY PRESSING ENTER ")
                    updatedemp = {}
                    updatedemp['name'] = input("Enter Updated Employe Name: ")
                    updatedemp['email'] = input(
                        "Enter Updated Employe Email: ")
                    updatedemp['designation'] = input(
                        "Enter Updated Employe Designation: ")

                    if not updatedemp['name'].strip():
                        del updatedemp['name']
                    if not updatedemp['email'].strip():
                        del updatedemp['email']
                    if not updatedemp['designation'].strip():
                        del updatedemp['designation']

                    Employee.__employee[i] = {**v, **updatedemp}

                    with open(Employee.__database, 'w') as fw:
                        fw.write(json.dumps(Employee.__employee))

                    Employee.UpdateData()

                    return f"EMPLOYEE WITH ID {v['id']} HAS BEEN UPDATED SUCCESSFULLY!"
            return "EMPLOYEE NOT FOUND!"
        except Exception as err:
            print("ERROR >> ", err)


emp = Employee()
CreateEmp = emp.CreateEmp
UpdateEmp = emp.UpdateEmp
ReadSingleEmp = emp.ReadSingleEmp
DeleteEmp = emp.DeleteEmp
ReadAllEmp = emp.ReadAllEmp

while(True):
    print("1. Create Employee")
    print("2. Read Single Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("0. Exit Application")
    try:
        n = int(input("Enter Your Choice: "))
        if n == 1:
            print(CreateEmp())
        elif n == 2:
            print(ReadSingleEmp())
        elif n == 3:
            print(UpdateEmp())
        elif n == 4:
            print(DeleteEmp())
        elif n == 69:
            print(ReadAllEmp())
        elif n == 0:
            print("APPLICATION CLOSED!")
            exit(0)
    except Exception as err:
        print("ERROR >>", err)
