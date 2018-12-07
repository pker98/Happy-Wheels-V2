from Respository.Cars_repo import Cars_repo
from Models.Car import Car
import os

class Rent_service(object):
    def __init__(self):
        self.car_class = Cars_repo()
       

    def find_available_cars(self, date, size, location):
        """Get car_dict from repo and get inputs from Rent controller. 
        Compare to get available car."""
        self.available_car_list = []
        self.dict = self.car_class.get_cars()
        for value in self.dict.values():
            if location == value.get_location() and size == value.get_car_size():
                pick_up, drop_off = date
                pick_up = int(pick_up)
                drop_off = int(drop_off)
                old_orders = value.get_orders()
                for order in old_orders:
                    old_pick_up, old_drop_off = order
                    if (old_drop_off < pick_up and old_drop_off < drop_off) or \
                    (old_pick_up > pick_up and old_pick_up > drop_off): 
                        self.available_car_list.append(value)
                        break
                    else:
                        break
        return self.available_car_list

    def get_car_size_string(self, choice):
        """Converts choice of size (a,b,c) to a string which represents the size name (Small, Medium, SUVs)"""
        if choice == "a":
            string = "Small cars"
        elif choice == "b":
            string = "Medium cars"
        elif choice == "c":
            string = "SUVs"
        return string

    def make_carlist_string(self):
        """Constructs a string made from the car_list to print out for the user"""
        carlist_string = ""
        for index, car in enumerate(self.available_car_list):
            carlist_string += ("Car {}: {}\n".format(index+1, car.get_brand()))
        return carlist_string

    def get_desired_car(self, car_choice):
        """Uses self.user_input to index car in the car_list, makes the car object, self.desired_car"""
        num_choice = int(car_choice)
        self.desired_car = self.available_car_list[num_choice-1]
        return self.desired_car

    def desired_car_info(self):
        "Takes the desired car object and return all of its attributes in a string"
        string = ""
        string += "~~{}~~\n".format(self.desired_car.get_brand())
        string += "\n"
        string += "Location: {}\n".format(self.desired_car.get_location_string())

        price, insurance = self.desired_car.get_pri_ins()
        string += "Base price: {}\nInsurance: {}".format(price, insurance)
        return string

    def get_feature_string(self):
        """Converts user_input (a,b,c) to string (GPS, Extra Driver, Extra Insurance)"""
        if self.user_input == "a":
            return "GPS"
        elif self.user_input == "b":
            return "Extra Driver"
        elif self.user_input == "c":
            return "Extra Insurance"
    
    def get_index(self):
        """Get index of the additional feature the user wants to remove"""
        for index, feature in enumerate(self.feature_list):
            if feature == self.user_input:
                return index

    def add_features(self):
        """Adds features to list, returns list"""
        self.user_input = ""
        self.feature_list = []
        while self.user_input != "n":
            self.user_input = input().lower()

            # Get string from the user_input which we then use when printing added! or removed! statements.
            feature_string = self.get_feature_string()

            # Get index of the user_input to find it in the list, returns the index and then we
            # use the index to remove the feature from the list
            index = self.get_index()
           
            if self.user_input in ("a","b","c") and self.user_input not in self.feature_list:
                print("{} added!".format(feature_string))
                self.feature_list.append(self.user_input)
            elif self.user_input in self.feature_list:
                print("{} removed!".format(feature_string))
                self.feature_list.pop(index)

            print("Press n to continue to check out!")
        return self.feature_list

    def get_price(self, feature_list, car_obj):
        """Returns final price for the customer, takes the list of additional features and calculates the price."""
        price, insurance = car_obj.get_pri_ins()
        final_price = int(price) + int(insurance)
        for feature in feature_list:
            if feature == "a":
                final_price += 5000
            elif feature == "b":
                final_price += 1000
            elif feature == "c":
                final_price += 6500
        return str(final_price)

    def make_date_str(self, date):
        """Takes the self.__date_list and turns it into a string"""
        pick_up, drop_off = date
        date_info = "Pickup date: {}\nDrop off date: {}".format(pick_up, drop_off)
        return date_info
    
    def make_feature_string(self):
        feature_string = ""
        for self.user_input in self.feature_list:
            feature_string += "{}\n".format(self.get_feature_string())
        if feature_string == "":
            return "None\n"
        return feature_string









