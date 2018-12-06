import os

class Print_main_menu(object):
    def main_page(self):
        """ Prints out the main menu for the user """
        os.system('cls||clear')
        print("Press 'I' for information  Press 'X' for exit")
        print("\tMain menu")
        print("\tHAPPY WHEELS")
        print("1. Continue as a Customer")
        print("2. Continue as a Salesman")
        print("3. Cancel an existing order")

        choice = input("Choose an option: ").lower()
        return choice