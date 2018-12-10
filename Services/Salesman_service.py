from Respository.Cars_repo import Cars_repo
from Respository.Salesman_repo import Salesman_repo
from Models.Salesman import Salesman 
from Respository.Customer_repo import Customer_repo
from Models.Customer import Customer
from Respository.Log_repo import Log_repo 

class Salesman_service(object):
    def __init__(self):
        # Repo's
        self.cars_info = Cars_repo()
        self.salesman_info = Salesman_repo()
        self.customer_info = Customer_repo()
        self.log_repo = Log_repo()
    
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

    def get_customer(self, email):
        #nær í customer keys úr dict 
        self.customer_dict = self.customer_info.get_customer()
        #ef keyið passar input frá notanda, returna value úr þeim key
        for key, value in self.customer_dict.items():
            if key == email:
                return [value.get_name(), value.get_phone(), value.get_creditcard()]


    def make_cust_value_string(self, value_list):
        return "Name: {}\tPhone: {}\tCreditcard: {}".format(value_list[0], value_list[1], value_list[2])

    def salesman_ID_pw(self,ID, pw):
        valid = False
        salesman_dict = self.salesman_info.get_salesmen()
        for key, value in salesman_dict.items():
            if key == ID and pw == value.get_password():
                self.logged_salesman = key
                valid = True
                return valid
        return valid

    def change_pw(self, new_pw):
        salesman_dict = self.salesman_info.get_salesmen()
        for key, value in salesman_dict.items():
            if key == self.logged_salesman:
                salesman_object = value
                value.change_pw(new_pw)
                break
        self.salesman_info.update_data(salesman_dict)
        update_repo = self.log_repo
        update_repo.Update_repo("{} changed his password. ID: {}".format(salesman_object.get_name(), salesman_object.get_ID()))



        