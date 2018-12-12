from Models.Salesman import Salesman
from Repository.Salesman_repo import Salesman_repo
import os
class Print_information(object):
    def __init__(self):
        pass

    def information_main_page(self):
        """ Prints out the information window from main menu """
        os.system('cls||clear')
        print("\tHAPPY WHEELS")
        print("")
        print("Smiðjuvellir 13")
        print("IS-300,Akranes")
        print("Iceland")
        print("")
        print("Phone: 431-6000")
        print("happywheels@happywheels.is")
        print("")
        print("Id.no: 651174-0289")
        print("Tax nr: 14540")
        print("")
        print("----- © 2018-2018 Happy Wheels. -----")
        print("A. Car Rental Agreement")
        print("B. Terms and Conditions")
        print("C. Quality Policy")
        print("D. List of Employees")
        choice = input("Choose an option: ").lower()
        return choice
    
    def car_rental_agreement(self):
        """ Prints out the Car Rental Agreement """
        os.system('cls||clear')
        print("By using our services you therefore agree to us\n using your information to better our services.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    def terms_and_conditions(self):
        """ Prints out Terms and Conditions """
        os.system('cls||clear')
        print("Terms and conditions")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("By using our services you therefore agree to us\n using your information to better our services.")
    
    def quality_policy(self):
        """ Prints out the Quality Policy """
        os.system('cls||clear')
        print("By using our services you therefore agree to us\n using your information to better our services.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    def print_salesman(self, name, email, ID):
        """ Prints out a list of Employees """
        print("Name: {:20} Email: {:30} ID: {:20}".format(name,email,ID))
        
    def print_salesman_header(self):
        """Prints header for salesman list"""
        os.system('cls||clear')
        print("~~Salesmen~~\n")

        

        
            

            


  