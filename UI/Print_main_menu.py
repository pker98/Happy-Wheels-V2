import os

class Print_main_menu(object):
    def main_page(self):
        """ Prints out the main menu for the user """
        os.system('cls||clear')
        print("Press 'I' for information  Press 'X' for exit")
        print(" _    _          _____  _______     __   __          ___    _ ______ ______ _       _____")
        print("| |  | |   /\   |  __ \|  __ \ \   / /   \ \        / / |  | |  ____|  ____| |     / ____|")
        print("| |__| |  /  \  | |__) | |__) \ \_/ /     \ \  /\  / /| |__| | |__  | |__  | |    | (___  ")
        print("|  __  | / /\ \ |  ___/|  ___/ \   /       \ \/  \/ / |  __  |  __| |  __| | |     \___ \ ")
        print("| |  | |/ ____ \| |    | |      | |         \  /\  /  | |  | | |____| |____| |____ ____) |")
        print("|_|  |_/_/    \_\_|    |_|      |_|          \/  \/   |_|  |_|______|______|______|_____/ ")
        print("")
        print("\t\t\t\t          ,-----,     ")
        print("\t\t\t\t        ,--'---:---`--,")
        print("\t\t\t\t ~ ~ ~ ==(o)-----(o)==J")
        print("\t\t\t\tMain menu")
        print("")
        print("1. Continue as a Customer")
        print("2. Continue as a Salesman")
        print("3. Cancel an existing order")

        choice = input("Choose an option: ").lower()
        return choice