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
                    available_car_list.append(value)
        return available_car_list


