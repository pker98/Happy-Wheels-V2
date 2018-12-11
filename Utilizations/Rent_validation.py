# from Controller.Main_controller import Main_controller
import datetime

class Rent_validation():
    def __init__(self):
        # self.__main_controller = Main_controller()
        pass

    def Check_if_nav(self, user_input, page):
        """ Checks if user input is p for previous, h for home or x for exit
        before doing anything else """
        if user_input == "p":   # Goes to previous page
            page -= 1
        elif user_input == "m": # Goes back to start of program (Main_controller)
            # self.__main_controller.Main_page()
            pass
        elif user_input == "x": # Exits 
            exit()
        return page

    def Check_location(self, location, page):
        """ Checks if user input is a valid location """
        self.__check_nav = Rent_validation()    # Makes instance of Rent_validation class to call Check_if_nav, used in all Check functions
        page = self.__check_nav.Check_if_nav(location, page)    # Checks if user input is equal to p, m or X (navigation)
        if location in ("1", "2", "3"):
            return True, page
        else:
            return False, page

    def Check_date(self, dates, page): # mm//dd//yyyy
        for date in dates:
            page = self.__check_nav.Check_if_nav(date, page)    # Checks if user input is equal to p, m or X (navigation)
        pick_up = dates[0]
        drop_off = dates[1]
        # Time after exactly 5 years
        date_after_5years = datetime.date.today() + datetime.timedelta(365*5)  
        # Checks if dates are valid
        try:
            pickup_date = datetime.date(int(pick_up[4:8]), int(pick_up[:2]), int(pick_up[2:4]))
            dropoff_date = datetime.date(int(drop_off[4:8]), int(drop_off[:2]), int(drop_off[2:4]))
        except(ValueError):
            return False, page
        # Checks if pick_up- and drop_off dates are bigger than the date today and smaller than the date after 5 years
        # Also checks if pick_up date is smaller than drop_off date
        if datetime.date.today() < pickup_date < date_after_5years \
            and datetime.date.today() < dropoff_date < date_after_5years \
            and pickup_date < dropoff_date:         
            return True, page
        else: 
            return False, page

    def Check_vehicle_size(self, vehicle_size, page):
        page = self.__check_nav.Check_if_nav(vehicle_size, page)    # Checks if user input is equal to p, m or X (navigation)
        if vehicle_size in ("a", "b", "c"):
            return True, page
        else:
            return False, page

    def Check_car_choice(self, car_choice, page):
        page = self.__check_nav.Check_if_nav(car_choice, page)  # Checks if user input is equal to p, m or X (navigation)
        if car_choice in ("1", "2", "3", "4", "5"):
            return True, page
        else:
            return False, page

    def Check_confirmation(self, choice, page):
        page = self.__check_nav.Check_if_nav(choice, page)  # Checks if user input is equal to p, m or X (navigation)    
        if choice == "c":
            return True, page
        else:
            return False, page

    def Check_feature(self, feature_choice, page):
        page = self.__check_nav.Check_if_nav(feature_choice, page)  # Checks if user input is equal to p, m or X (navigation)
        if feature_choice in ("a", "b", "c", "n"):
            return True, page
        else:
            return False, page

    def Check_payment(self, payment_choice, page):
        page = self.__check_nav.Check_if_nav(payment_choice, page)  # Checks if user input is equal to p, m or X (navigation)
        if payment_choice in ("1", "2", "3"):
            return True, page
        else:
            return False, page