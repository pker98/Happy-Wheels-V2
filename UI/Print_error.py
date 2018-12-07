import os

class Print_error():
    def __init__(self):
        pass

    def Wrong_location(self):
        os.system('cls||clear')
        print("Wrong input | Choose option 1 - 3")
        input("Press enter to continue ")

    def Wrong_date(self):
        os.system('cls||clear')
        print("Wrong input | Date format: mmddyyyy")
        input("Press enter to continue ")