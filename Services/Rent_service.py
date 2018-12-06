from Respository.Cars_repo import Cars_repo

class Rent_service(object):
    def __init__(self):
        self.car_class = Cars_repo()

    def compare_date_size(self, date, size, location):
        """Get car_dict from repo and get inputs from Rent controller. 
        Compare to get available car."""
        self.dict = self.car_class.get_cars()
        return [date, location, size, self.dict]

