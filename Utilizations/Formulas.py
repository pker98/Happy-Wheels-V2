import datetime

class Formulas:
    def __init__(self):
        pass
    
    def calculate_price(self, base_price, date_list, additional_price):
        """ Calculates base price of car * days rented """
        pick_up, drop_off = date_list
        days = drop_off - pick_up
        price = (base_price * days.days) + additional_price
        return price