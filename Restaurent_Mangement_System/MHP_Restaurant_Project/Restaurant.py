# from Menu import Menu



# # RestaurantSystem class er moddhe restaurant system er properties thakbe
        
# class RestaurantSystem:
#     def __init__(self, Name ):
#         self.Name = Name
#         self.employees = [] #eta base hisebe use hobe 
#         self.menu = Menu()
        

#     def add_employee(self, new_employee):
#         self.employees.append(new_employee)


#     def view_employee(self):
#         print("Employee List:")
#         for emp in self.employees:
#             print(f"Name: {emp.Name}, Email: {emp.Email}, Address: {emp.Address}, Phone: {emp.Phone}, Age: {emp.Age}, Designation: {emp.Designation}, Salary: {emp.Salary}, EmployeeID: {emp.EmployeeID}")
#             # print(emp.name, emp.Email, emp.Address, emp.Phone, emp.Age, emp.Designation, emp.Salary, emp.EmployeeID)

from Menu import Menu

class RestaurantSystem:
    def __init__(self, Name):
        self.Name = Name
        self.employees = []
        self.menu = Menu()

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def view_employee(self):
        if not self.employees:
            print("No employees yet.")
            return
        print("Employee List:")
        for emp in self.employees:
            print(f"Name: {emp.Name}, Email: {emp.Email}, Address: {emp.Address}, Phone: {emp.Phone}, Age: {emp.Age}, Designation: {emp.Designation}, Salary: {emp.Salary}, EmployeeID: {emp.EmployeeID}")
