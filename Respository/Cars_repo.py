from Models.Car import Car
import csv

class Cars_repo:
    def __init__self(self):
        pass

    # def add_video(self, Car):
    #     # first add to file then to private list
    #     with open("data/Cars.csv", "a+") as Cars_file:
    #         car_size = video.get_car_size()
    #         plate_number = video.get_plate_number()
    #         brand = get_video.brand()
    #         Cars_file.write("{},{},{}\n".format(car_size, plate_number, brand))

    def get_cars(self):
        self.car_dict = {}
        with open("./data/Cars.csv", "r") as Cars_file:
            csv_reader = csv.reader(Cars_file)
            next(csv_reader)
            
            for line in csv_reader:
                plate_num, brand, size, location = line
                new_car = Car(plate_num, brand, size, location)
                key = new_car.get_plate_number() #key er platenumber
            
                self.car_dict[key] = new_car

        return self.car_dict

