from Respository.Orders_repo import Orders_repo
from UI.Cancel_order_menu import Cancel_order_Menu
from Services.Cancel_order_service import Cancel_order_service


class Order_controller:
    def __init__(self):
        self.cancel_service = Cancel_order_service()

    
    def cancel_order_process(self):
        menu = Cancel_order_Menu()
        order_num = menu.find_by_num()
        order = self.cancel_service.print_order(order_num)
        menu.print_order(order)
        choice = menu.choice()
        if choice == "d":
            self.cancel_service.delete_order(order_num)
            menu.confirmation()




