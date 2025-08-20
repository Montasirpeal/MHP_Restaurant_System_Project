# from Fooditem import FoodItem

# from Menu import Menu

# from Restaurant import RestaurantSystem

# from User import Customer, Admin, Employee

# from Order import Order



# MHP_Restaurant = RestaurantSystem("MHP_Restaurant")


# def customer_menu():
#     name = input("Enter your name: ")
#     email = input("Enter your email: ")
#     address = input("Enter your address: ")
#     phone = input("Enter your phone number: ")
#     customer = Customer(name = name, email = email, address = address, phone = phone)

#     while True:
#         print(f"Welcome {customer.name} to the restaurant!")
#         print("1. View Menu")
#         print("2. Add Item to Cart")
#         print("3. View Cart")
#         print("4. Pay your bill")
#         print("5. Exit")

#         choice = input("Enter your choice: ")
#         if choice == '1':
#             customer.view_menu(MHP_Restaurant)


#         elif choice == '2':
#             item_name = input("Enter the name of the item to add to cart: ")
#             quantity = int(input("Enter the quantity: "))
#             customer.add_to_cart(item_name, quantity, MHP_Restaurant)


#         elif choice == '3':
#             customer.view_cart()


#         elif choice == '4':
#             customer.pay_bill()
            
#         elif choice == '5':
#             print("Thank you for visiting!")
#             break
#         else:
#             print("Invalid choice. Please try again.")






# def admin_menu():
#     name = input("Enter your name: ")
#     email = input("Enter your email: ")
#     address = input("Enter your address: ")
#     phone = input("Enter your phone number: ")
#     admin = Admin(name=name, email=email, address=address, phone=phone)

#     while True:
#         print(f"Welcome {admin.name} to the restaurant!")
#         print("1. Add Menu New Item")
#         print("2. Add New Employee")
#         print("3. View Employees")
#         print("4. View Item in Menu")
#         print("5. Remove Item from Menu")
#         print("6. Exit")

#         choice = input("Enter your choice: ")
#         if choice == '1':
#             item_name = input("Enter the name of the item: ")
#             price = float(input("Enter the price of the item: "))
#             quantity = int(input("Enter the quantity of the item: "))
#             item = FoodItem(name=item_name, price=price, quantity=quantity)
#             admin.add_menu_item(MHP_Restaurant, item)

#         elif choice == '2':
#             emp_name = input("Enter employee name: ")
#             emp_email = input("Enter employee email: ")
#             emp_address = input("Enter employee address: ")
#             emp_phone = input("Enter employee phone number: ")
#             emp_age = int(input("Enter employee age: "))
#             emp_designation = input("Enter employee designation: ")
#             emp_salary = float(input("Enter employee salary: "))
#             emp_id = input("Enter employee ID: ")
#             new_employee = Employee(Name=emp_name, Email=emp_email, Address=emp_address, Phone=emp_phone, Age=emp_age, Designation=emp_designation, Salary=emp_salary, EmployeeID=emp_id)
#             MHP_Restaurant.add_employee(new_employee)

#         elif choice == '3':
#             admin.view_employee(MHP_Restaurant)
#         elif choice == '4':
#             MHP_Restaurant.menu.show_menu()
#         elif choice == '5':
#             item_name = input("Enter the name of the item to remove: ")
#             MHP_Restaurant.menu.remove_item(item_name)
#         elif choice == '6':
#             print("Thank you for visiting!")
#             break
#         else:
#             print("Invalid choice. Please try again.")




# while True:
#         print("Welcome to the Restaurant Management System!")
#         print("1. Customer Menu")
#         print("2. Admin Menu")
#         print("3. Exit")

#         choice = input("Enter your choice: ")
#         if choice == '1':
#             customer_menu()
#         elif choice == '2':
#             admin_menu()
#         elif choice == '3':
#             print("Exiting the system. Thank you!")
#             break
#         else:
#             print("Invalid choice. Please try again.")





from Fooditem import FoodItem
from Restaurant import RestaurantSystem
from User import Customer, Admin, Employee
from Order import Order

# ----------------- Initialize Restaurant -----------------
MHP_Restaurant = RestaurantSystem("MHP_Restaurant")

