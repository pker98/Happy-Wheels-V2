import os

class Print_rent_menu(object):
    def __init__(self):
        self.header = "Press 'p' for Previous page\tPress 'm' for Menu\tPress 'x' to Exit"

    def Page_1(self):
        """ Prints out the menu where the customer chooses 
        location to pick up his desired car """
        os.system('cls||clear')
        print(self.header)
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
        print(self.header)
        print("\t~ Date and time ~")
        print("\tPage 2 of 8\n") 
        pick_up_date = input("Enter pick up date(mmddyyyy): ")
        drop_off_date = input("Enter drop off date(mmddyyyy): ")

        return [pick_up_date, drop_off_date]

    def Page_3(self):
        os.system('cls||clear')
        print(self.header)
        print("\t~ Pick a car ~")
        print("\tPage 3 of 8\n")
        print("A. Small cars (from X kr. to Y kr.") # Hér er hægt að vera búinn að vera með breytu
        print("B. Medium cars (from X kr. to Y kr.")    # sem eru cheapest og most expensive bílar
        print("C. SUV (from X kr. to Y kr.")
        choice = input("Choose your vehicle size: ").lower()

        return choice
    
    def Page_4(self, available_car_string, size_string):
        os.system('cls||clear')
        print(self.header)
        print(size_string)  # Kallar á samansettan streng
        print(available_car_string) # Kallar á samansettan streng
        choice = input("Choose your desired car: ").lower()

        return choice
        
    def Page_5(self, car_info):
        os.system('cls||clear')
        print(self.header)
        print(car_info)
        choice = input("Press 'c' to confirm: ").lower()

        return choice
        
    def Page_6(self):
        os.system('cls||clear')
        print(self.header)
        print("A. GPS ...5.000 kr.")
        print("B. Extra driver (max 2) ...1.000 kr.")
        print("C. Insurance (extra) ...6.500 kr.\n")
        print("Press 'n' to continue to check out")
        choice = input("Choose an option: ")
        
        return choice
    
    def Page_7(self, car_info, price, date_info, features):
        os.system('cls||clear')
        print(self.header)
        print(car_info+"\n")
        print(date_info+"\n")
        print("~~Additional features~~")
        print(features)
        print("Final price: {}".format(price))

        


        
