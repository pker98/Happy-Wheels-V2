from UI.Print_rent_menu import Print_rent_menu
from Services.Rent_service import Rent_service
from Utilizations.Rent_validation import Rent_validation
from UI.Print_error import Print_error
from Models.Customer import Customer
import datetime

class Rent_controller(object):
    def __init__(self):
        # UI's
        self.__rent_menu = Print_rent_menu()
        self.error = Print_error()
        # Services
        self.__Rent_service = Rent_service()   
        # Validations
        self.__Rent_valid = Rent_validation() 

    def Rent_page(self):
        """ User's process when renting a car, put together in a while 
        loop, set up page by page for easy navigation """
        Page = 1   # If user inputs correctly he will go on next page
        # While loop used so the user can navigate back and forth in the system
        while Page < 9: # Stops running when user has completed the rental process
            # Variables
            self.section_valid = 0 # Used on page 8 for validation
            if Page == 1:
                # Open location menu - Returns location - Checks if correct input
                self.location = self.__rent_menu.Page_1()
                Valid, Page = self.__Rent_valid.Check_location(self.location, Page)
                if Valid:
                    Page += 1   # Moves to next page
                elif Page == 0:
                    Page = 10
                else:
                    self.error.Wrong_location() # Prints error message

            elif Page == 2:
                # Open date option menu - Returns pick up- and drop off dates - Checks if correct input
                self.__date_str_list = self.__rent_menu.Page_2()
                Valid, Page = self.__Rent_valid.Check_date(self.__date_str_list, Page)
                if Valid:
                    Page += 1   # Moves to next page
                elif Page == 1:
                    pass    # Moves to previous page
                elif Page != 10:
                    self.error.Wrong_date() # Prints error message

            elif Page == 3:
                # Change the input from the user to date format, input was a string.
                self.date_list = self.__Rent_service.change_str_to_date(self.__date_str_list)
                
                # Open size option menu - Returns size of car - Checks if correct input
                self.vehicle_size = self.__rent_menu.Page_3()
                Valid, Page = self.__Rent_valid.Check_vehicle_size(self.vehicle_size, Page)
                if Valid:
                    Page += 1   # Moves to next page
                elif Page == 2:
                    pass    # Moves to previous page
                elif Page != 10:
                    self.error.Wrong_vehicle_size() # Prints error message

            elif Page == 4:
                # Finds available cars using information from the user
                available_car_list = self.__Rent_service.find_available_cars(self.date_list, \
                self.vehicle_size, self.location)
                # Returns available cars as a string.
                available_car_string = self.__Rent_service.make_carlist_string(available_car_list)
                # Gets right name of size category, i.e. 1 = small cars, 2 = medium cars, 3 = SUV
                self.size_string = self.__Rent_service.get_car_size_string(self.vehicle_size)

                # Opens available cars menu - Returns chosen car - Checks if correct input
                self.car_choice = self.__rent_menu.Page_4(available_car_string, self.size_string)
                Valid, Page = self.__Rent_valid.Check_car_choice(self.car_choice, Page)
                if Valid:
                    Page += 1   # Moves to next page
                elif Page == 3:
                    pass    # Moves to previous page
                elif Page != 10:
                    self.error.Wrong_car_choice()   # Prints error message 

            elif Page == 5:
                # Feature_list resetted from page 6 - happens if user goes back one page
                self.feature_list, self.feature_string = self.__Rent_service.reset_features()
                # Use the self.car_choice to find the desired car in the car list and returns a car_obj
                car_obj = self.__Rent_service.get_desired_car(self.car_choice)
                # Returns car from the user's inputs
                self.car_info = self.__Rent_service.desired_car_info()  

                # Opens up confirmation menu - Returns confirmation - Checks if correct input
                choice = self.__rent_menu.Page_5(self.car_info)
                Valid, Page = self.__Rent_valid.Check_confirmation(choice, Page)
                if Valid:
                    Page += 1   # Moves to next page
                elif Page == 4:
                    pass    # Moves to previous page
                elif Page != 10:
                    self.error.Wrong_key_pressed()   # Prints error message 

            elif Page == 6:
                # Date info string, takes the self.date_list and turns it into a string.
                self.date_info = self.__Rent_service.make_date_str(self.date_list)
                # Opens up additional features page - Returns chosen car - Checks if correct input
                while 5 < Page < 7:
                    choice = self.__rent_menu.Page_6()
                    Valid, Page = self.__Rent_valid.Check_feature(choice, Page)
                    if Valid and choice != "n":
                        self.feature_list = self.__Rent_service.add_features(choice)
                        # Makes string of the features added
                        self.feature_string = self.__Rent_service.make_feature_string(choice)
                    elif Valid and choice == "n":
                        Page += 1 # Moves to next page
                        break
                    elif not Valid and choice not in ("x", "p", "m") and Page != 10:
                        self.error.Wrong_feature_choice()   # Prints error message
                
            if Page == 7:
                # Returns final price
                price = self.__Rent_service.get_price(self.feature_list, car_obj)
                choice = self.__rent_menu.Page_7(self.car_info, price, self.date_info, self.feature_string)
                Valid, Page = self.__Rent_valid.Check_confirmation(choice, Page)
                if Valid:
                    Page += 1 # Moves to next page
                elif Page == 6:
                    pass    # Moves to previous page
                elif Page != 10:
                    self.error.Wrong_key_pressed()   # Prints error message 

            elif Page == 8:
                # Opens up personal information menus, split to 2 sections - Returns personal info - Checks if correct input
                if self.section_valid == 0:
                    personal_info_list_1 = first_name, last_name, date_of_birth, email, choice = self.__rent_menu.Page_8_1()
                    Valid, Page = self.__Rent_valid.Check_personal_info_1(personal_info_list_1, Page)
                elif self.section_valid == 1:
                    personal_info_list_2 = country, address, zip_code, phone, driver, choice = self.__rent_menu.Page_8_2()
                    Valid, Page = self.__Rent_valid.Check_personal_info_2(personal_info_list_2, Page)

                if Valid:
                    if self.section_valid == 1:
                        Page += 1   # Moves to next page
                    self.section_valid = 1
                elif Page == 7:
                    pass    # Moves to previous page
                elif Page != 10:
                    if self.section_valid == 0:
                        self.error.Wrong_personal_info_1()
                    elif self.section_valid == 1:
                        self.error.Wrong_personal_info_2()

            elif Page == 9:
                # Opens up payment method menu - Returns payment method - Checks if correct input
                choice = self.__rent_menu.Page_9()
                Valid, Page = self.__Rent_valid.Check_payment(choice, Page)
                if Valid:
                    Page += 1
                elif Page == 8:
                    pass    # Moves to previous page
                else:
                    self.error.Wrong_car_choice()   # Prints error message 
                    
            elif Page == 10:
                if choice in ("1", "2"):    # Opens credit/debit card payment menu
                    card, security_code, exp_date = self.__rent_menu.Page_10_1()
                elif choice == "3":         # Opens up 
                    card, security_code, exp_date = self.__rent_menu.Page_10_2()
        
        new_customer = Customer(first_name, last_name, date_of_birth, email, country, address, zip_code, phone, card, security_code, exp_date)
        
        # Receipt print
        self.__rent_menu.Page_11(new_customer, self.car_info, self.date_info, self.feature_string)
        
        # Booking number and thank you page
        booking_num = self.__Rent_service.make_booking_num()
        self.__Rent_service.add_order_to_dict(booking_num, email, car_obj.get_plate_number(), self.date_list)
        self.__Rent_service.update_customer_repo(new_customer)
        self.__rent_menu.Page_12(booking_num)

        self.__Rent_service.update_log(first_name, last_name, car_obj, self.date_list)









            