# ----------------- Add 30 Sample Menu Items -----------------
sample_items = [
    ("Burger", 5.99, 50),
    ("Cheeseburger", 6.49, 50),
    ("Veggie Burger", 5.49, 50),
    ("French Fries", 2.99, 100),
    ("Cheese Fries", 3.49, 100),
    ("Onion Rings", 3.99, 80),
    ("Chicken Nuggets", 4.99, 60),
    ("Grilled Chicken Sandwich", 6.99, 40),
    ("Fish Sandwich", 6.49, 40),
    ("Caesar Salad", 4.99, 50),
    ("Greek Salad", 5.49, 50),
    ("Chicken Caesar Salad", 6.99, 40),
    ("Margherita Pizza", 8.99, 30),
    ("Pepperoni Pizza", 9.99, 30),
    ("Veggie Pizza", 8.49, 30),
    ("BBQ Chicken Pizza", 10.49, 25),
    ("Spaghetti Bolognese", 7.99, 35),
    ("Fettuccine Alfredo", 8.49, 35),
    ("Lasagna", 9.49, 30),
    ("Chicken Wings", 6.99, 60),
    ("Buffalo Wings", 7.49, 60),
    ("Garlic Bread", 2.99, 80),
    ("Mozzarella Sticks", 4.49, 70),
    ("Chocolate Cake", 3.99, 50),
    ("Cheesecake", 4.49, 50),
    ("Ice Cream Sundae", 3.49, 60),
    ("Brownie", 2.99, 60),
    ("Coke", 1.49, 100),
    ("Sprite", 1.49, 100),
    ("Lemonade", 1.99, 80)
]

for name, price, quantity in sample_items:
    MHP_Restaurant.menu.add_menu_item(FoodItem(name=name, price=price, quantity=quantity))

# ----------------- Customer Menu -----------------
def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")
    customer = Customer(Name=name, Email=email, Address=address, Phone=phone)

    while True:
        print(f"\nWelcome {customer.Name} to the restaurant!")
        print("1. View Menu")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Pay your bill")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            customer.view_menu(MHP_Restaurant)
        elif choice == '2':
            item_name = input("Enter the name of the item to add to cart: ")
            quantity = int(input("Enter the quantity: "))
            customer.add_to_cart(item_name, quantity, MHP_Restaurant)
        elif choice == '3':
            customer.view_cart()
        elif choice == '4':
            customer.pay_bill()
        elif choice == '5':
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice. Please try again.")

# ----------------- Admin Menu -----------------
def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")
    admin = Admin(Name=name, Email=email, Address=address, Phone=phone)

    while True:
        print(f"\nWelcome {admin.Name} to the restaurant!")
        print("1. Add New Menu Item")
        print("2. Add New Employee")
        print("3. View Employees")
        print("4. View Items in Menu")
        print("5. Remove Item from Menu")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            item_name = input("Enter the name of the item: ")
            price = float(input("Enter the price of the item: "))
            quantity = int(input("Enter the quantity of the item: "))
            item = FoodItem(name=item_name, price=price, quantity=quantity)
            admin.add_menu_item(MHP_Restaurant, item)

        elif choice == '2':
            emp_name = input("Enter employee name: ")
            emp_email = input("Enter employee email: ")
            emp_address = input("Enter employee address: ")
            emp_phone = input("Enter employee phone number: ")
            emp_age = int(input("Enter employee age: "))
            emp_designation = input("Enter employee designation: ")
            emp_salary = float(input("Enter employee salary: "))
            emp_id = input("Enter employee ID: ")

            new_employee = Employee(
                Name=emp_name,
                Email=emp_email,
                Address=emp_address,
                Phone=emp_phone,
                Age=emp_age,
                Designation=emp_designation,
                Salary=emp_salary,
                EmployeeID=emp_id
            )
            MHP_Restaurant.add_employee(new_employee)

        elif choice == '3':
            admin.view_employee(MHP_Restaurant)
        elif choice == '4':
            MHP_Restaurant.menu.show_menu()
        elif choice == '5':
            item_name = input("Enter the name of the item to remove: ")
            MHP_Restaurant.menu.remove_item(item_name)
        elif choice == '6':
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice. Please try again.")

# ----------------- Main Program -----------------
while True:
    print("\nWelcome to the Restaurant Management System!")
    print("1. Customer Menu")
    print("2. Admin Menu")
    print("3. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        customer_menu()
    elif choice == '2':
        admin_menu()
    elif choice == '3':
        print("Exiting the system. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")
# ----------------- End of Main Program -----------------