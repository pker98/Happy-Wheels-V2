from Respository.Cars_repo import Cars_repo
from Respository.Salesman_repo import Salesman_repo
from Models.Salesman import Salesman 

class Salesman_service(object):
    def __init__(self):
        self.cars_info = Cars_repo()
        self.salesman_info = Salesman_repo()
    
    def get_cars(self, choice):
        self.cars_dict = self.cars_info.get_cars()
        
        if choice == "1":
            return self.cars_dict
        elif choice == "2":
            for car_info in self.cars_dict.values():
            # If car_info.get_status == available(True?) þá append hann í available listann
                pass 
        elif choice == "3":
            # If car_info.get_status == unavailable(False?) þá append hann í unavailable listann  
            pass

    def salesman_ID_pw(self,ID, pw):
        valid = False
        salesman_dict = self.salesman_info.get_salesmen()
        for key, value in salesman_dict.items():
            if key == ID and pw == value.get_password():
                valid = True
                return valid

        return valid

        