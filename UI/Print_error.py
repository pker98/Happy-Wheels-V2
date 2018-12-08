import os

class Print_error():
        
    def Wrong_location(self):
        os.system('cls||clear')
        print("Something went wrong")
        print("Wrong input | Choose option 1 - 3")
        input("Press enter to continue ")

    def Wrong_date(self):
        os.system('cls||clear')
        print("Something went wrong")
        print("Wrong input | Date format: mmddyyyy")
        input("Press enter to continue ")

    def Wrong_vehicle_size(self):
        os.system('cls||clear')
        print("Something went wrong")
        print("Wrong input | Choose option A, B or C")
        input("Press enter to continue ")