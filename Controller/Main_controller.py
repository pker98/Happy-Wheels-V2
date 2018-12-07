from UI.Print_main_menu import Print_main_menu
from Controller.Rent_controller import Rent_controller
from Controller.Salesman_controller import Salesman_controller

class Main_controller(object):
    def __init__(self):
        # Menus
        self.__main_menu = Print_main_menu()
        # Controllers
        self.__rent_controller = Rent_controller()
        self.__salesman_controller = Salesman_controller()

    def Main_page(self):
        self.__choice = self.__main_menu.main_page()
        if self.__choice == "1":
            self.__rent_controller.Rent_page()
        elif self.__choice == "2":
            self.__salesman_controller.sign_in_page()