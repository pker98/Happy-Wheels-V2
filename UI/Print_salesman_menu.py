import os

class Print_salesman_menu(object):
    def __init__(self):
        pass
    
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
        print("2. Search for order\t6.Change password")
        print("3. Customer information\t7.Shortcuts instruction")
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
    
    def car_lists(self, plate, info):
        print("{}: {}".format(plate,info))

