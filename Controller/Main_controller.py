from UI.Print_main_menu import Print_main_menu
from Controller.Rent_controller import Rent_controller
from Controller.Salesman_controller import Salesman_controller
from Controller.Order_controller import Order_controller

class Main_controller(object):
    def __init__(self):
        # Menus
        self.__main_menu = Print_main_menu()
        # Controllers
        self.__rent_controller = Rent_controller()
        self.__salesman_controller = Salesman_controller()
        self.order_controller = Order_controller()

    def Main_page(self):
        choice = ""
        while choice != "x":
            choice = self.__main_menu.main_page()
            if choice == "1":
                self.__rent_controller.Rent_page()
            elif choice == "2":
                self.__salesman_controller.sign_in_page()
            elif choice == "3":
                self.order_controller.cancel_order_process()