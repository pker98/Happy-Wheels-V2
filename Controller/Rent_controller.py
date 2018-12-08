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
        self.__Rent_service = Rent_service()    # Notar input (1-3), finnur staðsetningu, skilar location
        # Validations
        self.__Rent_valid = Rent_validation() 


    def Rent_page(self):
        Page = 0   # If user inputs correctly he will go on next page
        while Page < 3: # Stops running when user has 
            if Page == 0:
                # Open location menu - Returns location - Checks if correct input
                self.location = self.__rent_menu.Page_1()
                if self.__Rent_valid.Check_location(self.location):
                    Page += 1
                else:
                    self.error.Wrong_location()
            elif Page == 1:
                # Open date option menu - Returns pick up- and drop off dates - Checks if correct input
                self.date_list = self.__rent_menu.Page_2()
                if self.__Rent_valid.Check_date(self.date_list):
                    Page += 1
                else:
                    self.error.Wrong_date()
            elif Page == 2:
                # Open size option menu - Returns size of car - Checks if correct input
                self.vehicle_size = self.__rent_menu.Page_3()
                if self.__Rent_valid.Check_vehicle_size(self.vehicle_size):
                    Page += 1
                else:
                    self.error.Wrong_vehicle_size()

        # Returns available cars using information from the user
        self.__Rent_service.find_available_cars(self.date_list, \
        self.vehicle_size, self.location)
        # Constructs a string, takes available_car_list and returns a string.
        available_car_string = self.__Rent_service.make_carlist_string()

        # Opens available cars menu - Returns chosen car - Checks if correct input
        self.size_string = self.__Rent_service.get_car_size_string(self.vehicle_size)
        self.car_choice = self.__rent_menu.Page_4(available_car_string, self.size_string)
        
        # Use the self.car_choice to find the desired car in the car list and makes a desired car obj
        # This definition does not return anything, it makes a self.obj used in the desired_car_info
        car_obj = self.__Rent_service.get_desired_car(self.car_choice)
        
        # All info on car printed out to the user, user needs to press enter to confirm car.
        self.car_info = self.__Rent_service.desired_car_info()
        self.__rent_menu.Page_5(self.car_info)

        # Date info string, takes the self.__date_list and turns it into a string.
        self.date_info = self.__Rent_service.make_date_str(self.date_list)

        # Additional features page
        self.__rent_menu.Page_6()
        feature_list = self.__Rent_service.add_features()
        feature_string = self.__Rent_service.make_feature_string()

        # Check out
        price = self.__Rent_service.get_price(feature_list, car_obj)
        self.__rent_menu.Page_7(self.car_info, price, self.date_info, feature_string)
        








            
