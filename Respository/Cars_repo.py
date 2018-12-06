from models.Car import Car
import csv

class Cars_repo(object):
    def __init__self(self):
        self.__cars = []

    # def add_video(self, Car):
    #     # first add to file then to private list
    #     with open("data/Cars.csv", "a+") as Cars_file:
    #         car_size = video.get_car_size()
    #         plate_number = video.get_plate_number()
    #         brand = get_video.brand()
    #         Cars_file.write("{},{},{}\n".format(car_size, plate_number, brand))

    def get_videos(self):
        if self.__cars == []:
            with open("./data/Cars.txt", "r") as Cars_file:
                csv_reader = csv.reader(Cars_file)
                next(csv_reader)
                car_dict = {}

                for line in csv_reader:
                    car_size, plate_number, brand
                    new_video = Video(title, genre, length)
                    self.__videos.append(new_video)    
        
        return self.__videos
