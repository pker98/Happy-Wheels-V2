import os
class Cancel_order_Menu:
    def __init__(self):
        pass

    def find_by_num(self):
        os.system('cls||clear')
        print("~~Cancel order~~\n")
        order_num = input("Enter order number: ")
        return order_num

    def confirmation(self):
        print("Order successfully canceled!")
        input("Press enter to continue.")

    def print_order(self, order):
        print("\n"+str(order))

    def choice(self):
        choice = ""
        choice = input("Press d to delete order.")
        return choice
