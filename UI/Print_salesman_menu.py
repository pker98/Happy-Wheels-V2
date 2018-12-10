import os

class Print_salesman_menu(object):
    
    def ID_menu(self):
        os.system("cls||clear")
        print("\t~Log in~")
        id = input("Enter your ID: ")
        return id
    
    def password_menu(self, id):
        os.system("cls||clear")
        print("\t~Log in~")
        print("ID:", id)
        password = input("Enter your password: ") 
        return password
    
    def salesman_main_page(self):
        os.system("cls||clear")
        print("\t~Salesman menu~")
        print("1. Rent a car\t\t5. Operation LOG")
        print("2. Search for order\t6. Change password")
        print("3. Customer information")
        print("4. Cars information")

        choice = input("Choose an option: ")
        return choice

    def cars_info_menu(self):
        os.system("cls||clear")
        print("\t~Cars information~")
        print("1. Overview of all cars")
        print("2. Overview of all available cars")
        print("3. Overview of all unavailable cars")
        print("4. Find car")
        print("5. Add car")

        choice = input("Choose an option: ")
        return choice
    
    def customer_info_menu(self):
        os.system("cls||clear")
        print("\t~Customer information~")
        cust_email = input("Enter customer email: ")
        self.email = cust_email
        return cust_email


    def customer_list(self, value_list):
        os.system("cls||clear")
        print('\t\t{}'.format(self.email))
        print("-"*60)
        print("\t\tCustomer info")
        print(value_list)

    def car_lists(self, plate, brand, location):
        print("Plate number: {}\tBrand: {}\tLocation: {}".format(plate,brand,location))

    def get_new_pw(self):
        new_pw = input("Enter new password: ")
        return new_pw

    def find_order_page(self):
        os.system("cls||clear")
        print("\t~Find order~\n")
        booking_num = input("Enter the booking number for the order: ")
        return booking_num
    
    def print_orders(self, num, order):
        print("\t~Find order~\n")
        print("{}. {}".format(num, order))

    def print_log(self, log):
        print("\n"+log)

