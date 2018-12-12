from Respository.Orders_repo import Orders_repo
from Models.Order import Order
class Cancel_order_service:
    def __init__(self):
        self.orders_repo = Orders_repo()

    def delete_order(self, key):
        order_dict = self.orders_repo.get_orders()
        for plate_num, orders in order_dict.items():
            for order in orders:
                if key == order.get_order_num():
                    orders.remove(order)
        self.orders_repo.update_order_file(order_dict)

    def print_order(self, key):
        order_dict = self.orders_repo.get_orders()
        for plate_num, orders in order_dict.items():
            for order in orders:
                if key == order.get_order_num():
                    return order
        

                
            

