from UI.Print_main_menu import Print_main_menu
from UI.Print_salesman_menu import Print_salesman_menu
from Controller.Rent_controller import Rent_controller
from Services.Salesman_service import Salesman_service

class Salesman_controller(object):
    def __init__(self):
        self.__salesman = Print_salesman_menu() 
        self.__rent_car = Rent_controller()
        self.__get_info = Salesman_service()
        self.__main_page = Print_main_menu()
        # self.__get_customer_info = Customer_service() - Andri

    def sign_in_page(self):
        """Gets employee's ID and password and checks if it's valid"""
        valid = False
        while valid == False:
            # Get ID
            self.__ID = self.__salesman.ID_menu()
            # Get password 
            self.__password = self.__salesman.password_menu(self.__ID)
            #Check whether it's valid
            valid = self.__get_info.salesman_ID_pw(self.__ID,self.__password)
            if valid == False:
                try_again = input("\nID or password is invalid. Try again? (y/n): ").lower()
                if try_again != "y":
                    self.__main_page.main_page()

        # Prints Salesman menu
        self.__option = self.__salesman.salesman_main_page()
        # Get rent process
        if self.__option == "1":
            self.__rent_car.Rent_page()
        # Search for order
        elif self.__option == "2":
            pass
        # Get customer information
        elif self.__option == "3":
            # Andra kóði kemur hér
            pass
        # Get cars information
        elif self.__option == "4":
            self.__info_choice = self.__salesman.cars_info_menu()
            self.cars = self.__get_info.get_cars(self.__info_choice)
            for key,value in self.cars.items():
                self.__salesman.car_lists(key,value)
        elif self.__option == "5":
            pass
        elif self.__option == "6":
            pass
        elif self.__option == "7":
            pass