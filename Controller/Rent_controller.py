from UI.Print_rent_menu import Print_rent_menu
from Services.Rent_service import Rent_service

class Rent_controller(object):
    def __init__(self):
        # Menus
        self.__rent_menu = Print_rent_menu()
        # Service
        self.__get_cars = Rent_service()    # Notar input (1-3), finnur staðsetningu, skilar location 

    def Rent_page(self):
        # Open location menu - Returns location
        self.__location = self.__rent_menu.Page_1()
        # Open date option menu - Returns pick up- and drop off dates
        self.__date_list = self.__rent_menu.Page_2()
        # Open size option menu - Returns size of car
        self.__vehicle_size = self.__rent_menu.Page_3()

        # Returns available cars with information from user
        available_car_list = self.__get_cars.find_available_cars(self.__date_list, \
        self.__vehicle_size, self.__location)

        # Opens available cars menu - Returns chosen car
        self.__car_choice = self.__rent_menu.Page_4(available_car_list)





            
