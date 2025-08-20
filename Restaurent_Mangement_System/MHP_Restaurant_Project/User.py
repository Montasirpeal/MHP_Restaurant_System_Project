# #customer 
# #employee
# #admin

# from abc import ABC
# from Order import Order



# # User class er moddhe common properties thakbe

# class User(ABC):
#     def __init__(self, Name , Email, Address, Phone):
#         self.Name = Name
#         self.Email = Email
#         self.Address = Address
#         self.Phone = Phone






# # Customer class er moddhe customer specific properties thakbe
# class Customer(User):
#     def __init__(self, Name, Email, Address, Phone):
#         super().__init__(Name, Email, Address, Phone)
#         self.cart= Order()  # Initialize an empty cart for the customer


#     def view_menu(self, RestaurantSystem):
#         RestaurantSystem.menu.show_menu()
        

#     def add_to_cart(self, item_name, quantity, RestaurantSystem):
#         item = RestaurantSystem.menu.find_item(item_name) 
#         if item :
#             if quantity > item.quantity:
#                 print(f"Sorry, only {item.quantity} of {item_name} is available.")
#                 return

#             item.quantity = quantity  # Update the item's quantity
#             self.cart.add_item(item)  # Add the item to the cart
#             print(" item added ")

#         else:
#             print(f"Item '{item_name}' not found in the menu.")
          
    
#     def view_cart(self):
#         if self.cart:
#             print("Cart Items:")
#             print("Name\tPrice\tQuantity")
#             for item , quantity in self.cart.items.items():
#                 print(f"Name: {item.name}, Price: {item.price}, Quantity: {quantity}")
#             print(f"Total Price: {self.cart.total_price()}")

    
#     def pay_bill(self):
#         print("Payment successful. Thank you for your order!")
#         self.cart.clear()


# #Employee class er moddhe employee specific properties thakbe

 
# class Employee(User):
#     def __init__( self, Name, Email, Address, Phone, Age , Designation , Salary , EmployeeID ):
#         super().__init__(Name, Email, Address, Phone)
#         self.Age = Age
#         self.Designation = Designation
#         self.Salary = Salary
#         self.EmployeeID = EmployeeID



# # Admin class er moddhe admin specific properties thakbe

# class Admin(User):
#     def __init__(self, Name, Email, Address, Phone):
#         super().__init__(Name, Email, Address, Phone)
        
# # Admin class er moddhe employee add korar method thakbe

#     def add_employee(self, RestaurantSystem, new_employee):
#         RestaurantSystem.add_employee(new_employee)
        

#     def view_employee(self, RestaurantSystem):
#         RestaurantSystem.view_employee()

#     def add_menu_item(self, RestaurantSystem, item):
#         RestaurantSystem.menu.add_menu_item(item)

#     def remove_menu_item(self, RestaurantSystem, item_name):
#         RestaurantSystem.menu.remove_item(item_name)




# # MHP_Restaurant = RestaurantSystem("MHP_Restaurant")
# # mn = Menu()
# # item = FoodItem("Pizza", 200, 5)
# # item1 = FoodItem("Burger", 100, 10)
# # admin = Admin("peal", "mh@mail.com", "Dhaka", "01700000000")
# # admin.add_menu_item(MHP_Restaurant, item)
# # admin.add_menu_item(MHP_Restaurant, item1)
# # mn.add_menu_item(item)
# # mn.add_menu_item(item1)


# # Customer1 = Customer("Peal" , " ttt@mail" , "Dhaka" , "01700000000")
# # Customer1.view_menu(MHP_Restaurant)

# # item_name = input("Enter the item name to add to cart: ")
# # item_quantity = int(input("Enter the quantity: "))
# # Customer1.add_to_cart(item_name, item_quantity, MHP_Restaurant)
# # Customer1.view_cart()


from abc import ABC
from Order import Order

class User(ABC):
    def __init__(self, Name, Email, Address, Phone):
        self.Name = Name
        self.Email = Email
        self.Address = Address
        self.Phone = Phone

class Customer(User):
    def __init__(self, Name, Email, Address, Phone):
        super().__init__(Name, Email, Address, Phone)
        self.cart = Order()

    def view_menu(self, RestaurantSystem):
        RestaurantSystem.menu.show_menu()

    def add_to_cart(self, item_name, quantity, RestaurantSystem):
        item = RestaurantSystem.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print(f"Sorry, only {item.quantity} of {item_name} is available.")
                return
            # Add a copy to cart to avoid modifying original quantity
            cart_item = type(item)(item.name, item.price, quantity)
            self.cart.add_item(cart_item)
            print(f"{quantity} x {item_name} added to cart.")
        else:
            print(f"Item '{item_name}' not found in the menu.")

    def view_cart(self):
        if self.cart.items:
            print("Cart Items:")
            print("Name\tPrice\tQuantity")
            for item, quantity in self.cart.items.items():
                print(f"{item.name}\t{item.price}\t{quantity}")
            print(f"Total Price: {self.cart.total_price()}")
        else:
            print("Cart is empty.")

    def pay_bill(self):
        print(f"Payment successful. Total amount: {self.cart.total_price()}. Thank you!")
        self.cart.clear()

class Employee(User):
    def __init__(self, Name, Email, Address, Phone, Age, Designation, Salary, EmployeeID):
        super().__init__(Name, Email, Address, Phone)
        self.Age = Age
        self.Designation = Designation
        self.Salary = Salary
        self.EmployeeID = EmployeeID

class Admin(User):
    def __init__(self, Name, Email, Address, Phone):
        super().__init__(Name, Email, Address, Phone)

    def add_employee(self, RestaurantSystem, new_employee):
        RestaurantSystem.add_employee(new_employee)

    def view_employee(self, RestaurantSystem):
        RestaurantSystem.view_employee()

    def add_menu_item(self, RestaurantSystem, item):
        RestaurantSystem.menu.add_menu_item(item)

    def remove_menu_item(self, RestaurantSystem, item_name):
        RestaurantSystem.menu.remove_item(item_name)
