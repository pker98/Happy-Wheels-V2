from UI.Print_rent_menu import Print_rent_menu
from Services.Rent_service import Rent_service

class Rent_controller(object):
    def __init__(self):
        # Menus
        self.__rent_menu = Print_rent_menu()
        # Service
        self.__get_cars = Rent_service()    # Notar input (1-3), finnur staðsetningu, skilar location 

    def Rent_page(self):
        # Fá location
        self.__location = self.__rent_menu.Page_1()
        # Fá date
        self.__date_list = self.__rent_menu.Page_2()
        # Fá 
        self.__vehicle_size = self.__rent_menu.Page_3()
        #bera saman car_dict og locaton, date_list og size
        
        compare = self.__get_cars.compare_date_size(self.__date_list, \
        self.__vehicle_size, self.__location)
        return compare



            
