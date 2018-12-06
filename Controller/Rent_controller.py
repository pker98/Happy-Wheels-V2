from UI.Print_rent_menu import Print_rent_menu

class Rent_controller(object):
    def __init__(self):
        # Menus
        self.__rent_menu = Print_rent_menu()
        # Service
        # self.__get_location = Rent_service()    # Notar input (1-3), finnur staðsetningu, skilar location 

    def Rent_page(self):
        # Fá location
        self.__location = self.__rent_menu.Page_1()
        # Fá date
        self.__date_time_list = self.__rent_menu.Page_2()
        # Fá 
        self.__vehicle_size = self.__rent_menu.Page_3()


            
