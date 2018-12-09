from UI.Print_rent_menu import Print_rent_menu
from Services.Rent_service import Rent_service
from Utilizations.Rent_validation import Rent_validation
from UI.Print_error import Print_error

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
        Page = 0   # If user inputs correctly he will go on next page
        # While loop used so the user can navigate back and forth in the system
        while Page < 7: # Stops running when user has completed the rental process
            if Page == 0:
                # Open location menu - Returns location - Checks if correct input
                self.location = self.__rent_menu.Page_1()
                Valid, Page = self.__Rent_valid.Check_location(self.location, Page)
                if Valid:
                    Page += 1
                elif Page == 1:
                    # Goes to main menu
                    pass
                else:
                    self.error.Wrong_location()
            elif Page == 1:
                # Open date option menu - Returns pick up- and drop off dates - Checks if correct input
                self.date_list = self.__rent_menu.Page_2()
                Valid, Page = self.__Rent_valid.Check_date(self.date_list, Page)
                if Valid:
                    Page += 1
                elif Page == 0:
                    pass    # Moves to previous page
                else:
                    self.error.Wrong_date()
            elif Page == 2:
                # Open size option menu - Returns size of car - Checks if correct input
                self.vehicle_size = self.__rent_menu.Page_3()
                Valid, Page = self.__Rent_valid.Check_vehicle_size(self.vehicle_size, Page)
                if Valid:
                    Page += 1
                elif Page == 1:
                    pass    # Moves to previous page
                else:
                    self.error.Wrong_vehicle_size()
            elif Page == 3:
                # Finds available cars using information from the user
                self.__Rent_service.find_available_cars(self.date_list, \
                self.vehicle_size, self.location)
                # Returns available cars as a string.
                available_car_string = self.__Rent_service.make_carlist_string()
                # Gets right name of size category, i.e. 1 = small cars, 2 = medium cars, 3 = SUV
                self.size_string = self.__Rent_service.get_car_size_string(self.vehicle_size)

                # Opens available cars menu - Returns chosen car - Checks if correct input
                self.car_choice = self.__rent_menu.Page_4(available_car_string, self.size_string)
                Valid, Page = self.__Rent_valid.Check_car_choice(self.car_choice, Page)
                if Valid:
                    Page += 1
                elif Page == 2:
                    pass    # Moves to previous page
                else:
                    self.error.Wrong_car_choice()    
            elif Page == 4:
                # Use the self.car_choice to find the desired car in the car list and makes a car object in service
                # This definition does not return anything, it makes a self.obj used in the desired_car_info in Rent_service
                self.__Rent_service.get_desired_car(self.car_choice)
                
                # Opens up confirmation menu - Enter to continue - No validation needed
                self.car_info = self.__Rent_service.desired_car_info()  # Returns car from the user's inputs
                self.__rent_menu.Page_5(self.car_info)
                Page += 1
            elif Page == 5:
                # Date info string, takes the self.date_list and turns it into a string.
                self.date_info = self.__Rent_service.make_date_str(self.date_list)

                # Additional features page
                # Validation check in service
                self.__rent_menu.Page_6()
                feature_list = self.__Rent_service.add_features()
                feature_string = self.__Rent_service.make_feature_string()  ### Bæta við navigation ###
                Page += 1
            elif Page == 6:
                # Check out
                price = self.__Rent_service.get_price(feature_list)
                self.__rent_menu.Page_7(self.car_info, price, self.date_info, feature_string)
        








            
