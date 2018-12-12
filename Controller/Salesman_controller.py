from UI.Print_main_menu import Print_main_menu
from UI.Print_salesman_menu import Print_salesman_menu
from UI.Print_error import Print_error
from Controller.Rent_controller import Rent_controller
from Services.Salesman_service import Salesman_service
from Repository.Log_repo import Log_repo
from Controller.Order_controller import Order_controller

class Salesman_controller(object):
    def __init__(self):
        # UI's
        self.__salesman_menu = Print_salesman_menu() 
        # Controllers
        self.__rent_controller = Rent_controller()
        self.__order_controller = Order_controller()
        # Services
        self.__salesman_service = Salesman_service()
        # Variables
        self.confirmation_str = ""
        

    def sign_in_page(self):
        """Gets employee's ID and password and checks if it's valid"""
        valid = False
        while valid == False:
            # Get ID
            self.__ID = self.__salesman_menu.ID_menu()
            # Get password 
            self.__password = self.__salesman_menu.password_menu(self.__ID)
            #Check whether it's valid
            valid = self.__salesman_service.salesman_ID_pw(self.__ID,self.__password)
            if valid == False:
                try_again = input("\nID or password is invalid. Try again? (y/n): ").lower()
                if try_again != "y":
                    break

        # Prints Salesman menu
        self.__option = self.__salesman_menu.salesman_main_page()
        # Get rent process
        if self.__option == "1":
            self.__rent_controller.Rent_page()
        # Search for order
        elif self.__option == "2":
            self.__order_controller.cancel_order_process()
        # Get customer information
        elif self.__option == "3":
            self.email = self.__salesman_menu.customer_info_menu()
            customer = self.__salesman_service.get_customer(self.email)
            if type(customer) is object:
                orders = self.__salesman_service.order_string()
            else:
                orders = ""
            delete = self.__salesman_menu.customer_list(customer, orders)
            if delete == "d":
                self.__salesman_service.delete_customer(customer)
                self.confirmation_str = "Customer"
                action = "removed"
                self.__salesman_service.delete_customer_to_log(self.__ID)
                self.__salesman_menu.confirmation(self.confirmation_str, action)
        # Get cars information
        elif self.__option == "4":
            self.__choice = self.__salesman_menu.cars_info_menu()
            if self.__choice == "1":
                self.cars = self.__salesman_service.get_all_cars()
            elif self.__choice == "2":
                self.cars = self.__salesman_service.get_available_cars()
            elif self.__choice == "3":
                self.cars = self.__salesman_service.get_unavailable_cars()
            elif self.__choice == "4":
                plate_num, brand, size, location = self.__salesman_menu.add_car()
                self.__salesman_service.add_car_repo(plate_num, brand, size, location)
                self.confirmation_str = "Car"
                action = "added"
                self.__salesman_menu.confirmation(self.confirmation_str, action)
                #Add to log
                self.__salesman_service.add_to_log(self.__ID, brand, plate_num)


            if self.__choice in ["1","2","3"]:
                for car in self.cars:
                    plate_number = car.get_plate_number()
                    brand = car.get_brand()
                    location = car.get_location_string()
                    self.__salesman_menu.car_lists(plate_number, brand, location)
                input("")
        elif self.__option == "5":
            log = self.__salesman_service.get_log()
            self.__salesman_menu.print_log(log)
            input("")
        elif self.__option == "6":
            new_pw = self.__salesman_menu.get_new_pw()
            self.__salesman_service.change_pw(new_pw)
            input("")