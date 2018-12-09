import os

class Print_error():

    def Wrong_location(self):
        return "Wrong input | Choose option 1 - 3")

    def Wrong_date(self):
        return "Wrong input | Date format: mmddyyyy")

    def Wrong_vehicle_size(self):
        return "Wrong input | Choose option A, B or C")

    def Wrong_car_choice(self):
        return "Wrong input | Choose option 1 - 5")

    def Wrong_feature_choice(self):
        return "Wrong input | Choose option A, B or C")    

    def All_errors(self):
        self.error = Print_error()
        os.system('cls||clear')
        print("Something went wrong")
        # Breytanleg
        input("Press enter to continue ")

    