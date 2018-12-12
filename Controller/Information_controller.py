from UI.Print_information import Print_information
from Services.Information_service import Information_service
from Models.Salesman import Salesman


class Information_controller(object):
    def __init__(self):
        self.__information_menu = Print_information()
        self.info_service = Information_service()
    def information_page(self):
        choice = self.__information_menu.information_main_page()
        if choice == "a":
            self.__information_menu.car_rental_agreement()
            input("")

        elif choice == "b":
            self.__information_menu.terms_and_conditions()
            input("")
        
        elif choice == "c":
            self.__information_menu.quality_policy()
            input("")

        elif choice == "d":
            salesman_dict = self.info_service.get_salesman_dict()
            self.__information_menu.print_salesman_header()
            for ID, salesman in salesman_dict.items():
                name = salesman.get_name()
                email = salesman.get_email()
                self.__information_menu.print_salesman(name, email, ID)
            input("")