from Respository.Cars_repo import Cars_repo
from Models.Car import Car

class Rent_service(object):
    def __init__(self):
        self.car_class = Cars_repo()
       

    def compare_date_size(self, date, size, location):
        """Get car_dict from repo and get inputs from Rent controller. 
        Compare to get available car."""
        available_car_list = []
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
                        available_car_list.append(value)
                        break
                    else:
                        break
        return available_car_list


