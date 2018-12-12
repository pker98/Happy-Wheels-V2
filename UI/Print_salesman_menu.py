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
        print("4. Add car")

        choice = input("Choose an option: ")
        return choice
    
    def customer_info_menu(self):
        os.system("cls||clear")
        print("\t~Customer information~")
        cust_email = input("Enter customer email: ")
        self.email = cust_email
        return cust_email


    def customer_list(self, customer, orders):
        os.system("cls||clear")
        print('\t\t{}'.format(self.email))
        print("-"*60)
        print("~~Customer information~~")
        print(customer)
        print(orders)
        delete = ""
        delete = input("Press d to delete customer.")
        print("\n~~Customer orders~~\n")
        return delete

    def car_lists(self, plate, brand, location):
        print("Plate number: {:10}\tBrand: {:10}\tLocation: {:10}".format(plate,brand,location))

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
        print("{}\n{}".format(num, order))

    def print_log(self, log):
        print("\n"+log)

    def confirmation(self, confirmation_str, action):
        """Prints out confirmation string"""
        print("{} successfully {}!\n".format(confirmation_str, action))
        input("Press enter to continue.")

    def add_car(self):
        os.system("cls||clear")
        print("~~Add car~~\n")
        print("Sizes: a = Small car\tb = Medium car\tc = SUV")
        print("Locations: 1 = Reykjavík\t2 = Keflavík\t3 = Akureyri\n")
        plate_num = input("Enter plate number: ")
        brand = input("Enter car brand: ")
        size = input("Enter car size type (a,b,c): ")
        location = input("Enter location (1,2,3): ")
        return plate_num, brand, size, location 
        
    def print_cust_order(self, order):
        print(order)
