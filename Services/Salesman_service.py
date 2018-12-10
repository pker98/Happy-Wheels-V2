from Respository.Cars_repo import Cars_repo
from Respository.Salesman_repo import Salesman_repo
from Models.Salesman import Salesman 
from Respository.Customer_repo import Customer_repo
from Models.Customer import Customer
from Respository.Log_repo import Log_repo 
from Respository.Orders_repo import Orders_repo
import datetime

class Salesman_service(object):
    def __init__(self):
        # Repo's
        self.cars_info = Cars_repo()
        self.salesman_info = Salesman_repo()
        self.customer_info = Customer_repo()
        self.log_repo = Log_repo()
        self.get_orders_dict = Orders_repo()
    
    def get_cars(self, choice):
        self.cars_dict = self.cars_info.get_cars()
        
        if choice == "1":
            return self.cars_dict.values()

        elif choice == "2":
            self.available_car_list = []
            car_dict = self.cars_info.get_cars()
            today = datetime.date.today()
            for value in car_dict.values():
                old_orders = value.get_orders()
                if old_orders != []:
                    for order in old_orders:
                        old_pick_up, old_drop_off = order
                        if (old_pick_up <= today <= old_drop_off): 
                            valid = False
                        else:
                            valid = True

                    if valid == True:
                        self.available_car_list.append(value)
                else:
                    self.available_car_list.append(value)                          
            return self.available_car_list

        elif choice == "3":
            self.unavailable_car_list = []
            car_dict = self.cars_info.get_cars()
            today = datetime.date.today()
            for value in car_dict.values():
                old_orders = value.get_orders()
                if old_orders != []:
                    for order in old_orders:
                        old_pick_up, old_drop_off = order
                        if (old_pick_up <= today <= old_drop_off): 
                            valid = True
                        else:
                            valid = False

                    if valid == True:
                        self.unavailable_car_list.append(value)
                                          
            return self.unavailable_car_list
            

    def get_customer(self, email):
        #nær í customer keys úr dict 
        self.customer_dict = self.customer_info.get_customers()
        #ef keyið passar input frá notanda, returna value úr þeim key
        for key, value in self.customer_dict.items():
            if key == email:
                return "Name: {}\tPhone: {}".format(value.get_first_name(), value.get_phone())


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

    def get_order_info(self, booking_num):
        order_list = []
        order_dict = self.get_orders_dict.get_orders()
        for values in order_dict.values():
            for order in values:
                if booking_num == order.get_order_num():
                    order_list.append(order)
        
        return order_list

    def get_log(self):
        return self.log_repo.Read_repo()


        