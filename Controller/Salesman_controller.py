from UI.Print_salesman_menu import Print_salesman_menu
from Controller.Rent_controller import Rent_controller
from Services.Customer_info import Customer_info

class Salesman_controller(object):
    def __init__(self):
        self.__employee = Print_salesman_menu() 
        self.__rent_car = Rent_controller()
        self.__get_customer_info = Customer_info
        # self.__get_cars_info = Employee_service()

    def sign_in_page(self):
        """Gets employee's ID and password and checks if it's valid"""
        # Get ID
        self.__ID = self.__employee.ID_menu()
        # Get password 
        self.__password = self.__employee.password_menu(self.__ID)
        #Check whether it's valid

        # Prints Salesman menu
        self.__option = self.__employee.salesman_main_page()
        # Get rent process
        if self.__option == "1":
            self.__rent_car.Rent_page()
        # Search for order
        elif self.__option == "2":
            pass
        # Get customer information
        elif self.__option == "3":
            self.__info_choice = self.__employee.customer_info_menu()
            self.customer = self.__get_customer_info.\
            __get_customer_info(self.__info_choice)
            for key,value in self.customer.items():
                self.__employee.customer_lists(key,value)
        # Get cars information
        elif self.__option == "4":
            self.__info_choice = self.__employee.cars_info_menu()
            self.cars = self.__get_cars_info.get_cars(self.__info_choice)
            for key,value in self.cars.items():
                self.__employee.car_lists(key,value)
        elif self.__option == "5":
            pass
        elif self.__option == "6":
            pass
        elif self.__option == "7":
            pass