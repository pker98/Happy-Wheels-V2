import os
from Models.Customer import Customer

class Print_rent_menu(object):
    def __init__(self):
        self.main_header = "Press 'p' for Previous page\tPress 'm' for Menu\tPress 'x' to Exit"
        self.receipt_header = "Press 'm' for Main menu\tPress 'x' to Exit"

    def Page_1(self):
        """ Prints out the menu where the customer chooses 
        location to pick up his desired car """
        os.system('cls||clear')
        print(self.main_header)
        print("\t~ Location ~")
        print("\tPage 1 of 8\n")
        print("Select pick up location:")
        print("1. Reykjavík")
        print("2. Keflavík")
        print("3. Akureyri")
        choice = input("Choose an option: ").lower()

        return choice

    def Page_2(self):
        """ Prints out the menu where the customer chooses 
        date to pick up his desired car """
        os.system('cls||clear')
        print(self.main_header)
        print("\t~ Date and time ~")
        print("\tPage 2 of 8\n") 
        pick_up_date = input("Enter pick up date(mmddyyyy): ")
        drop_off_date = input("Enter drop off date(mmddyyyy): ")

        return [pick_up_date, drop_off_date]

    def Page_3(self):
        os.system('cls||clear')
        print(self.main_header)
        print("\t~ Pick a car ~")
        print("\tPage 3 of 8\n")
        print("A. Small cars") # Hér er hægt að vera búinn að vera með breytu
        print("B. Medium cars")    # sem eru cheapest og most expensive bílar
        print("C. SUV")
        choice = input("Choose your vehicle size: ").lower()

        return choice
    
    def Page_4(self, available_car_string, size_string):
        os.system('cls||clear')
        print(self.main_header)
        print(size_string)  # Kallar á samansettan streng
        print(available_car_string) # Kallar á samansettan streng
        choice = input("Choose your desired car: ").lower()

        return choice
        
    def Page_5(self, car_info):
        os.system('cls||clear')
        print(self.main_header)
        print(car_info)
        choice = input("Press 'c' to confirm: ").lower()

        return choice
        
    def Page_6(self):
        os.system('cls||clear')
        print(self.main_header)
        print("A. GPS ...5.000 kr.")
        print("B. Extra driver (max 2) ...1.000 kr.")   # Breyta í e-ð annað
        print("C. Insurance (extra) ...6.500 kr.\n")
        print("Press 'n' to continue to check out")
        choice = input("Choose an option: ")
        
        return choice
    
    def Page_7(self, car_info, price, date_info, features):
        os.system('cls||clear')
        print(self.main_header)
        print(car_info+"\n")
        print(date_info+"\n")
        print("~~Additional features~~")
        print(features)
        print("Final price: {}".format(price))
        choice = input("Press 'c' to confirm: ").lower()

        return choice

    def Page_8_1(self):
        os.system('cls||clear')
        print(self.main_header)
        first_name = input("First name: ")
        last_name = input("Last name: ")
        date_of_birth = input("Date of birth(mmddyyyy): ")
        email = input("Email: ")
        choice = input("Press 'c' to confirm: ").lower()

        return first_name, last_name, date_of_birth, email, choice

    def Page_8_2(self):
        os.system('cls||clear')
        print(self.main_header)
        country = input("Country: ")
        address = input("Address: ")
        zip_code = input("Zip code: ")
        phone = input("Phone number: ")
        choice = input("Press 'c' to confirm: ").lower()

        return country, address, zip_code, phone, choice
    
    def Page_9(self):
        os.system('cls||clear')
        print(self.main_header)
        print("1. Pay now with credit card")
        print("2. Pay now with debit card.")
        print("3. Pay when I pick up.")
        choice = input("Choose payment method: ")

        return choice
    
    def Page_10_1(self):
        os.system('cls||clear')
        print(self.main_header)
        print("~~Card info~~")
        card_num = input("Input card number(xxxx xxxx xxxx xxxx): ")
        security_code = input("Input security code(xxx): ")
        exp_date = input("Enter expiration date(mmyy): ")
        choice = input("Press 'c' to confirm: ").lower()

        return card_num, security_code, exp_date, choice

    def Page_10_2(self):
        os.system('cls||clear')
        print(self.main_header)
        print("~~Insurance~~")
        print("Enter your creditcard information for insurance")
        card_num = input("Input card number(xxxx xxxx xxxx xxxx): ")
        security_code = input("Input security code(xxx): ")
        exp_date = input("Enter expiration date(mmyy): ")
        print("If you do not show up or forget to cancel order, the company will charge you full price")
        choice = input("Press 'c' to confirm: ").lower()

        return card_num, security_code, exp_date, choice
    
    def Page_11(self, New_customer, car_info, date_info, feature_string):
        os.system('cls||clear')
        print(self.main_header)
        print("~~Check-out~~")
        print(New_customer)
        print(car_info)
        print(date_info)
        print(feature_string)
        choice = input("Press 'c' to confirm: ").lower()

        return choice

    def Page_12(self, booking_num):
        os.system('cls||clear')
        print(self.receipt_header)
        print("Thanks for using our service and hope to see you soon!")
        print("Your booking number is: {}".format(booking_num))
        print("The receipt will be sent to your email, along with the booking number.")
        input("Press enter to go back to main menu ")
        
