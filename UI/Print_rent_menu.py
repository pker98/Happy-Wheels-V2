import os

class Print_rent_menu(object):
    def Page_1(self):
        """ Prints out the menu where the customer chooses 
        location to pick up his desired car """
        os.system('cls||clear')
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
        print("\t~ Date and time ~")
        print("\tPage 2 of 8\n") 
        pick_up_date = input("Enter pick up date(mm/dd/yyyy): ")
        # Pick_up_time = input("Enter pick up time(hh): ")
        drop_off_date = input("Enter drop off date(mm/dd/yyyy): ")
        # Drop_off_time = input("Enter drop off time(hh): ")

        return [pick_up_date, drop_off_date]

    def Page_3(self):
        os.system('cls||clear')
        print("\t~ Pick a car ~")
        print("\tPage 3 of 8\n")
        print("A. Small cars (from X kr. to Y kr.") # Hér er hægt að vera búinn að vera með breytu
        print("B. Medium cars (from X kr. to Y kr.")    # sem eru cheapest og most expensive bílar
        print("C. SUV (from X kr. to Y kr.")

        self.choice = input("Choose your vehicle size: ")
        return self.choice
    
    def Page_4(self, available_car_string, size_string):
        os.system('cls||clear')
        print(size_string)
        print(available_car_string)
        selected_car = input("Choose your desired car: ")

        return selected_car
        
    def Page_5(self, car_info):
        os.system('cls||clear')
        print(car_info)
        input("Press enter to confirm.")
        
    def Page_6(self):
        os.system('cls||clear')
        print("A. GPS ...5.000 kr.")
        print("B. Extra driver (max 2) ...1.000 kr.")
        print("C. Insurance (extra) ...6.500 kr.\n")
        print("Select an additional feature you want to add: ")
    
    def Page_7(self, car_info, price, date_info, features):
        os.system('cls||clear')
        print(car_info+"\n")
        print(date_info+"\n")
        print("~~Aditional features~~")
        print(features)

        print("Final price: {}".format(price))

        


        
