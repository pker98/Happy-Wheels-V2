from UI.Print_rent_menu import Print_rent_menu
from Services.Rent_service import Rent_service

class Rent_controller(object):
    def __init__(self):
        # Menus
        self.__rent_menu = Print_rent_menu()
        # Service
        self.__Rent_service = Rent_service()    # Notar input (1-3), finnur staðsetningu, skilar location 

    def Rent_page(self):
        # Open location menu - Returns location
        self.__location = self.__rent_menu.Page_1()
        # Open date option menu - Returns pick up- and drop off dates
        self.__date_list = self.__rent_menu.Page_2()
        # Open size option menu - Returns size of car
        self.__vehicle_size = self.__rent_menu.Page_3()

        # Returns available cars with information from user
        available_car_list = self.__Rent_service.find_available_cars(self.__date_list, \
        self.__vehicle_size, self.__location)
        # Returns and constructs a string, takes available_car_list and makes it a string.
        available_car_string = self.__Rent_service.make_carlist_string()

        # Opens available cars menu - Returns chosen car
        self.size_string = self.__Rent_service.get_car_size_string(self.__vehicle_size)
        self.__car_choice = self.__rent_menu.Page_4(available_car_string, self.size_string)

        # Use the self.__car_choice to find the desired car in the car list and makes a desired car obj
        # This definition does not return anything, it makes a self.obj used in the desired_car_info
        car_obj = self.__Rent_service.get_desired_car(self.__car_choice)
        
        # All info on car printed out to the user, user needs to press enter to confirm car.
        self.car_info = self.__Rent_service.desired_car_info()
        self.__rent_menu.Page_5(self.car_info)

        # Date info string, takes the self.__date_list and turns it into a string.
        self.date_info = self.__Rent_service.make_date_str(self.__date_list)

        # Additional features page
        self.__rent_menu.Page_6()
        feature_list = self.__Rent_service.add_features()
        feature_string = self.__Rent_service.make_feature_string()

        # Check out
        price = self.__Rent_service.get_price(feature_list, car_obj)
        self.__rent_menu.Page_7(self.car_info, price, self.date_info, feature_string)
        








            
