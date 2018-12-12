import os

class Print_error():
    def Wrong_location(self):
        os.system('cls||clear')
        print("Invalid location")
        print("Choose option 1 - 3\n")
        input("Press enter to continue ")

    def Wrong_date(self):
        os.system('cls||clear')
        print("Invalid date")
        print("Date format: mmddyyyy\n")
        input("Press enter to continue ")
        
    def Wrong_vehicle_size(self):
        os.system('cls||clear')
        print("Invalid vehicle size")
        print("Choose option A, B or C\n")
        input("Press enter to continue ")

    def Wrong_car_choice(self):
        os.system('cls||clear')
        print("Invalid car")
        print("Choose option 1 - 5\n")
        input("Press enter to continue ")
    
    def Wrong_key_pressed(self):
        os.system('cls||clear')
        print("Invalid key")
        print("Choose 'c' to confirm\n")
        input("Press enter to continue")

    def Wrong_feature_choice(self):
        os.system('cls||clear')
        print("Invalid feature")
        print("Choose option A, B or C\n") 
        input("Press enter to continue ")  

    def Wrong_personal_info_1(self):  # first_name, last_name, date_of_birth, email
        os.system('cls||clear')
        print("Invalid personal info\n")
        print("One of the following went wrong: ")
        print("\t1. Names can not contain numbers")
        print("\t2. You have to be 21 years old to rent a car")
        print("\t3. Date format: mmddyyyy")
        print("\t4. Emails must contain '@' and '.'\n")
        input("Press enter to continue ")  

    def Wrong_personal_info_2(self):    # country, zip_code, phone,
        os.system('cls||clear')
        print("Invalid personal info\n")
        print("One of the following went wrong:")
        print("\t1. Country can not contain numbers")
        print("\t2. Zip Code can not contain letters")
        print("\t3. Phone can not contain letters\n")
        input("Press enter to continue ")

    def Wrong_payment_metho(self):
        os.system('cls||clear')
        print("Invalid payment method\n")
        print("Choose option 1 - 3\n")
        input("Press enter to continue ")